from metapy import MetaPy

meta = MetaPy(
    server="http://localhost:5005",
    debug=True,
    log_level="DEBUG",
)

class MACrossStrategy:
    def __init__(self) -> None:
        pass

    def next(self, tick_data):
        meta.order.OrderSend("EURUSD",0,0,0,0,0,0)
        

@meta.OnInit()
def on_init():
    strategy = MACrossStrategy()
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