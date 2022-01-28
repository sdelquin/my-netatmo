from datetime import datetime
from functools import partial

import netatmo

from my_netatmo import xbarmenu

MEASURES_TRENDS = {'down': '↓', 'up': '↑'}


def get_measures(device: str):
    ws = netatmo.WeatherStation()
    ws.get_data()
    response = ws.station_by_name()
    if device == 'INDOOR':
        data = response.get('dashboard_data', 'NA')
    elif device == 'OUTDOOR':
        data = response['modules'][0].get('dashboard_data', 'NA')
    return data


get_indoor_measures = partial(get_measures, device='INDOOR')
get_outdoor_measures = partial(get_measures, device='OUTDOOR')


def timestamp_to_hour(timestamp: int):
    return datetime.fromtimestamp(timestamp).strftime('%H:%M')


def display_leader_measures(outdoor_data: dict, indoor_data: dict, menu: xbarmenu.Menu):
    outdoor_temp = outdoor_data.get('Temperature', 'NA')
    indoor_temp = indoor_data.get('Temperature', 'NA')
    temp_diff = 'up' if outdoor_temp - indoor_temp > 0 else 'down'
    temp_diff = MEASURES_TRENDS.get(temp_diff, '')
    temp_display = f'{outdoor_temp}º {temp_diff}'.strip()
    menu.add_item(temp_display)

    menu.add_sep()

    try:
        last_update = timestamp_to_hour(outdoor_data['time_utc'])
        last_update += 'h'
    except KeyError:
        last_update = 'NA'
    last_update_display = f'Last update: {last_update}'
    menu.add_item(last_update_display)


def display_outdoor_measures(data: dict, menu: xbarmenu.Menu):
    temp = data.get('Temperature', 'NA')
    temp_trend = MEASURES_TRENDS.get(data.get('temp_trend', 'NA'), '')
    temp_display = f'{temp}º {temp_trend}'.strip()
    menu.add_item(temp_display)

    humidity = data.get('Humidity', 'NA')
    humidity_display = f'H: {humidity}%'
    menu.add_item(humidity_display)

    try:
        when_min_temp = timestamp_to_hour(data['date_min_temp'])
        when_min_temp += 'h'
    except KeyError:
        when_min_temp = 'NA'
    min_temp = data.get('min_temp', 'NA')
    min_temp_display = f'↓ {min_temp}º ({when_min_temp})'
    menu.add_item(min_temp_display)

    try:
        when_max_temp = timestamp_to_hour(data['date_max_temp'])
        when_max_temp += 'h'
    except KeyError:
        when_max_temp = 'NA'
    max_temp = data.get('max_temp', 'NA')
    max_temp_display = f'↑ {max_temp}º ({when_max_temp})'
    menu.add_item(max_temp_display)


def display_indoor_measures(data: dict, menu: xbarmenu.Menu):
    temp = data.get('Temperature', 'NA')
    temp_trend = MEASURES_TRENDS.get(data.get('temp_trend', 'NA'), '')
    temp_display = f'{temp}º {temp_trend}'.strip()
    menu.add_item(temp_display)

    humidity = data.get('Humidity', 'NA')
    humidity_display = f'H: {humidity}%'
    menu.add_item(humidity_display)

    co2 = data.get('CO2', 'NA')
    co2_display = f'CO₂: {co2}ppm'
    menu.add_item(co2_display)

    pressure = data.get('Pressure', 'NA')
    pressure_trend = MEASURES_TRENDS.get(data.get('pressure_trend', 'NA'), '')
    pressure_display = f'P: {pressure}mbar {pressure_trend}'.strip()
    menu.add_item(pressure_display)

    noise = data.get('Noise', 'NA')
    noise_display = f'N: {noise}dB'
    menu.add_item(noise_display)

    try:
        when_min_temp = timestamp_to_hour(data['date_min_temp'])
        when_min_temp += 'h'
    except KeyError:
        when_min_temp = 'NA'
    min_temp = data.get('min_temp', 'NA')
    min_temp_display = f'↓ {min_temp}º ({when_min_temp}h)'
    menu.add_item(min_temp_display)

    try:
        when_max_temp = timestamp_to_hour(data['date_max_temp'])
        when_max_temp += 'h'
    except KeyError:
        when_max_temp = 'NA'
    max_temp = data.get('max_temp', 'NA')
    max_temp_display = f'↑ {max_temp}º ({when_max_temp}h)'
    menu.add_item(max_temp_display)
