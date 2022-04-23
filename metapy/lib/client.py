from datetime import datetime
import zmq
import json
from lib.order import ENUM_ORDER_ACTION
from lib.timeseries import ENUM_TIMESERIES_ACTION
from lib.type import Rate

class Client:
    def __init__(self, server_address):
        self.server_address = server_address

    def build_server(self):
        # build server
        server_address="tcp://127.0.0.1:5556"
        context = zmq.Context()
        self.server = context.socket(zmq.REP)
        self.server.bind(server_address)
        print("Server started")

    def connect_to_server(self):
        context = zmq.Context()
        self.client = context.socket(zmq.REQ)
        self.client.connect(self.server_address)
        print("Connected to server")

    def connect(self):
        self.build_server()
        self.connect_to_server()
        

        # EA <-isPrepared- Metapy
        # EA --------OK->  Metapy
        self.client.send_string("isPrepared")
        res = self.client.recv()
        if res.decode() == "OK":
            print("Prepared")

        # OnInit
        # EA ----OnInit->  Metapy
        # EA <-OK-------- Metapy
        res = self.server.recv()
        if res.decode() == "OnInit":
            self.server.send_string("OK")
        while True:
            print("Start OnInit")
            # EA <-FinishOnInit- Metapy
            # EA --------  OK->  Metapy
            self.client.send_string("FinishOnInit")
            res = self.client.recv()
            if res.decode() == "OK":
                print("Finish OnInit")
                break

        # OnTick
        # EA ----OnTick->  Metapy
        # EA <-OK-------- Metapy
        count = 0
        while True:
            res = self.server.recv()
            # EA ----OnDeinit->  Metapy
            # EA <-OK-------- Metapy
            if res.decode() == "OnDeinit":
                print("Deinit")
                self.server.send_string("OK")
                break
            if res.decode() == "OnTick":
                self.server.send_string("OK")
            while True:
                print("Start OnTick: ", count)
                count += 1
                # EA <-FinishOnTick- Metapy
                # EA --------  OK->  Metapy
                self.client.send_string("FinishOnTick")
                res = self.client.recv()
                if res.decode() == "OK":
                    print("Finish OnTick")
                    break

        # OnDeinit
        while True:
            print("Start OnDeinit")
            # EA <-FinishOnDeinit- Metapy
            # EA --------  OK->  Metapy
            self.client.send_string("FinishOnDeinit")
            res = self.client.recv()
            if res.decode() == "OK":
                print("Finish OnDeinit")
                break
        

    def send_message(self, data):
        self.client.send_string(data)
        message = self.client.recv()
        #message2 = self.client.recv()
        #print(message2)
        res = json.loads(message.decode())
        print(res)
        return res
        
        
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
