
from datetime import datetime
import json
from pydantic import BaseModel
from enum import Enum

class ENUM_ACCOUNT_ACTION(int, Enum):
    ACCOUNT_ACTION_BALANCE = 0
    ACCOUNT_ACTION_CREDIT = 1
    ACCOUNT_ACTION_CURRENCY = 2
    ACCOUNT_ACTION_EQUITY = 3

class MessageModel(BaseModel):
    action: ENUM_ACCOUNT_ACTION
    data: dict
    
class Account:
    def __init__(self, client):
        self.client = client

    def AccountBalance(
        self, 
    ):
        data = json.dumps(MessageModel(
            action=ENUM_ACCOUNT_ACTION.ACCOUNT_ACTION_BALANCE,
            data={}
        ).dict())
        res = self.client.send_message(data)
        return res

    def AccountCredit(
        self, 
    ):
        data = json.dumps(MessageModel(
            action=ENUM_ACCOUNT_ACTION.ACCOUNT_ACTION_CREDIT,
            data={}
        ).dict())
        res = self.client.send_message(data)
        return res

    def AccountCurrency(
        self, 
    ):
        data = json.dumps(MessageModel(
            action=ENUM_ACCOUNT_ACTION.ACCOUNT_ACTION_CURRENCY,
            data={}
        ).dict())
        res = self.client.send_message(data)
        return res

    def AccountEquity(
        self, 
    ):
        data = json.dumps(MessageModel(
            action=ENUM_ACCOUNT_ACTION.ACCOUNT_ACTION_EQUITY,
            data={}
        ).dict())
        res = self.client.send_message(data)
        return res