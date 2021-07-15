from my_netatmo import services, xbarmenu

menu = xbarmenu.Menu()
outdoor_data = services.get_outdoor_measures()
indoor_data = services.get_indoor_measures()

services.display_leader_measures(outdoor_data, menu)

outdoor_menu = menu.add_item('☁️ Outdoor')
services.display_outdoor_measures(outdoor_data, outdoor_menu)

indoor_menu = menu.add_item('🏠 Indoor')
services.display_indoor_measures(indoor_data, indoor_menu)

menu.add_item('🌐 Netatmo dashboard', href='https://my.netatmo.com/app/station')

print(menu)
