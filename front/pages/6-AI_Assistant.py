import streamlit as st
from utils.api import ask_ai

st.set_page_config(
    page_title="AgriGuard AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');

html, body, [class*="css"]{
    font-family:'Inter',sans-serif;
}

.stApp{
    background:
        radial-gradient(circle at top left, rgba(137,207,240,.22), transparent 30%),
        radial-gradient(circle at top right, rgba(176,132,255,.22), transparent 35%),
        linear-gradient(180deg,#070914 0%,#0c1022 50%,#080b16 100%);
    color:white;
}

/* ---- Consistent spacing scale ----
   xs:8  sm:12  md:16  lg:24  xl:32  xxl:40
*/

.block-container{
    max-width:1220px;
    padding-top:32px;
    padding-bottom:40px;
}

.hero{
    padding:40px 40px;
    border-radius:24px;
    background:
        radial-gradient(circle at 18% 0%, rgba(137,207,240,.30), transparent 35%),
        radial-gradient(circle at 85% 20%, rgba(176,132,255,.20), transparent 30%),
        linear-gradient(135deg,#111936 0%,#17112e 55%,#0b1930 100%);
    border:1px solid rgba(137,207,240,.20);
    box-shadow:0 18px 45px rgba(0,0,0,.35);
    margin-bottom:32px;
}

.hero-pill{
    display:inline-block;
    padding:8px 16px;
    border-radius:999px;
    background:rgba(137,207,240,.12);
    border:1px solid rgba(137,207,240,.28);
    color:#bfefff;
    font-size:13px;
    font-weight:800;
    margin-bottom:16px;
    line-height:1.4;
}

.hero-title{
    font-size:40px;
    font-weight:900;
    color:white;
    margin-bottom:16px;
    line-height:1.25;
}

.hero-subtitle{
    font-size:17px;
    line-height:1.8;
    color:#c9def0;
    max-width:900px;
    margin:0;
}

.chat-card{
    padding:24px;
    border-radius:22px;
    background:
        radial-gradient(circle at 90% 0%, rgba(137,207,240,.18), transparent 35%),
        linear-gradient(145deg,#111936,#0b1022);
    border:1px solid rgba(137,207,240,.18);
    box-shadow:0 18px 38px rgba(0,0,0,.30);
    margin:24px 0;
}

.section-spacer{
    height:24px;
}

.metric-card{
    padding:20px;
    border-radius:20px;
    background:linear-gradient(145deg,#111936,#0b1022);
    border:1px solid rgba(137,207,240,.18);
    text-align:center;
    height:100%;
}

.metric-title{
    color:#c9def0;
    font-size:13px;
    font-weight:800;
    letter-spacing:.3px;
}

.metric-value{
    color:white;
    font-size:28px;
    font-weight:900;
    margin-top:10px;
}

.recommend-card{
    padding:24px;
    border-radius:22px;
    background:
        radial-gradient(circle at top right, rgba(176,132,255,.18), transparent 35%),
        linear-gradient(145deg,#111936,#0b1022);
    border:1px solid rgba(137,207,240,.18);
    box-shadow:0 18px 38px rgba(0,0,0,.30);
    min-height:280px;
    height:100%;
}

.reading-card{
    padding:24px;
    border-radius:22px;
    background:linear-gradient(145deg,#111936,#0b1022);
    border:1px solid rgba(137,207,240,.18);
    box-shadow:0 18px 38px rgba(0,0,0,.30);
    min-height:280px;
    height:100%;
}

.card-title{
    font-size:22px;
    font-weight:900;
    color:white;
    margin-bottom:16px;
    line-height:1.3;
}

.card-text{
    color:#c9def0;
    line-height:2;
    font-size:15px;
    padding-right:4px;
}

.footer{
    text-align:center;
    margin-top:40px;
    padding:18px;
    color:#89cff0;
    font-size:14px;
    opacity:.8;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-pill">AI Powered Agricultural Assistant</div>
    <div class="hero-title">🤖 AgriGuard AI Assistant</div>
    <div class="hero-subtitle">
        Ask AgriGuard AI about crop stress, vegetation health,
        irrigation recommendations, and agricultural insights based on your field data.
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# User Input
# -----------------------------
prompt = st.chat_input("Ask AgriGuard AI about your crop...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # بيانات مؤقتة
    features = {
        "NDVI": 0.35,
        "veg_health": 0.72,
        "EVI_change": -0.10,
        "water_stress": 1,
        "heat_stress": 0,
        "dry_stress": 1,
        "VPD_stress": 1,
        "drought_severity": 0.63
    }

    with st.spinner("🧠 AgriGuard AI is analyzing the field..."):
        result = ask_ai(prompt, features)

    answer = result.get("answer", "No response returned.")
    risk = result.get("risk", "Unknown")
    probability = result.get("probability", 0)

    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)

    # ---- Metrics ----
    c1, c2 = st.columns(2, gap="large")

    with c1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Current Risk</div>
            <div class="metric-value">{risk}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Stress Probability</div>
            <div class="metric-value">{probability:.1%}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)

    # ---- Recommendations + Reading ----
    left, right = st.columns(2, gap="large")

    with left:
        recommendation = """
- Increase irrigation over the next 48 hours.
- Continue monitoring NDVI changes.
- Inspect the field for drought symptoms.
- Reduce water stress during high temperatures.
- Monitor vegetation health weekly.
"""
        st.markdown(f"""
        <div class="recommend-card">
            <div class="card-title">🌾 AI Recommendations</div>
            <div class="card-text">{recommendation.replace(chr(10), "<br>")}</div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown(f"""
        <div class="reading-card">
            <div class="card-title">📊 Field Readings</div>
            <div class="card-text">
                NDVI: {features['NDVI']}<br>
                Vegetation Health: {features['veg_health']}<br>
                EVI Change: {features['EVI_change']}<br>
                Drought Severity: {features['drought_severity']:.0%}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">AgriGuard AI · Powered by satellite & climate data</div>
""", unsafe_allow_html=True)