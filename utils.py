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
