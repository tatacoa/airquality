# API data

from pprint import pprint
import pandas as pd
import requests

#resp = requests.get('https://api.waqi.info/search/?keyword=bogota&token=aa51ef4782205d1fadf8d5151cf29c235a707c98')
resp = requests.get('https://api.waqi.info/feed/colombia/bogota/usaquen/?token=aa51ef4782205d1fadf8d5151cf29c235a707c98')
#pprint(resp.json())

data = resp.json()
values = data['data']['iaqi']
valdate = data['data']['time']['s'] #cutdown the time zone info

pprint(valdate)
pprint(values)

