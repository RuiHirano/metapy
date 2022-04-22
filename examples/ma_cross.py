from metapy import ExpertAdvisor, Tick, ENUM_TIMEFRAME, ENUM_ORDER_TYPE

def crossover(ma1, ma2):
    if ma1[-1] > ma2[-1] and ma1[-2] < ma2[-2]:
        return True
    return False

def sma(rates):
    result = []
    for rate in rates:
        result.append(1)
    return result

class MACrossEA(ExpertAdvisor):
    def on_init(self):
        self.symbol = "EURUSD"
        self.ticket = None
        print("on_init")  

    def on_tick(self, tick: Tick):
        print("on_tick", tick.time)
        rates_h1 = self.GetNRatesByStartPosition(self.symbol, ENUM_TIMEFRAME.PERIOD_H1, 0, 100)
        rates_m15 = self.GetNRatesByStartPosition(self.symbol, ENUM_TIMEFRAME.PERIOD_M15, 0, 100)
        sma_h1 = sma(rates_h1)
        sma_m15 = sma(rates_m15)
        
        if crossover(sma_m15, sma_h1):
            if self.ticket:
                self.OrderClose(self.ticket, 0, 0, 3)
            self.ticket = self.OrderSend(self.symbol, ENUM_ORDER_TYPE.ORDER_TYPE_BUY, 1, tick.ask, 3, 0, 0)
        elif crossover(sma_h1, sma_m15):
            if self.ticket:
                self.OrderClose(self.ticket, 0, 0, 3)
            self.ticket = self.OrderSend(self.symbol, ENUM_ORDER_TYPE.ORDER_TYPE_SELL, 1, tick.ask, 3, 0, 0)

    def on_deinit(self):
        print("on_deinit")


if __name__ == "__main__":
    ea = MACrossEA(
        debug=True,
        log_level="DEBUG",
    )
    ea.connect(server="localhost:5555")
    ea.run()
