from metapy import MetaPy

meta = MetaPy()

class MACrossStrategy:
    def __init__(self, api) -> None:
        self.api = api

    def next(self, tick_data):
        self.api.order.OrderSend(0,0,0,0,0,0,0)
        

@meta.OnInit()
def on_init():
    strategy = MACrossStrategy(meta)
    meta.strategy = strategy
    print("on_init")

@meta.OnTick()
def on_tick(tick_data):
    meta.strategy.next(tick_data)
    print("on_tick", tick_data)

@meta.OnDeinit()
def on_deinit():
    print("on_deinit")


if __name__ == "__main__":
    meta.run()