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
