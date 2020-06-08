import requests
import json

# URL:
URL = 'https://swapi.dev/api/'

# Item 'luke':
luke = 'people/1'

item = URL + luke

# get the request:
content = requests.get(item)

# load the info into a variable:
info = json.loads(content.text)

# Write the JSON file:
with open('mijson.json', 'w') as f:
    f.write(json.dumps(info, indent=4))
