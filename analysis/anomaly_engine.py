def detect_anomalies(df):

    alerts = []

    for _, row in df.iterrows():

        if row["ctr"] < 1:
            alerts.append(f"CTR crash in Campaign {row['campaign_id']}")

        if row["cpc"] > 3:
            alerts.append(f"CPC spike in Campaign {row['campaign_id']}")

        if row["conversion_rate"] < 1:
            alerts.append(f"Conversion drop in Campaign {row['campaign_id']}")

    return alerts