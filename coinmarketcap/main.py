from optparse import Values
from requests import Session
from json import loads, dump

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}

header = {
    'Accept': 'application/json',
    'X-CMC_PRO_API_KEY': '4b406c86-4328-4c80-8708-ffe3c55259cf'
}

def response():

    r = Session()
    r.headers.update(header)
    return r.get(url, params=parameters)

def handle_data():

    data = loads(response().text)

    with open('json_data.json', 'w') as json_data:
        dump(data, json_data)

    return data
    
print(handle_data()['data'])







