import requests
import json

url ="http://127.0.0.1:8000/car/list/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print(data['cars'][1]['model'])

else:
    print('Error')
