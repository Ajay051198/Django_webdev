import requests
Debug = False
key = 'Message for key'


def search_item(item):
    params = {'api_key': key}
    data = {'generalSearchInput': item}
    response = requests.post(
        r'https://api.nal.usda.gov/fdc/v1/search',
        params=params,
        json=data
    )

    try:
        name = response.json()['foods'][0]['description']
        data_db = []

        for data in response.json()['foods'][0]['foodNutrients']:
            entry = dict()
            entry['Nutrient'] = data['nutrientName']
            entry['Unit'] = data['unitName']
            entry['Value'] = data['value']
            data_db.append(entry)

        context = {'name': name,
                   'data_db': data_db}

    except:
        context = {'name': 'Item not found in the database',
                   'data_db': None}

    return context


if Debug:
    print(search_item('rice'))
