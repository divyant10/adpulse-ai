def root_cause_analysis(ads_report):

    issues = []

    if ads_report["Low CTR Campaigns"] > 0:
        issues.append(
            "Low CTR detected. Possible cause: weak ad creatives or poor targeting."
        )

    if ads_report["High CPC Campaigns"] > 0:
        issues.append(
            "High CPC detected. Possible cause: expensive keywords or poor bidding strategy."
        )

    if ads_report["Low Conversion Campaigns"] > 0:
        issues.append(
            "Low conversions detected. Possible cause: landing page issues."
        )

    return issues