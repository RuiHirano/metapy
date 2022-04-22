from metapy import MetaPy, ExpertAdvisor

class MACrossStrategy:
    def __init__(self) -> None:
        pass

    def next(self, tick):
        meta.order.OrderSend("EURUSD",0,0,0,0,0,0)

class MACrossEA(ExpertAdvisor):
    def on_init(self):
        self.strategy = MACrossStrategy()
        print("on_init")  

    def on_tick(self, tick):
        self.strategy.next(tick)
        print("on_tick", tick)

    def on_deinit(self):
        print("on_deinit")


if __name__ == "__main__":
    meta = MetaPy(
        ea=MACrossEA,
        server="http://localhost:5005",
        debug=True,
        log_level="DEBUG",
    )
    meta.run()