import json
from datetime import datetime, timedelta
from dateutil import parser
import time
import pytz
import csv
import os
import fasteners
import numpy as np
import pandas as pd
from copy import deepcopy

def find_peak_demand(start_datetime, end_datetime, window_length_minutes):
    """
	Input:
	:start_datetime: ISOFormat datetime of period start
	:end_datetime: ISOFormat datetime of period end
	:window_type: String, either 'rolling' or 'time-based' to specify calculation method
	:window_length_minutes: Integer, number of minutes in a window

	Returns:
	dictionary with keys 'peak_demand' and 'start_datetime'
	:peak_demand: Integer, kW_demand of highest window
	:start_datetime: ISOFormat datetime of window start
    """
    demand = {'peak_demand':[], 'start_datetime_window':[]}
    dstart_datetime = parser.parse(start_datetime)
    dend_datetime = parser.parse(end_datetime)


    demand['start_datetime_window'].append((dstart_datetime + timedelta(minutes=window_length_minutes)).isoformat())
    return demand
print(find_peak_demand('2021-09-01T08:00', '2021-09-01T09:00', 15))
