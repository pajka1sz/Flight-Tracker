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
