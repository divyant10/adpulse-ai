import pandas as pd


def analyze_ads(df):

    # normalize column names
    df.columns = df.columns.str.strip().str.lower()

    total_campaigns = len(df)

    # campaign diagnostics
    low_ctr = df[df["ctr"] < 0.03]          # CTR < 3%
    high_cpc = df[df["cpc"] > 2.5]          # CPC > $2.5
    low_conversion = df[df["conversion_rate"] < 0.05]   # <5%

    report = {
        "Total Campaigns": total_campaigns,
        "Low CTR Campaigns": len(low_ctr),
        "High CPC Campaigns": len(high_cpc),
        "Low Conversion Campaigns": len(low_conversion)
    }

    return report