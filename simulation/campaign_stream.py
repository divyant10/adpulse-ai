import random


def generate_campaign_event(df):

    campaign = random.choice(df["campaign_id"].tolist())

    event_type = random.choice([
        "CTR drop detected",
        "CPC spike detected",
        "Conversion spike detected",
        "Budget increase detected"
    ])

    return f"Campaign {campaign}: {event_type}"