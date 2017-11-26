"""

Покемоны! Вывести номер покемона и его способности
"""

import urllib.request
import json

total_number = 803
k = 1
url = "http://pokeapi.co/api/v2/pokemon/"
while k < total_number:
    newurl = url + str(k) + '/'
    rq = urllib.request.Request(newurl, headers={'User-Agent': 'Yandex/17.10.0.2017'})
    response = urllib.request.urlopen(rq)
    pokemon = json.loads(response.read().decode())
    print('Pokemon №: ',pokemon['id'])
    print('Pokemon name: ',pokemon['name'])
    print('Pokemon ability: ',pokemon['abilities'][0]['ability']['name'])
    k += 1
