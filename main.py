from http import HTTPStatus
import requests

response = requests.get('https://twitter.com')

if response.status_code == 200:
    print('Everythink is OK')

if response.status_code == HTTPStatus.OK:
    print('Everythink is OK')
