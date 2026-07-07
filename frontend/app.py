import streamlit as st

st.set_page_config(
    page_title="AgriGuard",
    page_icon="🌾",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(137, 207, 240, 0.24), transparent 32%),
        radial-gradient(circle at top right, rgba(176, 132, 255, 0.24), transparent 34%),
        linear-gradient(180deg, #070914 0%, #0c1022 50%, #080b16 100%);
    color: #f7fbff;
}

.block-container {
    padding-top: 1.6rem;
    max-width: 1180px;
}

.hero {
    min-height: 330px;
    padding: 42px 44px;
    border-radius: 28px;
    background:
        radial-gradient(circle at 18% 0%, rgba(137, 207, 240, 0.34), transparent 34%),
        radial-gradient(circle at 85% 18%, rgba(176, 132, 255, 0.24), transparent 30%),
        linear-gradient(135deg, #111936 0%, #17112e 52%, #0b1930 100%);
    border: 1px solid rgba(137, 207, 240, 0.22);
    box-shadow: 0 22px 55px rgba(0, 0, 0, 0.38);
}

.hero-pill {
    display: inline-block;
    padding: 9px 17px;
    border-radius: 999px;
    background: rgba(137, 207, 240, 0.12);
    border: 1px solid rgba(137, 207, 240, 0.28);
    color: #bfefff;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 22px;
}

.hero-title {
    font-size: 56px;
    line-height: 1;
    font-weight: 900;
    color: #ffffff;
    margin: 0 0 18px 0;
    letter-spacing: 0;
}

.hero-subtitle {
    font-size: 18px;
    line-height: 1.8;
    color: #c9def0;
    max-width: 820px;
    margin: 0 0 28px 0;
}

.hero-actions {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
}

.action-chip {
    padding: 11px 16px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 800;
    color: #eef8ff;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(137, 207, 240, 0.18);
}

.action-chip.primary {
    color: #07101f;
    background: #89cff0;
    border-color: #89cff0;
}

.quick-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-top: 22px;
}

.quick-card {
    padding: 20px;
    border-radius: 22px;
    background: rgba(17, 25, 54, 0.82);
    border: 1px solid rgba(137, 207, 240, 0.16);
    box-shadow: 0 14px 32px rgba(0, 0, 0, 0.26);
}

.quick-card-title {
    color: #ffffff;
    font-size: 16px;
    font-weight: 900;
    margin-bottom: 8px;
}

.quick-card-text {
    color: #b9dff5;
    font-size: 14px;
    line-height: 1.6;
}

@media (max-width: 900px) {
    .hero-title {
        font-size: 42px;
    }

    .quick-grid {
        grid-template-columns: 1fr;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-pill">Satellite crop intelligence platform</div>
    <h1 class="hero-title">AgriGuard AI</h1>
    <p class="hero-subtitle">
        A smart agricultural monitoring system for crop stress detection,
        vegetation health analysis, climate risk tracking, and grid-level field insights.
    </p>
    <div class="hero-actions">
        <div class="action-chip primary">Executive Dashboard</div>
        <div class="action-chip">Risk Map</div>
        <div class="action-chip">Grid Inspection</div>
        <div class="action-chip">AI Prediction</div>
    </div>
</div>

<div class="quick-grid">
    <div class="quick-card">
        <div class="quick-card-title">Vegetation Monitoring</div>
        <div class="quick-card-text">
            Track NDVI, NDWI, and EVI patterns across agricultural grids.
        </div>
    </div>
    <div class="quick-card">
        <div class="quick-card-title">Stress Intelligence</div>
        <div class="quick-card-text">
            Analyze stress probability, risk levels, and critical field zones.
        </div>
    </div>
    <div class="quick-card">
        <div class="quick-card-title">Decision Support</div>
        <div class="quick-card-text">
            Convert satellite and climate signals into actionable recommendations.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)