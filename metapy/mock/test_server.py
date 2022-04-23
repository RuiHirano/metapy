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
from lib.type import Rate, Tick
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

server = build_server()
client = connect_to_server()
count = 0

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

def on_tick():
    global count
    print("onTick")
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
            res = Response(action=ENUM_ORDER_ACTION.ORDER_ACTION_SEND, data=None, error=None)
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
        #print("prepare")
        #self.build_server()
        #self.connect_to_server()
        #prepare()
        wait_run_command()
        on_init()
    
    def next(self):
        on_tick()
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
    backtester = Backtester()
    backtester.run()
    #server = TestServer()
    #server.connect()
    #server.run_server()

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
