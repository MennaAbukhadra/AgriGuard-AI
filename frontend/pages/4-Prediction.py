import streamlit as st

from utils.api import predict

st.set_page_config(
    page_title="AgriGuard Prediction",
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

h1, h2, h3, p, label {
    color: #f7fbff !important;
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
    margin-bottom: 24px;
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

.section-title {
    color: #ffffff;
    font-size: 24px;
    font-weight: 900;
    margin: 8px 0 16px 0;
}

.result-card {
    min-height: 210px;
    padding: 24px;
    border-radius: 22px;
    background:
        radial-gradient(circle at 90% 0%, rgba(176, 132, 255, 0.18), transparent 32%),
        linear-gradient(145deg, rgba(17, 25, 54, 0.96), rgba(10, 14, 31, 0.98));
    border: 1px solid rgba(137, 207, 240, 0.18);
    box-shadow: 0 18px 38px rgba(0, 0, 0, 0.28);
}

.result-label {
    color: #c9def0;
    font-size: 13px;
    font-weight: 900;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.result-value {
    color: #ffffff;
    font-size: 34px;
    line-height: 1.1;
    font-weight: 900;
    margin-bottom: 18px;
}

.risk-high {
    color: #ff5c8a;
}

.risk-healthy {
    color: #7df9c4;
}

.probability {
    color: #89cff0;
    font-size: 46px;
    line-height: 1;
    font-weight: 900;
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

.stButton button {
    width: 100%;
    min-height: 48px;
    border-radius: 14px;
    border: 1px solid rgba(137, 207, 240, 0.32);
    background: linear-gradient(135deg, #89cff0 0%, #b084ff 100%);
    color: #07101f;
    font-weight: 900;
}

.stAlert {
    border-radius: 18px;
}
</style>
""", unsafe_allow_html=True)


st.sidebar.title("AgriGuard Filters")
st.sidebar.caption("Use this page to test crop stress risk for one grid reading.")


st.markdown("""
<div class="hero">
    <div class="hero-pill">Machine learning forecast</div>
    <h1 class="hero-title">Crop Stress Prediction</h1>
    <p class="hero-subtitle">
        Enter vegetation and climate readings to estimate whether the selected grid is
        healthy or moving toward crop stress.
    </p>
</div>
""", unsafe_allow_html=True)


left, right = st.columns([1.25, 1], gap="large")

with left:
    st.markdown(
        '<div class="section-title">Grid Readings</div>',
        unsafe_allow_html=True
    )

    with st.form("prediction_form"):
        col1, col2 = st.columns(2)

        with col1:
            NDVI = st.number_input("NDVI", value=0.50, step=0.01)
            veg_health = st.number_input("Vegetation Health", value=0.50, step=0.01)
            EVI_change = st.number_input("EVI Change", value=0.00, step=0.01)
            drought_severity = st.number_input("Drought Severity", value=0.00, step=0.01)

        with col2:
            water_stress = st.selectbox("Water Stress", [0, 1])
            heat_stress = st.selectbox("Heat Stress", [0, 1])
            dry_stress = st.selectbox("Dry Stress", [0, 1])
            VPD_stress = st.selectbox("VPD Stress", [0, 1])

        submitted = st.form_submit_button("Predict")


with right:
    st.markdown(
        '<div class="section-title">Prediction Result</div>',
        unsafe_allow_html=True
    )

    if "prediction_result" not in st.session_state:
        st.markdown("""
        <div class="result-card">
            <div class="result-label">Status</div>
            <div class="result-value">Waiting for input</div>
            <div class="result-label">Stress Probability</div>
            <div class="probability">--</div>
        </div>
        """, unsafe_allow_html=True)


if submitted:
    data = {
        "NDVI": float(NDVI),
        "veg_health": float(veg_health),
        "EVI_change": float(EVI_change),
        "water_stress": int(water_stress),
        "heat_stress": int(heat_stress),
        "dry_stress": int(dry_stress),
        "VPD_stress": int(VPD_stress),
        "drought_severity": float(drought_severity),
    }

    st.session_state.prediction_result = predict(data)


if "prediction_result" in st.session_state:
    result = st.session_state.prediction_result

    with right:
        if "error" in result:
            st.error(result["error"])
        else:
            prediction = result["prediction"]
            probability = result["probability"]

            label = "High Risk" if prediction == 1 else "Healthy"
            label_class = "risk-high" if prediction == 1 else "risk-healthy"

            st.markdown(f"""
            <div class="result-card">
                <div class="result-label">Status</div>
                <div class="result-value {label_class}">{label}</div>
                <div class="result-label">Stress Probability</div>
                <div class="probability">{probability * 100:.2f}%</div>
            </div>
            """, unsafe_allow_html=True)