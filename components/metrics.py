import streamlit as st


# ---------------- CAMPAIGN METRICS ----------------

def show_metrics(ads_report):

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        label="📊 Total Campaigns",
        value=f"{ads_report.get('Total Campaigns', 0):,}"
    )

    col2.metric(
        label="⚠ Low CTR Campaigns",
        value=f"{ads_report.get('Low CTR Campaigns', 0):,}"
    )

    col3.metric(
        label="💰 High CPC Campaigns",
        value=f"{ads_report.get('High CPC Campaigns', 0):,}"
    )

    col4.metric(
        label="📉 Low Conversion Campaigns",
        value=f"{ads_report.get('Low Conversion Campaigns', 0):,}"
    )


# ---------------- CAMPAIGN HEALTH SCORE ----------------

def campaign_health_score(ads_report):

    total = ads_report.get("Total Campaigns", 0)

    low_ctr = ads_report.get("Low CTR Campaigns", 0)
    high_cpc = ads_report.get("High CPC Campaigns", 0)
    low_conversion = ads_report.get("Low Conversion Campaigns", 0)

    bad = low_ctr + high_cpc + low_conversion

    if total == 0:
        return 0

    score = max(0, 100 - int((bad / total) * 100))

    return score


# ---------------- PERFORMANCE SUMMARY ----------------

def performance_summary(ads_df):

    # normalize column names (avoid CTR / ctr / Ctr errors)
    ads_df.columns = ads_df.columns.str.strip().str.lower()

    required_columns = ["ctr", "cpc", "conversion_rate"]

    # check if required columns exist
    for col in required_columns:
        if col not in ads_df.columns:
            st.warning(f"Column '{col}' not found in dataset.")
            return

    avg_ctr = ads_df["ctr"].mean()
    avg_cpc = ads_df["cpc"].mean()
    avg_conversion = ads_df["conversion_rate"].mean()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Average CTR",
        f"{avg_ctr:.2%}"
    )

    col2.metric(
        "Average CPC",
        f"${avg_cpc:.2f}"
    )

    col3.metric(
        "Conversion Rate",
        f"{avg_conversion:.2%}"
    )