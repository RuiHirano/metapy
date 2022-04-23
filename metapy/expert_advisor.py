from lib.api import ENUM_EVENT_ACTION
from lib.type import Tick, ENUM_TIMEFRAME
from lib.order import Order
from lib.account import Account
from lib.market import Market
from lib.timeseries import Timeseries
from lib.client import Client, MockClient
from lib.api import API
from datetime import datetime
from lib.logger import log
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

    def connect(self, server_address, target_address):
        self.api = API(server_address, target_address)
        self.api.connect()

    def run(self):
        print("run")
        try:
            self.api.register_event(ENUM_EVENT_ACTION.EVENT_ACTION_ON_INIT, lambda data: self.on_init())
            self.api.register_event(ENUM_EVENT_ACTION.EVENT_ACTION_ON_TICK, lambda tick: self.on_tick(Tick(**tick)))
            self.api.register_event(ENUM_EVENT_ACTION.EVENT_ACTION_ON_DEINIT, lambda data: self.on_deinit())
            self.api.send_run_command()
            self.api.wait_event()
        except Exception as e:
            log.error(e)
            raise e


if __name__ == "__main__":
    class MyEA(ExpertAdvisor):
        def on_init(self):
            print("started on_init")

        def on_tick(self, tick: Tick):
            ticket = self.OrderSend("EURUSD", 0, 0, 0, 0, 0, 0)
            print("on_tick", tick.time)

        def on_deinit(self):
            print("on_deinit")

    ea = MyEA(debug=False, log_level="DEBUG")
    ea.connect(server_address="tcp://127.0.0.1:5556", target_address="tcp://127.0.0.1:5557")
    ea.run()

