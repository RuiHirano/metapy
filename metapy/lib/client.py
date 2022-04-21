from datetime import datetime
import zmq

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
        
      