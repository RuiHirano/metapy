from lib.order import Order
from lib.account import Account
from lib.client import Client, MockClient
from lib.callback import OnInitCallback, OnTickCallback, OnDeinitCallback
import logging
from rich.logging import RichHandler

class MetaPy:
    def __init__(
        self, 
        server,
        debug=False,
        log_level="INFO",
    ):
        logging.basicConfig(
            level=log_level,
            format="%(message)s",
            datefmt="[%X]",
            handlers=[RichHandler(rich_tracebacks=True)],
        )
        
        self.server = server
        self.client = Client(self.server) if not debug else MockClient(self.server)
        self.order = Order(self.client)
        self.account = Account(self.client)
        self.on_init = None
        self.on_tick = None
        self.on_deinit = None

    def OnInit(self):
        self.on_init = OnInitCallback()
        return self.on_init

    def OnDeinit(self):
        self.on_deinit = OnDeinitCallback()
        return self.on_deinit

    def OnTick(self):
        self.on_tick = OnTickCallback()
        return self.on_tick

    def run(self):
        if not self.on_init or not self.on_tick or not self.on_deinit:
            raise Exception("OnInit, OnTick, OnDeinit must be defined")
        err = self.client.connect()
        if err:
            raise Exception(err)

        self.on_init.run()
        mockdata = range(20)
        for i in range(10):
            self.on_tick.run(mockdata[i])
        self.on_deinit.run()
