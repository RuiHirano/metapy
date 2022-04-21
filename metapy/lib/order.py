
from datetime import datetime
import json


class Order:
    def __init__(self, client):
        self.client = client

    def OrderSend(
        self, 
        symbol: str, 
        cmd: int,
        volume: float,
        price: float,
        slippage: int,
        stoploss: float,
        takeprofit: float,
        comment: str = None,
        magic: int = 0,
        expiration: datetime = 0,
        allow_color = "clrNONE"
    ):
        data = json.dumps({
            "type": "ORDER_SEND",
            "symbol": symbol,
            "cmd": cmd,
            "volume": volume,
            "price": price,
            "slippage": slippage,
            "stoploss": stoploss,
            "takeprofit": takeprofit,
            "comment": comment,
            "magic": magic,
            "expiration": expiration,
            "allow_color": allow_color
        })
        res = self.client.send_message(data)
        return res

    def OrderClose(
        self,
        ticket: int,
        lots: float,
        price: float,
        slippage: int,
        allow_color: str
    ):
        data = json.dumps({
            "type": "ORDER_CLOSE",
            "ticket": ticket,
            "lots": lots,
            "price": price,
            "slippage": slippage,
            "allow_color": allow_color
        })
        res = self.client.send_message(data)
        return res

    def OrderCloseBy(
        self,
        ticket: int,
        opposite: int,
        allow_color: str
    ):
        data = json.dumps({
            "type": "ORDER_CLOSE_BY",
            "ticket": ticket,
            "opposite": opposite,
            "allow_color": allow_color
        })
        res = self.client.send_message(data)
        return res

    def OrderModify(
        self,
        ticket: int,
        price: float,
        stoploss: float,
        takeprofit: float,
        expiration: datetime,
        allow_color: str
    ):
        data = json.dumps({
            "type": "ORDER_MODIFY",
            "ticket": ticket,
            "price": price,
            "stoploss": stoploss,
            "takeprofit": takeprofit,
            "expiration": expiration,
            "allow_color": allow_color
        })
        res = self.client.send_message(data)
        return res
        
    def OrderDelete(
        self,
        ticket: int,
        allow_color: str
    ):
        data = json.dumps({
            "type": "ORDER_DELETE",
            "ticket": ticket,
            "allow_color": allow_color
        })
        res = self.client.send_message(data)
        return res