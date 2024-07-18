
def kapsalonService():
    from kapsalon_web_service import KapsalonWebService as kws
    json = kws.retrieveKapsalonDataAsJson()
    selectedDishes = kws.retrieveKapsalonProperties(json)
    filtered_dishes = KapsalonWebService.filterDishes(selected_dishes)
    kws.insert_data_into_database(filtered_dishes)
    
kapsalonService()