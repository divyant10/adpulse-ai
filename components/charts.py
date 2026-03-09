import plotly.express as px
import streamlit as st


# ---------------- CTR DISTRIBUTION ----------------

def ctr_distribution_chart(df):

    fig = px.histogram(
        df,
        x="ctr",
        nbins=40,
        title="CTR Distribution Across Campaigns",
        labels={"ctr": "Click Through Rate"}
    )

    fig.update_layout(
        height=400,
        xaxis_title="CTR",
        yaxis_title="Number of Campaigns"
    )

    st.plotly_chart(fig, use_container_width=True)


# ---------------- CPC VS CONVERSION ----------------

def cpc_vs_conversion_chart(df):

    sample_size = min(len(df), 2000)

    fig = px.scatter(
        df.sample(sample_size),
        x="cpc",
        y="conversion_rate",
        title="CPC vs Conversion Rate",
        labels={
            "cpc": "Cost Per Click",
            "conversion_rate": "Conversion Rate"
        }
    )

    fig.update_layout(
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)


# ---------------- CAMPAIGN PERFORMANCE BAR ----------------

def campaign_performance_chart(df):

    # categorize campaigns by CTR
    performance = df.copy()

    performance["performance"] = performance["ctr"].apply(
        lambda x: "High CTR" if x > 0.08 else "Medium CTR" if x > 0.03 else "Low CTR"
    )

    summary = performance["performance"].value_counts().reset_index()
    summary.columns = ["Performance Level", "Campaign Count"]

    fig = px.bar(
        summary,
        x="Performance Level",
        y="Campaign Count",
        title="Campaign Performance Distribution"
    )

    fig.update_layout(
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)