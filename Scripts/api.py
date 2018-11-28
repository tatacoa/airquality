# API data

from pprint import pprint
import pandas as pd
import requests

API_KEY = 'aa51ef4782205d1fadf8d5151cf29c235a707c98'
COORDS = {
    'Yorkshire and the Humber': (53.90622, -1.03335),
    'North West': (53.53332, -2.69217),
    'East of England': (52.33651, 0.53221),
    'London': (51.50735, -0.12775),
    'North East': (54.94561, -1.94796),
    'West Midlands': (52.47507,-1.82983),
    'East Midlands': (53.04522,-0.39821),
    'South West': (51.15343,-2.4704),
    'South East': (51.17812, -0.55956)
}

URL_TEMPL = 'https://api.waqi.info/feed/geo:{0};{1}/?token={api_key}'

api_responses = {}
for place_name, (lat, lon) in COORDS.items():
    resp = requests.get(URL_TEMPL.format(lat, lon, api_key=API_KEY))
    resp.raise_for_status()
    api_responses[place_name] = resp.json()

pprint(api_responses)
data = []
column_names = ('date', 'region', 'O3', 'PM10', 'PM25', 'NO2')
for place_name, api_resp in api_responses.items():
    values = api_resp['data']['iaqi']
    valdate = api_resp['data']['time']['s'].split()[0] #cutdown the time zone info
    data.append((valdate, place_name, values['o3']['v'], values['pm10']['v'],
                 values['pm25']['v'], values['no2']['v']))

pprint(data)
df = pd.DataFrame(data, columns=column_names)
df.to_csv('../out/realtime_data.csv', index=False)

#### API help
#resp = requests.get('https://api.waqi.info/search/?keyword=bogota&token=aa51ef4782205d1fadf8d5151cf29c235a707c98')
#resp = requests.get('https://api.waqi.info/feed/colombia/bogota/usaquen/?token=aa51ef4782205d1fadf8d5151cf29c235a707c98')
#pprint(resp.json())
##
#data = resp.json()
#values = data['data']['iaqi']
#valdate = data['data']['time']['s'] #cutdown the time zone info
##
#pprint(valdate)
#pprint(values)
#








