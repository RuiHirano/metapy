
from datetime import datetime
from pydantic import BaseModel
from enum import Enum
from lib.type import ENUM_TIMEFRAME
import json

class ENUM_MARKET_ACTION(int, Enum):
    MARKET_ACTION_SYMBOL_EXIST = 0

class MessageModel(BaseModel):
    action: ENUM_MARKET_ACTION
    data: dict

class Market:
    def __init__(self, client):
        self.client = client

    def SymbolExist(
        self, 
    ):
        data = json.dumps(MessageModel(
            action=ENUM_MARKET_ACTION.MARKET_ACTION_SYMBOL_EXIST,
            data={}
        ).dict())
        res = self.client.send_message(data)
        return res
