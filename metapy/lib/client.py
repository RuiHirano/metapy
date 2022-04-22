from datetime import datetime
import zmq
import json
from lib.order import ENUM_ORDER_ACTION

class Client:
    def __init__(self, server):
        self.server = server

    def connect(self):
        context = zmq.Context()
        # ReqRep
        self.client = context.socket(zmq.REQ)
        self.client.connect("tcp://127.0.0.1:5557")
        print("Connected to server")

    def send_message(self, data):
        pass
        
class MockClient:
    def __init__(self, server):
        self.server = server

    def connect(self):
        pass

    def send_message(self, data):
        data = json.loads(data)
        action = data["action"]
        if ENUM_ORDER_ACTION(action) == ENUM_ORDER_ACTION.ORDER_ACTION_SEND:
            res = {
                "data": {"ticket": 100}
            }
        elif ENUM_ORDER_ACTION(action) == ENUM_ORDER_ACTION.ORDER_ACTION_CLOSE:
            res = {
                "data": {"closed": True}
            }
        elif ENUM_ORDER_ACTION(action) == ENUM_ORDER_ACTION.ORDER_ACTION_MODIFY:
            res = {
                "data": {"modified": True}
            }
        elif ENUM_ORDER_ACTION(action) == ENUM_ORDER_ACTION.ORDER_ACTION_DELETE:
            res = {
                "data": {"deleted": True}
            }
        else:
            raise Exception("Unknown action")
        return res