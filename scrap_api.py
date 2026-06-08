import json
import time

from opensky_api import OpenSkyApi, TokenManager

from utils import Plane, AIRPORTS_ICAOS

#import sys
#print(sys.executable, "\ndupa\n", sys.version)

tm = TokenManager.from_json_file('credentials.json')
api = OpenSkyApi(token_manager=tm)
#print(help(api))
api_states = api.get_states()
# n = len(api_states.states)
#print(api_states.states)

end = int(time.time())
start = end - 60 * 60 * 24
planes = []

for city, airport in AIRPORTS_ICAOS.items():
    departures = api.get_departures_by_airport(airport=airport, begin=start, end=end)
    print(city, ': ', departures)
    for d in departures:
        track = api.get_track_by_aircraft(d.icao24, d.firstSeen)
        print(d.icao24, '\n', track)
        planes.append(Plane(d.icao24, 'dupa', 'dupa', track))

#track = api.get_track_by_aircraft('a6d83c')
#print('TRACK:', track)
print(planes, '\n', len(planes))
with open('planes.json', 'w') as f:
    for plane in planes:
        json.dump(plane.to_dict(), f)

# Press the green button in the gutter to run the script.
if __name__ == '__scrap_api__':
    pass
