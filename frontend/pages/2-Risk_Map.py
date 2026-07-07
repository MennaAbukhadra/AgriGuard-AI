import requests
import pandas as pd
import streamlit as st
import plotly.express as px

from config import API_BASE_URL

st.set_page_config(
    page_title="AgriGuard Risk Map",
    page_icon="Map",
    layout="wide"
)

API_URL = f"{API_BASE_URL}/risk-map"
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(137, 207, 240, 0.22), transparent 30%),
        radial-gradient(circle at top right, rgba(142, 68, 173, 0.24), transparent 34%),
        linear-gradient(180deg, #070914 0%, #0c1022 48%, #080b16 100%);
    color: #f7fbff;
}

.block-container {
    padding-top: 1.4rem;
    max-width: 1220px;
}

[data-testid="stSidebar"] {
    background: #080b16;
    border-right: 1px solid rgba(137, 207, 240, 0.16);
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p {
    color: #eef8ff !important;
}

.hero {
    padding: 34px 36px;
    border-radius: 24px;
    background:
        radial-gradient(circle at 18% 0%, rgba(137, 207, 240, 0.30), transparent 34%),
        radial-gradient(circle at 85% 20%, rgba(176, 132, 255, 0.22), transparent 28%),
        linear-gradient(135deg, #111936 0%, #17112e 52%, #0b1930 100%);
    border: 1px solid rgba(137, 207, 240, 0.22);
    box-shadow: 0 18px 45px rgba(0, 0, 0, 0.35);
    margin-bottom: 22px;
}

.hero-pill {
    display: inline-block;
    padding: 8px 16px;
    border-radius: 999px;
    background: rgba(137, 207, 240, 0.12);
    border: 1px solid rgba(137, 207, 240, 0.28);
    color: #bfefff;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 18px;
}

.hero-title {
    font-size: 40px;
    line-height: 1.1;
    font-weight: 900;
    color: #ffffff;
    margin: 0 0 16px 0;
}

.hero-subtitle {
    font-size: 17px;
    line-height: 1.8;
    color: #c9def0;
    max-width: 940px;
    margin: 0;
}

.map-overview-head {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    gap: 18px;
    margin: 28px 0 16px 0;
}

.map-eyebrow {
    color: #89cff0;
    font-size: 13px;
    font-weight: 900;
    text-transform: uppercase;
    margin-bottom: 5px;
}

.map-title {
    color: #ffffff;
    font-size: 25px;
    font-weight: 900;
}

.map-filter-pill {
    color: #c9def0;
    font-size: 14px;
    font-weight: 700;
    padding: 9px 14px;
    border-radius: 999px;
    background: rgba(137, 207, 240, 0.10);
    border: 1px solid rgba(137, 207, 240, 0.18);
}

.mini-kpi {
    min-height: 118px;
    padding: 18px;
    border-radius: 22px;
    background:
        radial-gradient(circle at 90% 0%, rgba(137, 207, 240, 0.20), transparent 32%),
        linear-gradient(145deg, rgba(17, 25, 54, 0.96), rgba(10, 14, 31, 0.98));
    border: 1px solid rgba(137, 207, 240, 0.18);
    box-shadow: 0 18px 38px rgba(0, 0, 0, 0.28);
}

.mini-kpi-accent {
    width: 42px;
    height: 4px;
    border-radius: 999px;
    background: #89cff0;
    margin-bottom: 18px;
}

.mini-kpi-label {
    color: #c9def0;
    font-size: 12px;
    font-weight: 900;
    margin-bottom: 8px;
}

.mini-kpi-value {
    color: #ffffff;
    font-size: 30px;
    line-height: 1;
    font-weight: 900;
}
</style>
""", unsafe_allow_html=True)


def load_map_data():
    try:
        response = requests.get(API_URL, timeout=80)

    except requests.exceptions.ConnectionError:
        st.error(
            "FastAPI is not reachable. Make sure the backend is running on port 8010."
        )
        st.code("uvicorn main:app --reload --port 8010")
        st.stop()

    except requests.exceptions.Timeout:
        st.error("FastAPI took too long to respond.")
        st.stop()

    except requests.exceptions.RequestException as error:
        st.error(f"Request failed: {error}")
        st.stop()

    if response.status_code != 200:
        st.error(f"FastAPI returned status code: {response.status_code}")
        st.code(response.text)
        st.stop()

    try:
        data = response.json()
    except ValueError:
        st.error("FastAPI did not return valid JSON.")
        st.code(response.text)
        st.stop()

    if not data:
        st.warning("The /risk-map endpoint returned no data.")
        st.stop()

    df = pd.DataFrame(data)

    required_columns = [
        "Grid_ID",
        "date",
        "lat",
        "lon",
        "risk_label",
        "NDVI",
        "risk_score"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        st.error(f"Missing columns from API response: {missing_columns}")
        st.dataframe(df.head())
        st.stop()

    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    if df["date"].isna().any():
        st.error("Some date values could not be converted to datetime.")
        st.dataframe(df[df["date"].isna()])
        st.stop()

    return df


df = load_map_data()

st.markdown("""
<div class="hero">
    <div class="hero-pill">Interactive geospatial intelligence</div>
    <h1 class="hero-title">AgriGuard Risk Map</h1>
    <p class="hero-subtitle">
        Explore monitored agricultural grids by location, risk level, vegetation health,
        and stress probability across Kafr El-Sheikh.
    </p>
</div>
""", unsafe_allow_html=True)

st.sidebar.title("Risk Map Filters")
st.sidebar.caption("Control how monitored grids appear on the map.")

dates = sorted(df["date"].dt.date.unique())

selected_date = st.sidebar.selectbox(
    "Date",
    dates,
    index=len(dates) - 1
)

risk_options = ["Low", "Medium", "High"]

selected_risk = st.sidebar.multiselect(
    "Risk Level",
    risk_options,
    default=risk_options
)

grid_ids = ["All"] + sorted(df["Grid_ID"].astype(str).unique().tolist())

selected_grid = st.sidebar.selectbox(
    "Grid",
    grid_ids
)

color_by = st.sidebar.selectbox(
    "Color By",
    ["Risk Level", "NDVI", "Risk Score"],
    index=0
)

filtered = df[df["date"].dt.date == selected_date].copy()
filtered = filtered[filtered["risk_label"].isin(selected_risk)].copy()

if selected_grid != "All":
    filtered = filtered[
        filtered["Grid_ID"].astype(str) == selected_grid
    ].copy()

if filtered.empty:
    st.warning("No map records match the selected filters.")
    st.stop()

st.markdown(f"""
<div class="map-overview-head">
    <div>
        <div class="map-eyebrow">Geospatial Snapshot</div>
        <div class="map-title">Visible Grid Overview</div>
    </div>
    <div class="map-filter-pill">Color by - {color_by}</div>
</div>
""", unsafe_allow_html=True)

total_visible = filtered["Grid_ID"].nunique()
high_risk = (filtered["risk_label"] == "High").sum()
avg_ndvi = round(filtered["NDVI"].mean(), 3)
avg_risk_score = round(filtered["risk_score"].mean(), 3)

kpi_cols = st.columns(4)

kpi_data = [
    ("Total Visible Grids", total_visible),
    ("High Risk", high_risk),
    ("Average NDVI", avg_ndvi),
    ("Average Risk Score", avg_risk_score),
]

for col, (label, value) in zip(kpi_cols, kpi_data):
    with col:
        st.markdown(f"""
        <div class="mini-kpi">
            <div class="mini-kpi-accent"></div>
            <div class="mini-kpi-label">{label}</div>
            <div class="mini-kpi-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

if color_by == "Risk Level":
    color_column = "risk_label"
    color_args = {
        "color_discrete_map": {
            "Low": "#89cff0",
            "Medium": "#b084ff",
            "High": "#ff5c8a"
        }
    }

elif color_by == "NDVI":
    color_column = "NDVI"
    color_args = {
        "color_continuous_scale": "Blues"
    }

else:
    color_column = "risk_score"
    color_args = {
        "color_continuous_scale": "Purples"
    }

filtered["point_size"] = 8 + (filtered["risk_score"] * 28)

fig = px.scatter_mapbox(
    filtered,
    lat="lat",
    lon="lon",
    color=color_column,
    size="point_size",
    size_max=28,
    zoom=9,
    height=560,
    mapbox_style="carto-darkmatter",
    hover_name="Grid_ID",
    hover_data={
        "risk_label": True,
        "NDVI": ":.3f",
        "risk_score": ":.3f",
        "date": True,
        "lat": False,
        "lon": False,
        "point_size": False
    },
    **color_args
)

fig.update_layout(
    margin=dict(l=0, r=0, t=10, b=0),
    paper_bgcolor="#080b16",
    plot_bgcolor="#080b16",
    font_color="#f7fbff"
)

st.plotly_chart(fig, use_container_width=True)