import streamlit as st
import pandas as pd
import plotly.express as px
from utils.api import get_model_insights

st.set_page_config(
    page_title="AgriGuard Model Insights",
    page_icon="🧠",
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

.block-container{
    max-width:1220px;
    padding-top:1.4rem;
}

.hero{
    padding:34px 36px;
    border-radius:24px;
    background:
        radial-gradient(circle at 18% 0%, rgba(137,207,240,.30), transparent 35%),
        radial-gradient(circle at 85% 20%, rgba(176,132,255,.20), transparent 30%),
        linear-gradient(135deg,#111936 0%,#17112e 55%,#0b1930 100%);
    border:1px solid rgba(137,207,240,.20);
    box-shadow:0 18px 45px rgba(0,0,0,.35);
    margin-bottom:25px;
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
    margin-bottom:18px;
}

.hero-title{
    font-size:40px;
    font-weight:900;
    color:white;
    margin-bottom:15px;
}

.hero-subtitle{
    font-size:17px;
    line-height:1.8;
    color:#c9def0;
    max-width:900px;
}

.section-block{
    margin-top:40px;
    margin-bottom:12px;
}

.section-title{
    font-size:27px;
    font-weight:900;
    margin-top:0;
    margin-bottom:18px;
    color:white;
}

.kpi, .mini-kpi{
    padding:20px;
    border-radius:22px;
    background:
        radial-gradient(circle at 90% 0%, rgba(137,207,240,.20), transparent 32%),
        linear-gradient(145deg, rgba(17,25,54,.96), rgba(10,14,31,.98));
    border:1px solid rgba(137,207,240,.18);
    box-shadow:0 18px 38px rgba(0,0,0,.30);
    min-height:120px;
    display:flex;
    flex-direction:column;
    justify-content:center;
}

.kpi-line, .mini-kpi-accent{
    width:42px;
    height:4px;
    background:#89cff0;
    border-radius:999px;
    margin-bottom:18px;
}

.kpi-label, .mini-kpi-label{
    color:#c9def0;
    font-size:12px;
    font-weight:900;
    margin-bottom:8px;
}

.kpi-value, .mini-kpi-value{
    color:white;
    font-size:30px;
    font-weight:900;
    line-height:1.2;
}

.info-card{
    padding:24px;
    border-radius:22px;
    background:
        radial-gradient(circle at 90% 0%, rgba(137,207,240,.18), transparent 30%),
        linear-gradient(145deg,#111936,#0b1022);
    border:1px solid rgba(137,207,240,.18);
    box-shadow:0 18px 38px rgba(0,0,0,.30);
    color:white;
    height:100%;
}

.info-title{
    font-size:24px;
    font-weight:900;
    color:white;
    margin-bottom:18px;
}

.info-text{
    color:#c9def0;
    font-size:15px;
    line-height:1.9;
}

.error-card{
    padding:24px;
    border-radius:22px;
    background:rgba(255,92,138,.12);
    border:1px solid rgba(255,92,138,.35);
    color:#ffd7e2;
}
</style>
""", unsafe_allow_html=True)

# ---------- Hero Section ----------
st.markdown("""
<div class="hero">
    <div class="hero-pill">Explainable Artificial Intelligence (XAI)</div>
    <div class="hero-title">🧠 AI Explainability & Model Insights</div>
    <div class="hero-subtitle">
        Explore how the AI model evaluates crop stress,
        understand the most influential features,
        and assess model reliability through
        performance metrics and explainability visualizations.
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- Fetch data from FastAPI ----------
try:
    data = get_model_insights()
except Exception as e:
    st.markdown(f"""
    <div class="error-card">
        ⚠️ Couldn't reach the model insights API.<br>
        <span style="opacity:.75;font-size:13px;">{e}</span>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

feature_df = pd.DataFrame(data["feature_importance"])
accuracy = data["accuracy"]
precision = data["precision"]
recall = data["recall"]
f1 = data["f1_score"]
roc_auc = data["roc_auc"]
model_name = data["model"]

# ---------- Performance Metrics ----------
st.markdown('<div class="section-block"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">📊 AI Performance Snapshot</div>', unsafe_allow_html=True)

perf_metrics = [
    ("Model", model_name),
    ("Accuracy", f"{accuracy:.0%}"),
    ("Precision", f"{precision:.0%}"),
    ("Recall", f"{recall:.0%}"),
    ("F1 Score", f"{f1:.0%}"),
    ("ROC AUC", f"{roc_auc:.2f}"),
]

perf_cols = st.columns(6, gap="medium")

for col, (label, value) in zip(perf_cols, perf_metrics):
    with col:
        st.markdown(f"""
        <div class="mini-kpi">
            <div class="mini-kpi-accent"></div>
            <div class="mini-kpi-label">{label}</div>
            <div class="mini-kpi-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

# ---------- Feature Importance + AI Interpretation ----------
st.markdown('<div class="section-block"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">🌾 Feature Importance</div>', unsafe_allow_html=True)

feature_df = feature_df.sort_values("importance")

fig = px.bar(
    feature_df,
    x="importance",
    y="feature",
    orientation="h",
    text="importance",
    color="importance",
    color_continuous_scale=["#89cff0", "#b084ff", "#ff5c8a"]
)

fig.update_traces(
    texttemplate="%{text:.3f}",
    textposition="outside"
)

fig.update_layout(
    height=480,
    paper_bgcolor="#080b16",
    plot_bgcolor="#080b16",
    font_color="white",
    coloraxis_showscale=False,
    xaxis_title="Importance Score",
    yaxis_title="",
    margin=dict(l=10, r=10, t=20, b=10)
)

left, right = st.columns([2.2, 1], gap="medium")

with left:
    st.plotly_chart(fig, use_container_width=True)

with right:
    top_feature = feature_df.iloc[-1]
    second_feature = feature_df.iloc[-2]

    st.markdown(f"""
    <div class="info-card">
        <div class="info-title">🧠 AI Interpretation</div>
        <div class="info-text">
            ✅ <b>{top_feature["feature"]}</b> is the strongest feature affecting the prediction
            (<b>{top_feature["importance"]:.1%}</b>).
            <br><br>
            ✅ <b>{second_feature["feature"]}</b> is the second most influential vegetation indicator.
            <br><br>
            ✅ Vegetation indices contribute more than climate stress indicators.
            <br><br>
            ✅ Dry Stress has almost no contribution to the trained model.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------- Model Information ----------
st.markdown('<div class="section-block"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">🤖 Model Information</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4, gap="medium")

model_info_cards = [
    ("Algorithm", model_name),
    ("Features", str(len(feature_df))),
    ("Training Samples", "2828"),
    ("Explainability", "Feature Importance")
]

def kpi_html(title, value):
    size = "22px" if len(str(value)) > 12 else "30px"
    return f"""
    <div class="kpi">
        <div class="kpi-line"></div>
        <div class="kpi-label">{title}</div>
        <div class="kpi-value" style="font-size:{size};">{value}</div>
    </div>
    """

for col, (title, value) in zip([c1, c2, c3, c4], model_info_cards):
    with col:
        st.markdown(kpi_html(title, value), unsafe_allow_html=True)