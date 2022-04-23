from datetime import datetime
import zmq
import json
from lib.order import ENUM_ORDER_ACTION
from lib.timeseries import ENUM_TIMESERIES_ACTION
from lib.market import ENUM_MARKET_ACTION
from lib.account import ENUM_ACCOUNT_ACTION
from typing import Union, Any
from lib.type import Rate, Tick
from lib.logger import log
from enum import Enum
from pydantic import BaseModel

'''
Event Request:
{aciton: EVENT_ON_INIT, data: {}}
{aciton: EVENT_ON_TICK, data: {}}
{aciton: EVENT_ON_DEINIT, data: {}}
Other Request:
{action: ENUM_ORDER_ACTION.ORDER_ACTION_SEND, data: {anydata}}
'''

class ENUM_EVENT_ACTION(str, Enum):
    EVENT_ACTION_RUN = "EVENT_ACTION_RUN"
    EVENT_ACTION_ON_INIT = "EVENT_ACTION_ON_INIT"
    EVENT_ACTION_ON_TICK = "EVENT_ACTION_ON_TICK"
    EVENT_ACTION_ON_DEINIT = "EVENT_ACTION_ON_DEINIT"

class Request(BaseModel):
    action: Union[ENUM_EVENT_ACTION, ENUM_MARKET_ACTION, ENUM_ACCOUNT_ACTION, ENUM_TIMESERIES_ACTION, ENUM_ORDER_ACTION]
    data: Any

class Response(BaseModel):
    action: Union[ENUM_EVENT_ACTION, ENUM_MARKET_ACTION, ENUM_ACCOUNT_ACTION, ENUM_TIMESERIES_ACTION, ENUM_ORDER_ACTION]
    data: Any
    error: Union[str, None]

class API:
    def __init__(self, server_address, target_address):
        self.server_address = server_address
        self.target_address = target_address
        self.callbacks = {}

    def build_server(self):
        # build server
        server_address="tcp://127.0.0.1:5556"
        context = zmq.Context()
        self.server = context.socket(zmq.REP)
        self.server.bind(server_address)
        print("Built server")

    def connect_to_server(self):
        context = zmq.Context()
        self.client = context.socket(zmq.REQ)
        self.client.connect(self.target_address)
        print("Connected to server")

    def connect(self):
        self.build_server()
        self.connect_to_server()

    def send_run_command(self):
        print("Run")
        req = Request(action=ENUM_EVENT_ACTION.EVENT_ACTION_RUN, data=None)
        self.client.send_string(req.json())
        message = self.client.recv()
        res = Response(**json.loads(message.decode()))
        if not res.error:
            log.info("Connection is OK")
            return True
        
    def register_event(self, event, callback):
        self.callbacks[event] = callback

    def disconnect(self):
        self.server.close()
        self.client.close()

    def wait_event(self):
        log.info("Waiting events...")
        events = self.callbacks.keys()
        while True:
            message = self.server.recv()
            req = Request(**json.loads(message.decode()))
            if req.action in events:
                # Event Request
                res = Response(action=req.action, data="OK")
                self.server.send_string(res.json())
                log.debug("{} Started".format(req.action))
                self.callbacks[req.action](req.data)
                
                req = Request(action=req.action, data=None)
                self.client.send_string(req.json())
                message = self.client.recv()
                res = Response(**json.loads(message.decode()))
                if res.error:
                    log.error(res.error)
                else:
                    log.debug("{} Finished".format(req.action))

    def send_message(self, action, data):
        req = Request(action=action, data=data)
        self.client.send_string(req.json())
        message = self.client.recv()
        res = Response(**json.loads(message.decode()))
        if res.error:
            log.error(res.error)
        return res.data
        
        
class MockClient:
    def __init__(self, server):
        self.server = server

    def connect(self):
        pass

    def send_message(self, data):
        data = json.loads(data)
        action = data["action"]
        print(action)
        if ENUM_ORDER_ACTION(action) == ENUM_ORDER_ACTION.ORDER_ACTION_SEND:
            res = {
                "data": 100
            }
        elif ENUM_ORDER_ACTION(action) == ENUM_ORDER_ACTION.ORDER_ACTION_CLOSE:
            res = {
                "data": True
            }
        elif ENUM_ORDER_ACTION(action) == ENUM_ORDER_ACTION.ORDER_ACTION_MODIFY:
            res = {
                "data": True
            }
        elif ENUM_ORDER_ACTION(action) == ENUM_ORDER_ACTION.ORDER_ACTION_DELETE:
            res = {
                "data": True
            }
        elif ENUM_TIMESERIES_ACTION(action) == ENUM_TIMESERIES_ACTION.TIMESERIES_ACTION_GET_N_RATES_BY_START_POSITION:
            print("GetNRatesByStartPosition")
            res = {
                "data": [Rate(
                    time=datetime.now(),
                    open=1.0,
                    high=1.0,
                    low=1.0,
                    close=1.0,
                    tick_volume=1,
                    spread=1,
                    real_volume=1,
                )]
            }
        else:
            raise Exception("Unknown action")
        return res
