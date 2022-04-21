
from datetime import datetime
import json


class Account:
    def __init__(self, client):
        self.client = client

    def AccountInfoInteger(
        self, 
        property_id: int
    ):
        data = json.dumps({
            "type": "ACCOUNT_INFO_INTEGER",
            "property_id": property_id
        })
        res = self.client.send_message(data)
        return res

    def AccountBalance(
        self, 
    ):
        data = json.dumps({
            "type": "ACCOUNT_BALANCE",
        })
        res = self.client.send_message(data)
        return res

    def AccountCredit(
        self, 
    ):
        data = json.dumps({
            "type": "ACCOUNT_CREDIT",
        })
        res = self.client.send_message(data)
        return res