from my_netatmo import services, xbarmenu

MEASURES_TRENDS = {'down': '↓', 'up': '↑'}


def display_leader_measures(data: dict, menu: xbarmenu.Menu):
    temp = data['Temperature']
    temp_trend = MEASURES_TRENDS.get(data['temp_trend'], '')
    temp_display = f'{temp}º {temp_trend}'.strip()
    menu.add_item(temp_display)

    menu.add_sep()

    last_update = services.timestamp_to_hour(data['time_utc'])
    last_update_display = f'Last update: {last_update}h'
    menu.add_item(last_update_display)


def display_outdoor_measures(data: dict, menu: xbarmenu.Menu):
    temp = data['Temperature']
    temp_trend = MEASURES_TRENDS.get(data['temp_trend'], '')
    temp_display = f'{temp}º {temp_trend}'.strip()
    menu.add_item(temp_display)

    humidity = data['Humidity']
    humidity_display = f'H: {humidity}%'
    menu.add_item(humidity_display)

    when_min_temp = services.timestamp_to_hour(data['date_min_temp'])
    min_temp = data['min_temp']
    min_temp_display = f'↓ {min_temp}º ({when_min_temp}h)'
    menu.add_item(min_temp_display)

    when_max_temp = services.timestamp_to_hour(data['date_max_temp'])
    max_temp = data['max_temp']
    max_temp_display = f'↑ {max_temp}º ({when_max_temp}h)'
    menu.add_item(max_temp_display)


def display_indoor_measures(data: dict, menu: xbarmenu.Menu):
    temp = data['Temperature']
    temp_trend = MEASURES_TRENDS.get(data['temp_trend'], '')
    temp_display = f'{temp}º {temp_trend}'.strip()
    menu.add_item(temp_display)

    humidity = data['Humidity']
    humidity_display = f'H: {humidity}%'
    menu.add_item(humidity_display)

    co2 = data['CO2']
    co2_display = f'CO₂: {co2}ppm'
    menu.add_item(co2_display)

    pressure = data['Pressure']
    pressure_trend = MEASURES_TRENDS.get(data['pressure_trend'], '')
    pressure_display = f'P: {pressure}mbar {pressure_trend}'.strip()
    menu.add_item(pressure_display)

    noise = data['Noise']
    noise_display = f'N: {noise}dB'
    menu.add_item(noise_display)

    when_min_temp = services.timestamp_to_hour(data['date_min_temp'])
    min_temp = data['min_temp']
    min_temp_display = f'↓ {min_temp}º ({when_min_temp}h)'
    menu.add_item(min_temp_display)

    when_max_temp = services.timestamp_to_hour(data['date_max_temp'])
    max_temp = data['max_temp']
    max_temp_display = f'↑ {max_temp}º ({when_max_temp}h)'
    menu.add_item(max_temp_display)


menu = xbarmenu.Menu()
outdoor_data = services.get_outdoor_measures()
indoor_data = services.get_indoor_measures()

display_leader_measures(outdoor_data, menu)

outdoor_menu = menu.add_item('☁️ Outdoor')
display_outdoor_measures(outdoor_data, outdoor_menu)

indoor_menu = menu.add_item('🏠 Indoor')
display_indoor_measures(indoor_data, indoor_menu)

print(menu)
