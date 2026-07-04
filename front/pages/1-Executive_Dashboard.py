import requests
import pandas as pd
import streamlit as st
import plotly.express as px

# =========================
# Page Config
# =========================

st.set_page_config(
    page_title="AgriGuard Executive Dashboard",
    page_icon="🌾",
    layout="wide"
)

# =========================
# Styling
# =========================

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

[data-testid="stSidebar"] .stCaptionContainer {
    color: #b9dff5 !important;
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
    letter-spacing: 0;
}

.hero-subtitle {
    font-size: 17px;
    line-height: 1.8;
    color: #c9def0;
    max-width: 940px;
    margin: 0;
}

.section-title {
    font-size: 22px;
    font-weight: 900;
    color: #ffffff;
    margin: 26px 0 14px 0;
}

.overview-head {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    gap: 18px;
    margin: 28px 0 16px 0;
}

.eyebrow {
    color: #89cff0;
    font-size: 13px;
    font-weight: 900;
    letter-spacing: 0.4px;
    text-transform: uppercase;
    margin-bottom: 5px;
}

.overview-title {
    color: #ffffff;
    font-size: 25px;
    font-weight: 900;
}

.overview-date {
    color: #c9def0;
    font-size: 14px;
    font-weight: 700;
    padding: 9px 14px;
    border-radius: 999px;
    background: rgba(137, 207, 240, 0.10);
    border: 1px solid rgba(137, 207, 240, 0.18);
}
.kpi-card {
    min-height: 150px;
    padding: 18px 16px;
    border-radius: 22px;
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(137, 207, 240, 0.18);
    background:
        radial-gradient(circle at 84% 10%, rgba(137, 207, 240, 0.20), transparent 28%),
        linear-gradient(145deg, rgba(17, 25, 54, 0.96), rgba(10, 14, 31, 0.98));
    box-shadow: 0 18px 38px rgba(0, 0, 0, 0.30);
}

.kpi-card::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        linear-gradient(120deg, rgba(255,255,255,0.08), transparent 35%);
    opacity: 0.25;
    pointer-events: none;
}

.kpi-card.blue { border-color: rgba(137, 207, 240, 0.30); }
.kpi-card.cyan { border-color: rgba(77, 225, 255, 0.30); }
.kpi-card.purple { border-color: rgba(176, 132, 255, 0.30); }
.kpi-card.green { border-color: rgba(125, 249, 196, 0.30); }
.kpi-card.pink { border-color: rgba(255, 92, 138, 0.34); }
.kpi-card.soft { border-color: rgba(215, 236, 255, 0.25); }

.kpi-accent {
    width: 42px;
    height: 4px;
    border-radius: 999px;
    margin-bottom: 22px;
    position: relative;
    z-index: 1;
}

.kpi-card.blue .kpi-accent { background: #89cff0; }
.kpi-card.cyan .kpi-accent { background: #4de1ff; }
.kpi-card.purple .kpi-accent { background: #b084ff; }
.kpi-card.green .kpi-accent { background: #7df9c4; }
.kpi-card.pink .kpi-accent { background: #ff5c8a; }
.kpi-card.soft .kpi-accent { background: #d7ecff; }

.kpi-chip {
    color: #a8c6dd;
    font-size: 10px;
    font-weight: 800;
    line-height: 1.25;
    min-height: 26px;
    max-width: 115px;
    position: relative;
    z-index: 1;
}

.kpi-label {
    color: #c9def0;
    font-size: 12px;
    font-weight: 900;
    margin: 13px 0 7px 0;
    position: relative;
    z-index: 1;
}

.kpi-value {
    color: #ffffff;
    font-size: clamp(24px, 2.4vw, 34px);
    line-height: 1;
    font-weight: 900;
    position: relative;
    z-index: 1;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.kpi-progress {
    height: 5px;
    width: 100%;
    margin-top: 18px;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.08);
    overflow: hidden;
    position: relative;
    z-index: 1;
}

.kpi-progress span {
    display: block;
    height: 100%;
    border-radius: 999px;
    background: #89cff0;
}

.kpi-card.blue .kpi-progress span { background: #89cff0; }
.kpi-card.cyan .kpi-progress span { background: #4de1ff; }
.kpi-card.purple .kpi-progress span { background: #b084ff; }
.kpi-card.green .kpi-progress span { background: #7df9c4; }
.kpi-card.pink .kpi-progress span { background: #ff5c8a; }
.kpi-card.soft .kpi-progress span { background: #d7ecff; }

h1, h2, h3, p, label {
    color: #f7fbff;
}

hr {
    border-color: rgba(137, 207, 240, 0.12);
}

div[data-testid="stDataFrame"] {
    border-radius: 18px;
    border: 1px solid rgba(137, 207, 240, 0.18);
    overflow: hidden;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.25);
}

.stAlert {
    border-radius: 18px;
}

div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    background-color: #111936;
    border-color: rgba(137, 207, 240, 0.22);
}

div[data-baseweb="select"] span,
div[data-baseweb="input"] input {
    color: #eef8ff;
}
</style>
""", unsafe_allow_html=True)

# =========================
# Constants
# =========================

API_URL = "http://127.0.0.1:8010/dashboard"

risk_options = ["Low", "Medium", "High"]

risk_colors = {
    "Low": "#89cff0",
    "Medium": "#b084ff",
    "High": "#ff5c8a"
}

chart_layout = {
    "height": 370,
    "plot_bgcolor": "#111936",
    "paper_bgcolor": "#111936",
    "font_color": "#f7fbff",
    "xaxis": dict(
        gridcolor="rgba(137, 207, 240, 0.10)",
        zerolinecolor="rgba(137, 207, 240, 0.12)"
    ),
    "yaxis": dict(
        gridcolor="rgba(137, 207, 240, 0.10)",
        zerolinecolor="rgba(137, 207, 240, 0.12)"
    ),
    "margin": dict(l=40, r=30, t=45, b=40)
}

# =========================
# Load Data
# =========================

@st.cache_data
def load_data():
    response = requests.get(API_URL)

    if response.status_code != 200:
        st.error("Failed to connect to FastAPI")
        st.stop()

    data = response.json()

    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])

    return df


df = load_data()

# =========================
# Sidebar
# =========================

st.sidebar.title("AgriGuard Filters")
st.sidebar.caption("Filter monitored grids by date, risk level, and grid ID.")

dates = sorted(df["date"].dt.date.unique())

selected_date = st.sidebar.selectbox(
    "Date",
    dates,
    index=len(dates) - 1
)

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

# =========================
# Filter Data
# =========================

filtered = df[df["date"].dt.date == selected_date]

filtered = filtered[
    filtered["risk_label"].isin(selected_risk)
]

if selected_grid != "All":
    filtered = filtered[
        filtered["Grid_ID"].astype(str) == selected_grid
    ]

# =========================
# Header
# =========================

st.markdown("""
<div class="hero">
    <div class="hero-pill">Satellite crop monitoring</div>
    <h1 class="hero-title">AgriGuard AI</h1>
    <p class="hero-subtitle">
        Interactive agricultural dashboard for vegetation health, crop stress probability,
        grid-level monitoring, and climate-driven risk analysis.
    </p>
</div>
""", unsafe_allow_html=True)

if filtered.empty:
    st.warning("No records match the selected filters.")
    st.stop()

# =========================
# KPIs
# =========================

st.markdown(f"""
<div class="overview-head">
    <div>
        <div class="eyebrow">Live Monitoring Snapshot</div>
        <div class="overview-title">Field Command Center</div>
    </div>
    <div class="overview-date">Latest scan · {selected_date}</div>
</div>
""", unsafe_allow_html=True)

total_grids = filtered["Grid_ID"].nunique()
avg_ndvi = round(filtered["NDVI"].mean(), 3)
avg_risk_score = round(filtered["risk_score"].mean(), 3)
healthy = (filtered["risk_label"] == "Low").sum()
high_risk = (filtered["risk_label"] == "High").sum()
latest_date = str(selected_date)

kpi_items = [
    ("Total Grids", total_grids, "Monitored field cells", "blue", "100%"),
    ("Average NDVI", avg_ndvi, "Vegetation health index", "cyan", f"{min(avg_ndvi * 100, 100):.0f}%"),
    ("Avg Risk Score", avg_risk_score, "Mean risk level", "purple", f"{min(avg_risk_score * 100, 100):.0f}%"),
    ("Healthy", healthy, "Stable crop zones", "green", f"{(healthy / max(len(filtered), 1)) * 100:.0f}%"),
    ("High Risk", high_risk, "Needs attention", "pink", f"{(high_risk / max(len(filtered), 1)) * 100:.0f}%"),
    ("Latest Date", latest_date, "Current selected scan", "soft", "100%"),
]

cols = st.columns(6)

for col, item in zip(cols, kpi_items):
    label, value, caption, tone, progress = item

    with col:
        st.markdown(f"""
        <div class="kpi-card {tone}">
            <div class="kpi-accent"></div>
            <div class="kpi-chip">{caption}</div>
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-progress">
                <span style="width: {progress};"></span>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# =========================
# Charts Row 1
# =========================

left, right = st.columns(2)

with left:
    st.markdown("<div class='section-title'>Risk Distribution</div>", unsafe_allow_html=True)

    risk_df = (
        filtered["risk_label"]
        .value_counts()
        .reindex(risk_options, fill_value=0)
        .reset_index()
    )

    risk_df.columns = ["Risk Level", "Count"]

    fig = px.bar(
        risk_df,
        x="Risk Level",
        y="Count",
        color="Risk Level",
        color_discrete_map=risk_colors,
        text="Count"
    )

    fig.update_traces(
        textposition="outside",
        marker_line_width=0
    )

    fig.update_layout(
        **chart_layout,
        showlegend=False,
        xaxis_title="Risk Level",
        yaxis_title="Number of Records"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown("<div class='section-title'>NDVI Distribution</div>", unsafe_allow_html=True)

    fig = px.histogram(
        filtered,
        x="NDVI",
        nbins=35,
        color_discrete_sequence=["#89cff0"]
    )

    fig.update_traces(
        marker_line_width=0,
        opacity=0.92
    )

    fig.update_layout(
        **chart_layout,
        xaxis_title="NDVI",
        yaxis_title="Count"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# =========================
# Charts Row 2
# =========================

left, right = st.columns(2)

with left:
    st.markdown("<div class='section-title'>Monthly Risk Trend</div>", unsafe_allow_html=True)

    monthly = (
        df.groupby(df["date"].dt.to_period("M"))["risk_score"]
        .mean()
        .reset_index()
    )

    monthly["date"] = monthly["date"].astype(str)

    fig = px.line(
        monthly,
        x="date",
        y="risk_score",
        markers=True,
        color_discrete_sequence=["#b084ff"]
    )

    fig.update_traces(
        line=dict(width=3),
        marker=dict(
            size=8,
            color="#89cff0",
            line=dict(width=2, color="#b084ff")
        )
    )

    fig.update_layout(
        **chart_layout,
        xaxis_title="Month",
        yaxis_title="Average Stress Probability"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:
    st.markdown("<div class='section-title'>Average NDVI Over Time</div>", unsafe_allow_html=True)

    ndvi = (
        df.groupby("date")["NDVI"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        ndvi,
        x="date",
        y="NDVI",
        color_discrete_sequence=["#89cff0"]
    )

    fig.update_traces(
        line=dict(width=3)
    )

    fig.update_layout(
        **chart_layout,
        xaxis_title="Date",
        yaxis_title="Average NDVI"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# =========================
# Dataset Summary
# =========================

st.markdown("<div class='section-title'>Dataset Summary</div>", unsafe_allow_html=True)

display_columns = [
    "Grid_ID",
    "date",
    "risk_label",
    "risk_score",
    "NDVI",
    "NDWI",
    "EVI"
]

available_columns = [
    col for col in display_columns
    if col in filtered.columns
]

st.dataframe(
    filtered[available_columns].sort_values("date", ascending=False),
    use_container_width=True,
    height=350
)