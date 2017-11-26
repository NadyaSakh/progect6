"""
Геолокация космической станции, широта и долгота.
"""

import urllib.request
import json

response = urllib.request.urlopen("http://api.open-notify.org/iss-now.json")

obj = json.loads(response.read().decode())
print(obj)
print("longitude = ", obj['iss_position']['longitude'])
print("latitude = ",obj['iss_position']['latitude'])
#{'timestamp': 1511595604, 'message': 'success', 'iss_position': {'latitude': '51.4139', 'longitude': '-127.4700'}}