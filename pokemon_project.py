import pandas as pd
import numpy as np
import requests
import json

# Reading from API
response = requests.get("https://pokeapi.co/api/v2/generation/1/")
# Checking the status of API - Turned out to be 200 which means everything went okay
print(response.status_code)
# Using response.json() method to see the data we received back from the API
print(response.json())

# Extracting 151 pokemon URLs
pokemon_species = response.json()['pokemon_species']
pokemon_url = []
for i in pokemon_species:
    pokemon_url.append(i['url'])
pokemon_url

# Looping multiple URLs and save their information in a list
url_information = []
for url in pokemon_url:
    resp = requests.get(url)
    url_information.append(resp.json())

for i in url_information[0]:
    print(i)

# Testing first URL - extracting information I want
information = ['capture_rate', 'evolves_from_species', 'growth_rate', 'habitat', 'name', 'shape']
information_list = []
for each_pokemon in url_information:
    for each_info in each_pokemon:
        for info in information:
            if each_info == info:
                information_list.append([each_info, each_pokemon[each_info]])
information_list

