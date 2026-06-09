import time
from pathlib import Path

import pandas as pd

AIRPORTS_ICAOS = {
    'JASIONKA': 'EPRZ',
    'BALICE': 'EPKK',
    'OKECIE': 'EPWA',
    'MODLIN': 'EPMO',
    'GDANSK': 'EPGD',
    'WROCLAW': 'EPWR',
    'POZNAN': 'EPPO',
    'LUBLIN': 'EPLB',
    'KATOWICE': 'EPKT',
    'FRANKFURT': 'EDDF',
    'NEWARK': 'KEWR',
    'MONACHIUM': 'EDDM',
}

class Plane:
    def __init__(self, icao24, origin_country, category, track):
        self.icao24 = icao24
        self.origin_country = origin_country
        self.category = category
        self.track = track

    def to_dict(self):
        return {
            'icao24': self.icao24,
            'origin_country': self.origin_country,
            'category': self.category,
            'track':
                [{
                    'time': p.time,
                    'latitude': p.latitude,
                    'longitude': p.longitude,
                    'baro_altitude': p.baro_altitude,
                    'true_track': p.true_track,
                    'on_ground': p.on_ground
                } for p in self.track]
        }

def extract_data():
    start = time.time()
    for i in range(12, 24):
        print(f"{i} started...")
        a = i if i > 9 else f"0{i}"
        df = pd.read_csv(f"data/zipped/states_2017-06-05-{a}.csv.gz", compression="gzip")
        df.to_parquet(f"data/processed/states_2017-06-05-{a}.parquet", index=False)
        print(f"{i} finished")
    end = time.time()
    print(end - start)
    return "Success!"

COLS = ["time", "icao24", "lat", "velocity", "heading", "vertrate", "onground", "baroaltitude", "lon", "callsign"]
def load_data() -> pd.DataFrame:
    files = sorted(Path("data/processed").glob("states_2017-06-05-*.parquet"))
    data = []
    for f in files:
        try:
            d = pd.read_parquet(f, columns=COLS)
            d.dropna(subset=["lat", "lon"])
            data.append(d)
            print(f"{f.name} OK")
        except Exception as e:
            print(f"{f.name} ERROR")
            print(e)
    #data = pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)
    print(data[0].columns)
    return pd.concat(data[0:2], ignore_index=True)

