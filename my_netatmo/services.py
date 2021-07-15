from datetime import datetime
from functools import partial

import netatmo


def get_measures(device: str):
    ws = netatmo.WeatherStation()
    ws.get_data()
    response = ws.station_by_name()
    if device == 'INDOOR':
        data = response['dashboard_data']
    elif device == 'OUTDOOR':
        data = response['modules'][0]['dashboard_data']
    return data


get_indoor_measures = partial(get_measures, device='INDOOR')
get_outdoor_measures = partial(get_measures, device='OUTDOOR')


def timestamp_to_hour(timestamp: int):
    return datetime.fromtimestamp(timestamp).strftime('%H:%M')
