import pandas as pd
import time


def extract_data():
    start = time.time()
    for i in range(10, 24):
        print(f"{i} started...")
        a = i if i > 9 else f"0{i}"
        df = pd.read_csv(f"data/zipped/states_2017-06-05-{a}.csv.gz", compression="gzip")
        df.to_parquet(f"data/processed/states_2017-06-05-{a}.parquet", index=False)
        print(f"{i} finished")
    end = time.time()
    print(end - start)
    return "Success!"

extract_data()

# start = time.time()
# df = pd.concat([pd.read_parquet(f"data/processed/states_2017-06-05-0{i}.parquet") for i in range(5)], ignore_index=True)
# end = time.time()
# print(end - start)
# print(df.tail(), len(df))
#
# df = df.sort_values(["icao24", "time"])
# groups = df.groupby("icao24")
#
# df["time_diff"] = df.groupby("icao24")["time"].diff()
# df["flight_icao"] = (df["time_diff"] > 1800).groupby(df["icao24"]).cumsum()
#
# flights = df.groupby(["icao24", "flight_icao"])
#
# print(flights.tail())
# print(df[["icao24", "flight_icao"]].value_counts().head())