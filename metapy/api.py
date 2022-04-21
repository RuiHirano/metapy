from lib.order import Order
from lib.account import Account
from lib.client import Client
from lib.callback import OnInitCallback, OnTickCallback, OnDeinitCallback

class MetaPy:
    def __init__(self, server="http://localhost:5005") -> None:
        self.server = server
        self.client = Client(self.server)
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

    def run(self, debug=False):
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

if __name__ == "__main__":
    meta = MetaPy()

    class Strategy:
        def __init__(self, api) -> None:
            self.api = api

        def next(self, tick_data):
            self.api.order.OrderSend(0,0,0,0,0,0,0)
            

    @meta.OnInit()
    def on_init():
        strategy = Strategy(meta)
        meta.strategy = strategy
        print("on_init")

    @meta.OnTick()
    def on_tick(tick_data: str):
        meta.strategy.next(tick_data)
        print("on_tick", tick_data)

    @meta.OnDeinit()
    def on_deinit():
        print("on_deinit")

    #on_init()
    meta.run()