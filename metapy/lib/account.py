
from datetime import datetime
import json
from pydantic import BaseModel
from enum import Enum

class ENUM_ACCOUNT_ACTION(str, Enum):
    ACCOUNT_ACTION_BALANCE = "ACCOUNT_ACTION_BALANCE"
    ACCOUNT_ACTION_CREDIT = "ACCOUNT_ACTION_CREDIT"
    ACCOUNT_ACTION_CURRENCY = "ACCOUNT_ACTION_CURRENCY"
    ACCOUNT_ACTION_EQUITY = "ACCOUNT_ACTION_EQUITY"

class MessageModel(BaseModel):
    action: ENUM_ACCOUNT_ACTION
    data: dict
    
class Account:
    def __init__(self, api):
        self.api = api

    def AccountBalance(
        self, 
    ):
        data = json.dumps(MessageModel(
            action=ENUM_ACCOUNT_ACTION.ACCOUNT_ACTION_BALANCE,
            data={}
        ).dict())
        res = self.api.send_message(data)
        return res

    def AccountCredit(
        self, 
    ):
        data = json.dumps(MessageModel(
            action=ENUM_ACCOUNT_ACTION.ACCOUNT_ACTION_CREDIT,
            data={}
        ).dict())
        res = self.api.send_message(data)
        return res

    def AccountCurrency(
        self, 
    ):
        data = json.dumps(MessageModel(
            action=ENUM_ACCOUNT_ACTION.ACCOUNT_ACTION_CURRENCY,
            data={}
        ).dict())
        res = self.api.send_message(data)
        return res

    def AccountEquity(
        self, 
    ):
        data = json.dumps(MessageModel(
            action=ENUM_ACCOUNT_ACTION.ACCOUNT_ACTION_EQUITY,
            data={}
        ).dict())
        res = self.api.send_message(data)
        return res
