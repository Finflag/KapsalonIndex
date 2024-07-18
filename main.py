
def kapsalonService():
    from kapsalon_web_service import KapsalonWebService as kws
    json = kws.retrieveKapsalonDataAsJson()
    selectedDishes = kws.retrieveKapsalonProperties(json)
    filtered_dishes = kws.filterDishes(selectedDishes)
    kws.insert_data_into_database(filtered_dishes)
    
kapsalonService()