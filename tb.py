import requests
import pandas as pd

# API-endpoint
api_url = "https://cw-api.takeaway.com/api/v34/restaurants/search"

# Queryparameters
params = {
    "searchString": "kapsalon",
    "postalCode": "1093",
    "sortBy": "bestMatch",
    "orderBy": "asc",
    "page": "1",
    "limit": "50000",
    "select": "dishes"
}

# Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "nl",
    "Referer": "https://www.thuisbezorgd.nl/",
    "X-Language-Code": "nl",
    "X-Country-Code": "nl"
}

# Een GET-verzoek sturen om JSON-data op te halen
response = requests.get(api_url, headers=headers, params=params)

# Controleren of het verzoek succesvol was
if response.status_code == 200:
    data = response.json()

    # Bekijken van de opgehaalde JSON-data
    #print(data)

    # Laten we enkele objecten uit de JSON-data halen
    # We gaan de 'dishes' extraheren

    dishes = data.get('dishes', [])

    # Lijst van dictionaries omzetten naar een pandas DataFrame
    dishes_df = pd.DataFrame(dishes)

    # Bekijken van de eerste paar rijen van de DataFrame
    #print(dishes_df.head())

    # Specifieke kolommen extraheren (bijvoorbeeld 'name' en 'price')
    dishes_selected = dishes_df[['name', 'price', 'restaurant']]

    # Filteren van gerechten op basis van cuisineType "kapsalon_1694"
    #filtered_dishes = dishes_selected[dishes_selected['restaurant'].apply(lambda x: 'kapsalon_1694' in x['cuisineTypes'])]

    # Uitsluiten van gerechten die de woorden 'vegetarisch' of 'vega' bevatten
    excluded_terms = "vegetarisch|vega|pizza|Broodje|kip|falafel|piri piri|en extra vlees|menu|zonder kaas|Ben & Jerry's|frisdrank|Veggie"
    #filtered_dishes = filtered_dishes[~filtered_dishes['name'].str.contains(excluded_terms, case=False, na=False)]
    filtered_dishes = dishes_selected[~dishes_selected['name'].str.contains(excluded_terms, case=False, na=False)]


    # Filteren van gerechten die het woord 'döner' bevatten
    included_terms = "döner"
    filtered_dishes = filtered_dishes[filtered_dishes['name'].str.contains(included_terms, case=False, na=False)]

    # Extracting the city from the location and adding it to the final output
    filtered_dishes['city'] = filtered_dishes['restaurant'].apply(lambda x: x['location']['city'])

    out = filtered_dishes[['name', 'price', 'city']]

    # Bekijken van de gesorteerde en gefilterde kolommen
    print(out)

else:
    print(f"Request failed with status code {response.status_code}")