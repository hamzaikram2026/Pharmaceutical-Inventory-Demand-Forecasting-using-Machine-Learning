import streamlit as st
from src.eda import show_eda
from src.model import show_model
from src.profile import show_profile
from src.performance import show_performance
from src.feature_importance import show_feature_importance
from src.prediction import show_prediction


st.set_page_config(
    page_title="PharmaInsight : Pharmaceutical Inventory Analytics",
    page_icon="",
    layout="wide",
)

st.markdown("""
<style>

/* ---------- Header ---------- */

.main-title {
    font-size: 3.8rem;
    font-weight: 800;
    margin-bottom: 0.2rem;
}

.subtitle {
    font-size: 1.5rem;
    font-weight: 600;
    color: #BDBDBD;
    margin-bottom: 0.35rem;
}

.description {
    font-size: 1.2rem;
    color: #A8A8A8;
    margin-bottom: 2rem;
}



/* ---------- Markdown Headings ---------- */

h1 {font-size: 3rem !important;}
h2 {font-size: 2.2rem !important;}
h3 {font-size: 1.7rem !important;}



/* ---------- Buttons ---------- */

.stButton button,
.stDownloadButton button {
    font-size: 1rem !important;
    font-weight: 600 !important;
}

/* ---------- Tabs ---------- */

div[data-testid="stTabs"] button p {
    font-size: 20px !important;
    font-weight: 700 !important;
}

div[data-testid="stTabs"] button {
    padding: 12px 20px !important;
}

/* ---------- Metrics ---------- */

[data-testid="stMetricValue"] {
    font-size: 2rem !important;
}

[data-testid="stMetricLabel"] {
    font-size: 1rem !important;
}
/* Widget labels (Dataset, Business Question, Target column, etc.) */
.stFileUploader label,
.stTextArea label,
.stSelectbox label {
    font-size: 1.25rem !important;
    font-weight: 700 !important;
}

</style>

<div class="main-title">PharmaInsight : Pharmaceutical Inventory Forecasting</div>

<div class="subtitle">
Developed by Hamza Ikram
</div>

<div class="description">
   End-to-end analytics and machine learning dashboard for pharmaceutical inventory demand forecasting,
    feature engineering, and predictive modeling across healthcare facilities.
</div>

""", unsafe_allow_html=True)

import pandas as pd

stock = pd.read_csv("data/medicine_stock.csv")
medicine = pd.read_csv("data/medicines.csv")



col1, col2, col3, col4 = st.columns(4)
col1.metric("Records", len(stock))
col2.metric("Medicines", stock["Medicine_Name"].nunique())
col3.metric("States", stock["State"].nunique())
col4.metric("Facilities", stock["Facility_Name"].nunique())

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.link_button(
        "Dataset",
        "https://github.com/hamzaikram2026/Pharmaceutical-Inventory-Demand-Forecasting-using-Machine-Learning/data", use_container_width=True
    )

with col2:
    st.link_button(
        "Source Code",
        "https://github.com/hamzaikram2026/Pharmaceutical-Inventory-Demand-Forecasting-using-Machine-Learning",
         use_container_width=True
    )

with col3:
    st.link_button(
        "Project README",
        "https://github.com/hamzaikram2026/Pharmaceutical-Inventory-Demand-Forecasting-using-Machine-Learning/blob/main/README.md", use_container_width=True
    )
st.write("")
st.write("")

st.markdown("""
<div style="
background-color:#1B1F24;
padding:20px;
border-radius:10px;
border:1px solid #3A3A3A;
color:white;
">

<h3 style="color:white; margin-top:0;">Project Summary</h3>

<p style="font-size:20px; line-height:1.8;">
Developed an end-to-end machine learning pipeline to analyze pharmaceutical inventory
across <b>25 healthcare facilities</b> in <b>5 Indian states</b>, leveraging historical stock
movement data to model medicine demand patterns and support data-driven inventory planning.
</p>

<p style="font-size:20px; line-height:1.8;">
<b>Analytics & Machine Learning Workflow</b><br>
Data Integration • Exploratory Data Analysis • Lag & Rolling-Window Feature Engineering •
Recursive Feature Elimination (RFE) • Random Forest Regression • GridSearchCV •
5-Fold Cross-Validation
</p>

<p style="font-size:20px; line-height:1.8;">
<b>Business Objective</b><br>
Explore how historical inventory trends can improve demand forecasting,
reduce stockout and overstock risk, and support proactive pharmaceutical
inventory management.
</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Profile",
    "EDA",
    "Model",
    "Performance",
    "Feature Importance",
    "Prediction"
])

with tab1:
    show_profile(stock)

with tab2:
    show_eda(stock)

with tab3:
    show_model()

with tab4:
    show_performance()


with tab5:
    show_feature_importance()
	
with tab6:
    show_prediction()
    