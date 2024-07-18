
def kapsalonService():
    from kapsalon_web_service import KapsalonWebService as kws
    json = kws.retrieveKapsalonDataAsJson()
    selectedDishes = kws.retrieveKapsalonProperties(json)
    kws.filterDishes(selectedDishes)
    

kapsalonService()