import requests
from pprint import pprint

with open("api.key", 'r') as api_file:
    api_key = api_file.readline().strip()
    print(f'api key: {api_key}')
    # get the full list of exchange rates with USD as the base value
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'

    # make the request
    response = requests.get(url)
    data = response.json()

    pprint(data)
