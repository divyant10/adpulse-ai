def calculate_health_score(df):

    score = 100

    avg_ctr = df["ctr"].mean()
    avg_cpc = df["cpc"].mean()
    avg_conv = df["conversion_rate"].mean()

    # CTR evaluation
    if avg_ctr < 2:
        score -= 25
    elif avg_ctr < 4:
        score -= 10

    # CPC evaluation
    if avg_cpc > 3:
        score -= 25
    elif avg_cpc > 2:
        score -= 10

    # Conversion rate evaluation
    if avg_conv < 3:
        score -= 25
    elif avg_conv < 6:
        score -= 10

    return max(score, 0)