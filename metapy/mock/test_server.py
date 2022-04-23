import os
import sys
from pathlib import Path
sys.path.append(str(Path(os.path.dirname(__file__)).joinpath('..').resolve()))
import zmq
import json
from backtesting import Strategy, Backtest
from backtesting.test import EURUSD
from lib.api import Request, Response
from lib.order import ENUM_ORDER_ACTION
from lib.api import ENUM_EVENT_ACTION
from lib.type import Rate, Tick, ENUM_ORDER_TYPE
from lib.timeseries import ENUM_TIMESERIES_ACTION
from datetime import datetime

def connect_to_server():
        # connect client
        target_address="tcp://127.0.0.1:5556"
        context = zmq.Context()
        client = context.socket(zmq.REQ)
        client.connect(target_address)
        print("Connected to server")
        return client

def build_server():
    # build server
    server_address="tcp://127.0.0.1:5557"
    context = zmq.Context()
    server = context.socket(zmq.REP)
    server.bind(server_address)
    print("Server started")
    return server

def wait_run_command():
    # EA <-isPrepared- Metapy
    # EA --------OK->  Metapy
    print("Waiting for run command")
    while True:
        message = server.recv()
        req = Request(**json.loads(message.decode()))
        if req.action == ENUM_EVENT_ACTION.EVENT_ACTION_RUN:
            print("Start Backtest")
            res = Response(action=ENUM_EVENT_ACTION.EVENT_ACTION_RUN, data=None, error=None)
            server.send_string(res.json())
            break

def on_init():
    print("onInit")
    # EA ----OnInit->  Metapy
    # EA <-OK-------- Metapy
    req = Request(action=ENUM_EVENT_ACTION.EVENT_ACTION_ON_INIT, data=None)
    client.send_string(req.json())
    message = client.recv()
    res = Response(**json.loads(message.decode()))
    if res.action == ENUM_EVENT_ACTION.EVENT_ACTION_ON_INIT:
        print("Start OnInit")
    
    while True:
        message = server.recv()
        req = Request(**json.loads(message.decode()))
        if req.action == ENUM_EVENT_ACTION.EVENT_ACTION_ON_INIT:
            # EA <-FinishOnInit- Metapy
            # EA --------  OK->  Metapy
            res = Response(action=ENUM_EVENT_ACTION.EVENT_ACTION_ON_INIT, data=None, error=None)
            server.send_string(res.json())
            break
    print("onInit finished")

def on_tick(strategy):
    global count
    print("onTick", strategy.data.Close)
    # EA ----OnTick->  Metapy
    # EA <-OK-------- Metapy
    tick = Tick(
        time=datetime.now(),
        bid=100,
        ask=100,
        last=100,
        volume=100,
        time_msc=100,
        flags=0,
        volume_real=100,
    )
    req = Request(action=ENUM_EVENT_ACTION.EVENT_ACTION_ON_TICK, data=tick)
    print(req.json())
    client.send_string(req.json())
    message = client.recv()
    res = Response(**json.loads(message.decode()))
    if res.action == ENUM_EVENT_ACTION.EVENT_ACTION_ON_TICK:
        print("Start OnTick: ", count)
        count += 1
    
    while True:
        message = server.recv()
        req = Request(**json.loads(message.decode()))
        if req.action == ENUM_EVENT_ACTION.EVENT_ACTION_ON_TICK:
            # EA <-FinishOnTick- Metapy
            # EA --------  OK->  Metapy
            res = Response(action=ENUM_EVENT_ACTION.EVENT_ACTION_ON_TICK, data=None, error=None)
            server.send_string(res.json())
            break
        elif req.action == ENUM_ORDER_ACTION.ORDER_ACTION_SEND:
            if req.data["type"] == ENUM_ORDER_TYPE.ORDER_TYPE_BUY:
                strategy.buy()
            if req.data["type"] == ENUM_ORDER_TYPE.ORDER_TYPE_SELL:
                strategy.sell()
            res = Response(action=ENUM_ORDER_ACTION.ORDER_ACTION_SEND, data=10000, error=None)
            server.send_string(res.json())
        elif req.action == ENUM_ORDER_ACTION.ORDER_ACTION_CLOSE:
            strategy.position.close()
            res = Response(action=ENUM_ORDER_ACTION.ORDER_ACTION_CLOSE, data=True, error=None)
            server.send_string(res.json())
        elif req.action == ENUM_TIMESERIES_ACTION.TIMESERIES_ACTION_GET_N_RATES_BY_START_POSITION:
            num = req.data["count"]
            if len(strategy.data.Close) < num:
                res = Response(action=ENUM_ORDER_ACTION.ORDER_ACTION_SEND, data=None, error="Not enough data")
            else:
                rates = [Rate(
                        time=datetime.now(),
                        open=strategy.data.Open[-i-1],
                        high=strategy.data.High[-i-1],
                        low=strategy.data.Low[-i-1],
                        close=strategy.data.Close[-i-1],
                        tick_volume=1,
                        spread=1,
                        real_volume=1,
                    ) for i in range(num)]
                res = Response(action=ENUM_ORDER_ACTION.ORDER_ACTION_SEND, data=rates, error=None)
            server.send_string(res.json())

    print("onTick finished")

def on_deinit():
    print("onDeinit")
    # EA ----OnInit->  Metapy
    # EA <-OK-------- Metapy
    req = Request(action=ENUM_EVENT_ACTION.EVENT_ACTION_ON_DEINIT, data=None)
    client.send_string(req.json())
    message = client.recv()
    res = Response(**json.loads(message.decode()))
    if res.action == ENUM_EVENT_ACTION.EVENT_ACTION_ON_DEINIT:
        print("Start OnDeinit")
    
    while True:
        message = server.recv()
        req = Request(**json.loads(message.decode()))
        if req.action == ENUM_EVENT_ACTION.EVENT_ACTION_ON_DEINIT:
            # EA <-FinishOnDeinit- Metapy
            # EA --------  OK->  Metapy
            res = Response(action=ENUM_EVENT_ACTION.EVENT_ACTION_ON_DEINIT, data=None, error=None)
            server.send_string(res.json())
            break
    print("onDeinit finished")

class MockMetatrader(Strategy):


    def init(self):
        wait_run_command()
        on_init()
    
    def next(self):
        on_tick(self)
        print("finish next")
        

class Backtester:
    def __init__(self):
        self.bt = Backtest(EURUSD[:100], MockMetatrader, cash=10_000, commission=.002)

    def run(self):
        stats = self.bt.run()
        ## On Deinit
        # EA ----OnDeinit->  Metapy
        # EA <-OK-------- Metapy
        print("OnDeinit")
        on_deinit()
        
        print(stats)

if __name__ == "__main__":
    server = build_server()
    client = connect_to_server()
    count = 0
    bt = Backtest(EURUSD[:100], MockMetatrader, cash=10_000, commission=.002)
    stats = bt.run()
    on_deinit()
    print(stats)

    ## Prepare
    # EA <-isPrepared- Metapy
    # EA --------OK->  Metapy
    # EA <-Start----- Metapy
    # EA --------OK->  Metapy
    ## On Init
    # EA ----OnInit->  Metapy
    # EA <-OK-------- Metapy
    # EA <-FinishOnInit- Metapy
    # EA --------  OK->  Metapy
    ## On Tick
    # EA ----OnTick->  Metapy
    # EA <-OK-------- Metapy
    # EA <-FinishOnTick- Metapy
    # EA --------  OK->  Metapy
    ## On Deinit
    # EA ----OnDeinit->  Metapy
    # EA <-OK-------- Metapy
    # EA <-FinishOnDeinit- Metapy
    # EA --------  OK->  Metapy
