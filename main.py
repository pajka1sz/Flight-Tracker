import pandas as pd
import time
from utils import extract_data, load_data

def export_df() -> pd.DataFrame:
    start = time.time()
    df = load_data()
    end = time.time()
    print(end - start)
    #print(df.tail(), len(df))

    #df = df.dropna(subset=["lat", "lon"])
    print(len(df))
    df = df.sort_values(["icao24", "time"])
    #groups = df.groupby("icao24")
    print("Df exported")
    return df

    #df["time_diff"] = df.groupby("icao24")["time"].diff()
    #df["flight_icao"] = (df["time_diff"] > 1800).groupby(df["icao24"]).cumsum()

    #flights = df.groupby(["icao24", "flight_icao"])

# flights = df.groupby(["icao24", "callsign"])
# trajectories = {}
#
# for (icao, call), group in flights:
#     trajectories[(icao, call)] = group.sort_values("time")[["lat", "lon", "time"]].values
#     print(icao, ": ", trajectories[(icao, call)])

#print("Flights:\n", flights.tail())
#print(df[["icao24", "flight_icao"]].value_counts().head())

if __name__ == "__main__":
    pass