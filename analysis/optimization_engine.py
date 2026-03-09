import pandas as pd


# ---------------------------------------------------
# CAMPAIGN OPTIMIZATION ENGINE
# ---------------------------------------------------

def campaign_optimizer(df):

    pause_campaigns = []
    scale_campaigns = []
    waste_campaigns = []

    for _, row in df.iterrows():

        cpc = row.get("cpc", 0)
        ctr = row.get("ctr", 0)
        conversion = row.get("conversion_rate", 0)
        impressions = row.get("impressions", 0)
        campaign_id = row.get("campaign_id")

        # ---------------------------------------------------
        # Campaigns to PAUSE
        # High cost + very low conversion
        # ---------------------------------------------------
        if cpc > 3 and conversion < 0.02:

            pause_campaigns.append(campaign_id)

        # ---------------------------------------------------
        # Campaigns to SCALE
        # High CTR + strong conversions
        # ---------------------------------------------------
        if ctr > 0.08 and conversion > 0.05:

            scale_campaigns.append(campaign_id)

        # ---------------------------------------------------
        # Budget Waste Campaigns
        # High impressions but almost no conversions
        # ---------------------------------------------------
        if impressions > 5000 and conversion < 0.01:

            waste_campaigns.append(campaign_id)

    return pause_campaigns[:5], scale_campaigns[:5], waste_campaigns[:5]


# ---------------------------------------------------
# ANOMALY DETECTION ENGINE
# ---------------------------------------------------

def anomaly_detector(df):

    alerts = []

    avg_ctr = df["ctr"].mean()
    avg_cpc = df["cpc"].mean()
    avg_conversion = df["conversion_rate"].mean()

    for _, row in df.iterrows():

        campaign_id = row["campaign_id"]

        ctr = row["ctr"]
        cpc = row["cpc"]
        conversion = row["conversion_rate"]

        # CTR drop anomaly
        if ctr < avg_ctr * 0.4:

            alerts.append(
                f"📉 Campaign {campaign_id} CTR dropped significantly"
            )

        # CPC spike anomaly
        if cpc > avg_cpc * 2:

            alerts.append(
                f"💰 Campaign {campaign_id} CPC spike detected"
            )

        # Conversion crash anomaly
        if conversion < avg_conversion * 0.3:

            alerts.append(
                f"⚠️ Campaign {campaign_id} conversion rate crash detected"
            )

    return alerts[:5]