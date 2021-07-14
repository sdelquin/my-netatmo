from my_netatmo import services

MEASURES_TRENDS = {'down': '↓', 'stable': '•', 'up': '↑'}

data = services.get_outdoor_measures()
temp = data['Temperature']
temp_trend = MEASURES_TRENDS.get(data['temp_trend'])
print(f'{temp}º {temp_trend}')
