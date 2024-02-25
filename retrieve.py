import requests
import csv
import json

# failure data
def failure():
    url = "https://banks.data.fdic.gov/api/failures"


    response = requests.get(url)
    json_data = response.json()

    fields = list(json_data['data'][0]['data'].keys()) 

    with open('output.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for item in json_data['data']:
            writer.writerow(item['data'])

# summary of deposits data
def sod():
    url = "https://banks.data.fdic.gov/api/sod"

    params = {
        'limit': 10000,
        'fields' : 'CERT,YEAR,ASSET,DEPSUMBR,STALPBR',
        'sort_by' : 'YEAR',
    }

    response = requests.get(url, params=params)
    json_data = response.json()
     
    # with open('sod.json', 'w') as file:
    #     json.dump(json_data, file)
    
    fields = list(json_data['data'][0]['data'].keys()) 

    with open('sod.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for item in json_data['data']:
            writer.writerow(item['data'])

sod()
# failure()