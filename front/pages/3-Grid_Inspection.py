import requests
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="AgriGuard Grid Inspection",
    page_icon=None,
    layout="wide"
)

API_URL = "https://agriguard-api-hahqevhdc3eab3c8.uaenorth-01.azurewebsites.net/grid-inspection"

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #070914 0%, #0c1022 50%, #080b16 100%);
    color: #f7fbff;
}

.block-container {
    padding-top: 1.4rem;
    max-width: 1220px;
}

.hero {
    padding: 34px 36px;
    border-radius: 24px;
    background: linear-gradient(135deg, #111936 0%, #17112e 52%, #0b1930 100%);
    border: 1px solid rgba(137, 207, 240, 0.22);
    margin-bottom: 22px;
}

.hero-title {
    font-size: 40px;
    font-weight: 900;
    color: #ffffff;
    margin: 0 0 12px 0;
}

.hero-subtitle {
    font-size: 17px;
    line-height: 1.7;
    color: #c9def0;
    margin: 0;
}

.metric-card {
    padding: 18px;
    border-radius: 18px;
    background: #111936;
    border: 1px solid rgba(137, 207, 240, 0.18);
}

.metric-label {
    color: #c9def0;
    font-size: 12px;
    font-weight: 900;
}

.metric-value {
    color: #ffffff;
    font-size: 28px;
    font-weight: 900;
}
</style>
""", unsafe_allow_html=True)


@st.cache_data(ttl=600)
def load_data():
    response = requests.get(API_URL, timeout=60)
    response.raise_for_status()

    df = pd.DataFrame(response.json())
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    return df.dropna(subset=["Grid_ID", "date"])


def metric_card(label, value):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)


df = load_data()

st.markdown("""
<div class="hero">
    <h1 class="hero-title">Grid Inspection</h1>
    <p class="hero-subtitle">
        Inspect historical vegetation, climate indicators, and crop health
        for a selected agricultural grid.
    </p>
</div>
""", unsafe_allow_html=True)

st.sidebar.title("Grid Inspection")

selected_grid = st.sidebar.selectbox(
    "Select Grid",
    sorted(df["Grid_ID"].astype(str).unique())
)

grid_df = df[df["Grid_ID"].astype(str) == selected_grid].copy()

selected_date = st.sidebar.selectbox(
    "Select Date",
    grid_df["date"].dt.strftime("%Y-%m-%d").drop_duplicates().tolist()[::-1]
)

latest = grid_df[grid_df["date"] == pd.to_datetime(selected_date)].iloc[0]
history_df = grid_df[grid_df["date"] <= pd.to_datetime(selected_date)].copy()

st.subheader(f"Current Status - {selected_grid}")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    metric_card("NDVI", f"{latest['NDVI']:.3f}")

with col2:
    metric_card("NDWI", f"{latest['NDWI']:.3f}")

with col3:
    metric_card("EVI", f"{latest['EVI']:.3f}")

with col4:
    metric_card("Vegetation Health", f"{latest['veg_health']:.3f}")

with col5:
    metric_card("Risk Score", f"{latest['risk_score']:.2f}")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Vegetation Indices")

    fig = px.line(
        history_df,
        x="date",
        y=["NDVI", "NDWI", "EVI"],
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Climate Indicators")

    climate_cols = [
        col for col in ["temperature", "rainfall", "humidity", "VPD"]
        if col in history_df.columns
    ]

    fig2 = px.line(
        history_df,
        x="date",
        y=climate_cols,
        markers=True
    )

    st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.subheader("Latest Readings")

st.dataframe(
    latest.to_frame().T,
    use_container_width=True
)