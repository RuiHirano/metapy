from pydantic import BaseModel
from datetime import datetime
from enum import Enum, IntEnum

class Tick(BaseModel):
    time: datetime
    bid: float
    ask: float
    last: float
    volume: int
    time_msc: int
    flags: int
    volume_real: float

class Rate(BaseModel):
    time: datetime
    open: float
    high: float
    low: float
    close: float
    tick_volume: int
    spread: int
    real_volume: int

class Response(BaseModel):
    action: str
    data: str
    error: str

class ENUM_ORDER_TYPE(int, Enum):
    ORDER_TYPE_BUY = 0
    ORDER_TYPE_SELL = 1
    ORDER_TYPE_BUY_LIMIT = 2
    ORDER_TYPE_SELL_LIMIT = 3
    ORDER_TYPE_BUY_STOP = 4
    ORDER_TYPE_SELL_STOP = 5

class ENUM_ORDER_TYPE_TIME(str, Enum):
    ORDER_TIME_GTC = "ORDER_TIME_GTC"
    ORDER_TIME_DAY = "ORDER_TIME_DAY"
    ORDER_TIME_SPECIFIED = "ORDER_TIME_SPECIFIED"
    ORDER_TIME_SPECIFIED_DAY = "ORDER_TIME_SPECIFIED_DAY"

class ENUM_TRADE_REQUEST_ACTIONS(str, Enum):
    TRADE_ACTION_DEAL="TRADE_ACTION_DEAL"
    TRADE_ACTION_PENDING="TRADE_ACTION_PENDING"
    TRADE_ACTION_SLTP="TRADE_ACTION_SLTP"
    TRADE_ACTION_MODIFY="TRADE_ACTION_MODIFY"
    TRADE_ACTION_REMOVE="TRADE_ACTION_REMOVE"
    TRADE_ACTION_CLOSE_BY="TRADE_ACTION_CLOSE_BY"

class ENUM_ORDER_TYPE_FILLING(str, Enum):
    ORDER_FILLING_FOK="ORDER_FILLING_FOK"
    ORDER_FILLING_IOC="ORDER_FILLING_IOC"
    ORDER_FILLING_RETURN="ORDER_FILLING_RETURN"

class ENUM_TIMEFRAME(str, Enum):
    PERIOD_CURRENT=0
    PERIOD_M1=1
    PERIOD_M5=5
    PERIOD_M15=15
    PERIOD_M30=30
    PERIOD_H1=60
    PERIOD_H4=240
    PERIOD_D1=1440
    PERIOD_W1=10080
    PERIOD_MN1=43200
