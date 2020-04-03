from bs4 import BeautifulSoup
import requests
key = 'DUVrhfkiQygwj18fesQvdwpgbPbrAjP1QDfD9lgt'
params = {'api_key': key}
data = {'generalSearchInput': 'brown rice'}
response = requests.post(
    r'https://api.nal.usda.gov/fdc/v1/search',
    params=params,
    json=data
)
name = response.json()['foods'][0]['description']
data_db = []
entry = dict()
for data in response.json()['foods'][0]['foodNutrients']:
    entry['Nutrient'] = data['nutrientName']
    entry['Unit'] = data['unitName']
    entry['Value'] = data['value']
    data_db.append(entry)

context = {'name': name,
           'data_db': data_db}
print(context)

