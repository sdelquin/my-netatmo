from my_netatmo import services, xbarmenu

menu = xbarmenu.Menu()
try:
    outdoor_data = services.get_outdoor_measures()
    indoor_data = services.get_indoor_measures()
except Exception as err:
    menu.add_item('⚠️ NA')
    menu.add_item(str(err))
else:
    services.display_leader_measures(outdoor_data, indoor_data, menu)

    outdoor_menu = menu.add_item('☁️ Outdoor')
    services.display_outdoor_measures(outdoor_data, outdoor_menu)

    indoor_menu = menu.add_item('🏠 Indoor')
    services.display_indoor_measures(indoor_data, indoor_menu)

    menu.add_item('🌐 Netatmo dashboard', href='https://my.netatmo.com/app/station')

print(menu)
