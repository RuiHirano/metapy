
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
        balance = self.api.send_message(action=ENUM_ACCOUNT_ACTION.ACCOUNT_ACTION_BALANCE, data=None)
        return balance

    def AccountCredit(
        self, 
    ):
        credit = self.api.send_message(action=ENUM_ACCOUNT_ACTION.ACCOUNT_ACTION_CREDIT, data=None)
        return credit

    def AccountCurrency(
        self, 
    ):
        currency = self.api.send_message(action=ENUM_ACCOUNT_ACTION.ACCOUNT_ACTION_CURRENCY, data=None)
        return currency

    def AccountEquity(
        self, 
    ):
        equity = self.api.send_message(action=ENUM_ACCOUNT_ACTION.ACCOUNT_ACTION_EQUITY, data=None)
        return equity
