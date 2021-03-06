
from datetime import datetime
import json
from lib.type import ENUM_ORDER_TYPE
from pydantic import BaseModel
from enum import Enum
from lib.logger import log

class ENUM_ORDER_ACTION(int, Enum):
    ORDER_ACTION_SEND = 0
    ORDER_ACTION_CLOSE = 1
    ORDER_ACTION_MODIFY = 2
    ORDER_ACTION_DELETE = 3

class MessageModel(BaseModel):
    action: ENUM_ORDER_ACTION
    data: dict

class OrderSendModel(BaseModel):
    symbol: str 
    type: ENUM_ORDER_TYPE
    volume: float
    price: float
    slippage: int
    stoploss: float
    takeprofit: float
    comment: str = None
    magic: int = 0
    expiration: int = 0

class OrderCloseModel(BaseModel):
    ticket: int
    volume: float
    price: float
    slippage: int

class OrderModifyModel(BaseModel):
    ticket: int
    price: float
    stoploss: float
    takeprofit: float
    expiration: int = 0

class OrderDeleteModel(BaseModel):
    ticket: int

class Order:
    def __init__(self, client):
        self.client = client

    def OrderSend(
        self, 
        symbol: str, 
        type: ENUM_ORDER_TYPE,
        volume: float,
        price: float,
        slippage: int,
        stoploss: float,
        takeprofit: float,
        comment: str = None,
        magic: int = 0,
        expiration: int = 0,
    ):
        order_send = OrderSendModel(
            symbol=symbol,
            type=type,
            volume=volume,
            price=price,
            slippage=slippage,
            stoploss=stoploss,
            takeprofit=takeprofit,
            comment=comment,
            magic=magic,
            expiration=expiration
        )
        
        data = json.dumps(MessageModel(
            action=ENUM_ORDER_ACTION.ORDER_ACTION_SEND,
            data=order_send.dict()
        ).dict())
        res = self.client.send_message(data)
        ticket = res["data"]["ticket"]
        if ticket == -1:
            log.error("OrderSend is failed")
        else:
            log.info("OrderSend is success")
        return ticket

    def OrderClose(
        self,
        ticket: int,
        volume: float,
        price: float,
        slippage: int
    ):
        order_close = OrderCloseModel(
            ticket=ticket,
            volume=volume,
            price=price,
            slippage=slippage,
        )

        data = json.dumps(MessageModel(
            action=ENUM_ORDER_ACTION.ORDER_ACTION_CLOSE,
            data=order_close.dict()
        ).dict())
        
        res = self.client.send_message(data)
        closed = res["data"]["closed"]
        if closed:
            log.error("OrderClose is failed")
        else:
            log.info("OrderClose is success")
        return closed

    def OrderModify(
        self,
        ticket: int,
        price: float,
        stoploss: float,
        takeprofit: float,
        expiration: int = 0,
    ):
        order_modify = OrderModifyModel(
            ticket=ticket,
            price=price,
            stoploss=stoploss,
            takeprofit=takeprofit,
            expiration=expiration,
        )

        data = json.dumps(MessageModel(
            action=ENUM_ORDER_ACTION.ORDER_ACTION_MODIFY,
            data=order_modify.dict()
        ).dict())
        res = self.client.send_message(data)
        modified = res["data"]["modified"]
        if modified:
            log.error("OrderModified is failed")
        else:
            log.info("OrderModified is success")
        return modified
        
    def OrderDelete(
        self,
        ticket: int,
    ):
        order_delete = OrderDeleteModel(
            ticket=ticket,
        )

        data = json.dumps(MessageModel(
            action=ENUM_ORDER_ACTION.ORDER_ACTION_DELETE,
            data=order_delete.dict()
        ).dict())
        res = self.client.send_message(data)
        deleted = res["data"]["deleted"]
        if deleted:
            log.error("OrderDelete is failed")
        else:
            log.info("OrderDelete is success")
        return deleted