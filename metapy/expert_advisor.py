from lib.type import Tick, ENUM_TIMEFRAME
from lib.order import Order
from lib.account import Account
from lib.market import Market
from lib.timeseries import Timeseries
from lib.client import Client, MockClient
from datetime import datetime
import logging
from rich.logging import RichHandler

class ExpertAdvisor(Order, Account, Market, Timeseries):
    def __init__(self, debug=False, log_level="INFO"):
        self.debug = debug
        self.log_level = log_level
        self.connected = False

        logging.basicConfig(
            level=log_level,
            format="%(message)s",
            datefmt="[%X]",
            handlers=[RichHandler(rich_tracebacks=True)],
        )

    def on_init(self):
        raise NotImplementedError

    def on_tick(self, tick: Tick):
        raise NotImplementedError

    def on_deinit(self):
        raise NotImplementedError

    def connect(self, server):
        self.server = server
        self.client = Client(self.server) if not self.debug else MockClient(self.server)
        self.connected = True

    def run(self):
        print("run")
        if self.connected:
            self.on_init()
            for i in range(10):
                tick = Tick(
                    time=datetime.now(),
                    bid=i,
                    ask=i,
                    last=i,
                    volume=i,
                    time_msc=i,
                    flags=i,
                    volume_real=i
                )
                self.on_tick(tick)
            self.on_deinit()
        else:
            raise Exception("Not connected")


if __name__ == "__main__":
    class MyEA(ExpertAdvisor):
        def on_init(self):
            print("on_init")

        def on_tick(self, tick: Tick):
            ticket = self.OrderSend("EURUSD", 0, 0, 0, 0, 0, 0)
            print("on_tick", self.AccountBalance(), ticket)

        def on_deinit(self):
            print("on_deinit")

    ea = MyEA(debug=True, log_level="DEBUG")
    ea.connect(server="localhost:5555")
    ea.run()

