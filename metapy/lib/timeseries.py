
from datetime import datetime
from pydantic import BaseModel
from enum import Enum
from lib.type import ENUM_TIMEFRAME
import json

class ENUM_TIMESERIES_ACTION(int, Enum):
    TIMESERIES_ACTION_GET_N_RATES_BY_START_POSITION = 0
    TIMESERIES_ACTION_GET_N_RATES_BY_START_TIME = 1
    TIMESERIES_ACTION_GET_RATES_BY_TIME_INTERVAL = 2

class MessageModel(BaseModel):
    action: ENUM_TIMESERIES_ACTION
    data: dict

class GetNRatesByStartPositionModel(BaseModel):
    symbol: str 
    timeframe: ENUM_TIMEFRAME
    start_pos: int
    count: int

class GetNRatesByStartTimeModel(BaseModel):
    symbol: str 
    timeframe: ENUM_TIMEFRAME
    start_time: datetime
    count: int  

class GetRatesByTimeIntervalModel(BaseModel):
    symbol: str 
    timeframe: ENUM_TIMEFRAME
    start_time: datetime
    stop_time: datetime

class Timeseries:
    def __init__(self, client):
        self.client = client

    def GetNRatesByStartPosition(
        self, 
        symbol: str,
        timeframe: ENUM_TIMEFRAME,
        start_pos: int,
        count: int,
    ):
        get_rates = GetNRatesByStartPositionModel(
            symbol=symbol,
            timeframe=timeframe,
            start_pos=start_pos,
            count=count,
        )
        data = json.dumps(MessageModel(
            action=ENUM_TIMESERIES_ACTION.TIMESERIES_ACTION_GET_N_RATES_BY_START_POSITION,
            data=get_rates.dict()
        ).dict())
        res = self.client.send_message(data)
        return res

    def GetNRatesByStartTime(
        self, 
        symbol: str,
        timeframe: ENUM_TIMEFRAME,
        start_time: datetime,
        count: int,
    ):
        get_rates = GetNRatesByStartTimeModel(
            symbol=symbol,
            timeframe=timeframe,
            start_time=start_time,
            count=count,
        )
        data = json.dumps(MessageModel(
            action=ENUM_TIMESERIES_ACTION.TIMESERIES_ACTION_GET_N_RATES_BY_START_TIME,
            data=get_rates.dict()
        ).dict())
        res = self.client.send_message(data)
        return res

    def GetRatesByTimeInterval(
        self, 
        symbol: str,
        timeframe: ENUM_TIMEFRAME,
        start_time: datetime,
        stop_time: datetime,
    ):
        get_rates = GetRatesByTimeIntervalModel(
            symbol=symbol,
            timeframe=timeframe,
            start_time=start_time,
            stop_time=stop_time,
        )
        data = json.dumps(MessageModel(
            action=ENUM_TIMESERIES_ACTION.TIMESERIES_ACTION_GET_RATES_BY_TIME_INTERVAL,
            data=get_rates.dict()
        ).dict())
        res = self.client.send_message(data)
        return res
