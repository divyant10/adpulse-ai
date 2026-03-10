st.write("APP STARTED")
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh

from analysis.ads_analyzer import analyze_ads
from analysis.support_analyzer import analyze_support
from analysis.optimization_engine import campaign_optimizer, anomaly_detector
from analysis.health_score import calculate_health_score

from ai_engine.recommendation_engine import generate_recommendations

from components.metrics import (
    show_metrics,
    performance_summary
)

from components.charts import (
    ctr_distribution_chart,
    cpc_vs_conversion_chart,
    campaign_performance_chart
)

from components.gauge import show_health_gauge


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AdPulse AI",
    layout="wide"
)

# ---------------- LOAD CSS ----------------

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🚀 AdPulse AI – Advertising Diagnostics Platform")


# ---------------- SIDEBAR ----------------

st.sidebar.title("AdPulse AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "📊 Dashboard",
        "📈 Campaign Analysis",
        "🎧 Support Analysis",
        "🤖 AI Insights",
        "💬 AI Assistant",
        "⚡ Optimization Engine"
    ]
)

st.sidebar.markdown("---")

uploaded_ads = st.sidebar.file_uploader(
    "Upload Campaign Dataset",
    type=["csv"]
)

uploaded_support = st.sidebar.file_uploader(
    "Upload Support Dataset",
    type=["csv"]
)


# ---------------- SAFE CSV LOADER ----------------

def load_csv_safe(path):

    try:

        df = pd.read_csv(path)

        if df.empty:
            st.warning(f"{path} is empty")
            st.stop()

        df.columns = df.columns.str.strip().str.lower()

        return df

    except Exception as e:

        st.warning(f"Dataset error: {e}")
        st.stop()


# ---------------- LOAD DATA ----------------

if uploaded_ads is not None:

    ads_df = pd.read_csv(uploaded_ads)
    ads_df.columns = ads_df.columns.str.strip().str.lower()

else:

    ads_df = load_csv_safe("data/ads_campaign_data.csv")


if uploaded_support is not None:

    support_df = pd.read_csv(uploaded_support)

else:

    support_df = load_csv_safe("data/support_tickets.csv")


# ---------------- ANALYSIS ----------------

ads_report = analyze_ads(ads_df)
support_report = analyze_support(support_df)

health_score = calculate_health_score(ads_df)


# ---------------- DASHBOARD ----------------

if page == "📊 Dashboard":

    st_autorefresh(interval=5000, key="dashboard_refresh")

    st.header("Campaign Overview")

    show_metrics(ads_report)

    st.markdown("---")

    st.header("Campaign Health Score")

    col1, col2 = st.columns([1,2])

    with col1:
        st.metric(
            label="Health Score",
            value=f"{health_score}/100"
        )

    with col2:
        show_health_gauge(health_score)

    st.markdown("---")

    st.header("Performance Summary")

    performance_summary(ads_df)

    st.markdown("---")

    st.header("CTR Distribution")

    ctr_distribution_chart(ads_df)

    st.markdown("---")

    st.header("Campaign Performance Overview")

    campaign_performance_chart(ads_df)


# ---------------- CAMPAIGN ANALYSIS ----------------

elif page == "📈 Campaign Analysis":

    st.header("Campaign Performance Analysis")

    cpc_vs_conversion_chart(ads_df)

    st.markdown("---")

    st.subheader("Campaign Dataset Preview")

    st.dataframe(ads_df.head(20), width="stretch")


# ---------------- SUPPORT ANALYSIS ----------------

elif page == "🎧 Support Analysis":

    st.header("Support Ticket Insights")

    st.subheader("Top Issues")

    st.write(support_report["Top Issues"])

    st.subheader("Average Resolution Time")

    st.write(support_report["Average Resolution Time"])

    st.subheader("Priority Distribution")

    st.write(support_report["Priority Distribution"])


# ---------------- AI INSIGHTS ----------------

elif page == "🤖 AI Insights":

    st.header("AI Optimization Strategy")

    if st.button("Generate AI Strategy"):

        with st.spinner("Analyzing campaigns with AI..."):

            recommendations = generate_recommendations(
                ads_report,
                support_report["Top Issues"]
            )

        st.success("Analysis Complete")

        st.markdown(recommendations)


# ---------------- AI ASSISTANT ----------------

elif page == "💬 AI Assistant":

    st.header("Ask AdPulse AI")

    if "messages" not in st.session_state:

        st.session_state.messages = []

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    prompt = st.chat_input("Ask about your campaigns...")

    if prompt:

        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        context = f"""
Campaign Diagnostics:
{ads_report}

Support Insights:
{support_report['Top Issues']}

User Question:
{prompt}
"""

        with st.chat_message("assistant"):

            with st.spinner("AdPulse AI is analyzing..."):

                response = generate_recommendations(context, "")

                st.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )


# ---------------- OPTIMIZATION ENGINE ----------------

elif page == "⚡ Optimization Engine":

    st.header("AI Campaign Optimization Engine")

    pause, scale, waste = campaign_optimizer(ads_df)

    st.subheader("Campaigns to Pause")

    if pause:
        st.dataframe(ads_df.loc[pause], width="stretch")
    else:
        st.info("No campaigns need to be paused")

    st.subheader("Campaigns to Scale")

    if scale:
        st.dataframe(ads_df.loc[scale], width="stretch")
    else:
        st.info("No campaigns recommended for scaling")

    st.subheader("Budget Waste Campaigns")

    if waste:
        st.dataframe(ads_df.loc[waste], width="stretch")
    else:
        st.info("No budget waste campaigns detected")

    st.subheader("Anomaly Alerts")

    alerts = anomaly_detector(ads_df)

    if alerts:

        st.warning("🚨 Campaign Anomalies Detected")

        for a in alerts:

            st.warning(a)
