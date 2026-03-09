import pandas as pd
import random
import time
import os

FILE_PATH = "data/ads_campaign_data.csv"


def update_campaigns():

    # ---------------- READ DATASET ----------------
    try:
        df = pd.read_csv(FILE_PATH)
    except Exception as e:
        print("Dataset read error:", e)
        return

    if df.empty:
        print("Dataset empty. Skipping update.")
        return

    # ---------------- SELECT RANDOM CAMPAIGNS ----------------
    sample_size = min(50, len(df))
    sample = df.sample(sample_size)

    for idx in sample.index:

        # simulate impressions growth
        df.at[idx, "impressions"] += random.randint(100, 500)

        # simulate clicks
        df.at[idx, "clicks"] += random.randint(5, 50)

        impressions = df.at[idx, "impressions"]
        clicks = df.at[idx, "clicks"]

        # update CTR safely
        if impressions > 0:
            df.at[idx, "ctr"] = round(clicks / impressions, 4)

        # simulate CPC change
        df.at[idx, "cpc"] = round(random.uniform(0.3, 3.5), 2)

        # simulate conversion rate
        df.at[idx, "conversion_rate"] = round(random.uniform(0.01, 0.2), 3)

    # ---------------- SAFE FILE WRITE ----------------

    temp_file = FILE_PATH + ".tmp"

    try:
        df.to_csv(temp_file, index=False)

        # retry logic for Windows file lock
        for attempt in range(5):
            try:
                os.replace(temp_file, FILE_PATH)
                break
            except PermissionError:
                time.sleep(1)

    except Exception as e:
        print("Dataset write error:", e)
        return

    print(f"{sample_size} campaigns updated")


# ---------------- LIVE LOOP ----------------

print("🚀 Live Campaign Stream Started...")

while True:

    update_campaigns()

    # generator slower than dashboard refresh
    time.sleep(8)