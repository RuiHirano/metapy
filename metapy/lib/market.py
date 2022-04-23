
from datetime import datetime
from pydantic import BaseModel
from enum import Enum
from lib.type import ENUM_TIMEFRAME
import json

class ENUM_MARKET_ACTION(str, Enum):
    MARKET_ACTION_SYMBOL_EXIST = "MARKET_ACTION_SYMBOL_EXIST"

class MessageModel(BaseModel):
    action: ENUM_MARKET_ACTION
    data: dict

class Market:
    def __init__(self, api):
        self.api = api

    def SymbolExist(
        self, 
    ):
        data = json.dumps(MessageModel(
            action=ENUM_MARKET_ACTION.MARKET_ACTION_SYMBOL_EXIST,
            data={}
        ).dict())
        res = self.api.send_message(data)
        return res
