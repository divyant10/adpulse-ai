import streamlit as st
import plotly.graph_objects as go


def show_health_gauge(score):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": "Campaign Health Score"},
        gauge={

            "axis": {"range": [0, 100]},

            "bar": {"color": "#22c55e"},

            "steps": [
                {"range": [0, 40], "color": "#7f1d1d"},   # Poor
                {"range": [40, 70], "color": "#78350f"},  # Average
                {"range": [70, 100], "color": "#064e3b"}  # Healthy
            ],

            "threshold": {
                "line": {"color": "white", "width": 4},
                "thickness": 0.75,
                "value": score
            }
        }
    ))

    fig.update_layout(
        height=350,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    st.plotly_chart(fig, width="stretch")