
from datetime import datetime
from pydantic import BaseModel
from enum import Enum
from lib.type import ENUM_TIMEFRAME
import pandas as pd
import json

class ENUM_TIMESERIES_ACTION(str, Enum):
    TIMESERIES_ACTION_GET_N_RATES_BY_START_POSITION = "TIMESERIES_ACTION_GET_N_RATES_BY_START_POSITION"
    TIMESERIES_ACTION_GET_N_RATES_BY_START_TIME = "TIMESERIES_ACTION_GET_N_RATES_BY_START_TIME"
    TIMESERIES_ACTION_GET_RATES_BY_TIME_INTERVAL = "TIMESERIES_ACTION_GET_RATES_BY_TIME_INTERVAL"

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
    def __init__(self, api):
        self.api = api

    def GetNRatesByStartPosition(
        self, 
        symbol: str,
        timeframe: ENUM_TIMEFRAME,
        start_pos: int,
        count: int,
        dataframe=True,
    ):
        get_rates = GetNRatesByStartPositionModel(
            symbol=symbol,
            timeframe=timeframe,
            start_pos=start_pos,
            count=count,
        )
        rates = self.api.send_message(action=ENUM_TIMESERIES_ACTION.TIMESERIES_ACTION_GET_N_RATES_BY_START_POSITION, data=get_rates.dict())
        if dataframe:
            rates = pd.DataFrame.from_records(rates)
        return rates

    def GetNRatesByStartTime(
        self, 
        symbol: str,
        timeframe: ENUM_TIMEFRAME,
        start_time: datetime,
        count: int,
        dataframe=True,
    ):
        get_rates = GetNRatesByStartTimeModel(
            symbol=symbol,
            timeframe=timeframe,
            start_time=start_time,
            count=count,
        )
        rates = self.api.send_message(action=ENUM_TIMESERIES_ACTION.TIMESERIES_ACTION_GET_N_RATES_BY_START_TIME, data=get_rates.dict())
        if dataframe:
            df = pd.DataFrame.from_records(rates)
            print(df)
        return rates

    def GetRatesByTimeInterval(
        self, 
        symbol: str,
        timeframe: ENUM_TIMEFRAME,
        start_time: datetime,
        stop_time: datetime,
        dataframe=True,
    ):
        get_rates = GetRatesByTimeIntervalModel(
            symbol=symbol,
            timeframe=timeframe,
            start_time=start_time,
            stop_time=stop_time,
        )
        rates = self.api.send_message(action=ENUM_TIMESERIES_ACTION.TIMESERIES_ACTION_GET_RATES_BY_TIME_INTERVAL, data=get_rates.dict())
        if dataframe:
            df = pd.DataFrame.from_records(rates)
            print(df)
        return rates
