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

.main-title{
    font-size:clamp(2rem,3.2vw,3rem);
    font-weight:800;
    line-height:1.15;
    margin-bottom:.3rem;
    overflow-wrap:anywhere;
}

.subtitle{
    font-size:clamp(1rem,2vw,1.5rem);
    font-weight:600;
    color:#BDBDBD;
    margin-bottom:.35rem;
}

.description{
    font-size:clamp(.95rem,1.4vw,1.2rem);
    color:#A8A8A8;
    line-height:1.7;
    margin-bottom:2rem;
    overflow-wrap:anywhere;
}


/* ---------- Markdown Headings ---------- */

h1{
    font-size:clamp(2rem,4vw,3rem)!important;
}

h2{
    font-size:clamp(1.6rem,3vw,2.2rem)!important;
}

h3{
    font-size:clamp(1.3rem,2.5vw,1.7rem)!important;
}


/* ---------- Buttons ---------- */

.stButton button,
.stDownloadButton button{
    font-size:1rem!important;
    font-weight:600!important;
    width:100%;
}


/* ---------- Tabs ---------- */

div[data-testid="stTabs"] button[role="tab"]{
    font-size:clamp(1rem,2.2vw,1.4rem) !important;
    font-weight:700 !important;
    padding:12px 20px !important;
}

div[data-testid="stTabs"] button[role="tab"] p{
    font-size:clamp(1rem,2.2vw,1.4rem) !important;
    font-weight:700 !important;
}

div[data-testid="stTabs"] button[role="tab"][aria-selected="true"]{
    border-bottom: 3px solid #ffffff !important;
}


/* ---------- Metrics ---------- */

[data-testid="stMetricValue"]{
    font-size:clamp(1.4rem,2.2vw,1.8rem)!important;
}

[data-testid="stMetricLabel"]{
    font-size:clamp(.9rem,2vw,1rem)!important;
}


/* ---------- Widget Labels ---------- */

.stFileUploader label,
.stTextArea label,
.stSelectbox label{
    font-size:clamp(1rem,2vw,1.25rem)!important;
    font-weight:700!important;
}


/* ---------- Prevent text overflow ---------- */

*{
    overflow-wrap:anywhere;
    word-break:break-word;
}


/* ---------- Desktop content width cap ---------- */
.block-container{
    max-width:1800px !important;
    margin-left:auto !important;
    margin-right:auto !important;
    padding-left:2rem !important;
    padding-right:2rem !important;
}

html, body{
    overflow-x: hidden;
}
            
.mobile-title{
    display:none;
}

@media (max-width:768px){
    .desktop-title{
        display:none !important;
    }
    .mobile-title{
        display:block !important;
        font-size:1.9rem !important;
        line-height:1.3 !important;
        font-weight:800 !important;
    }
}
            
@media (max-width:768px){
    div[data-testid="stTabs"] div[role="tablist"]{
        display:flex !important;
        flex-wrap:wrap !important;
        width:100% !important;
        overflow-x:visible !important;
    }

    div[data-testid="stTabs"] button[role="tab"]{
        flex:1 1 30% !important;
        min-width:0 !important;
        font-size:0.68rem !important;
        padding:6px 2px !important;
        white-space:nowrap !important;
        text-overflow:ellipsis !important;
        overflow:hidden !important;
    }

    div[data-testid="stTabs"] button[role="tab"] p{
        font-size:0.68rem !important;
        white-space:nowrap !important;
        overflow:hidden !important;
        text-overflow:ellipsis !important;
    }
}

@media (max-width:768px){
    .st-key-metrics-row div[data-testid="stHorizontalBlock"]{
        display:grid !important;
        grid-template-columns:1fr 1fr !important;
        gap:1rem 1.5rem !important;
    }

    .st-key-metrics-row div[data-testid="column"]{
        width:100% !important;
        flex:none !important;
        min-width:0 !important;
    }
}

</style>    


<div class="main-title desktop-title">PharmaInsight : Pharmaceutical Inventory Forecasting</div>
<div class="main-title mobile-title">PharmaInsight :<br>Pharmaceutical<br>Inventory Forecasting</div>

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



with st.container(key="metrics-row"):
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Records", len(stock))
    col2.metric("Medicines", stock["Medicine_Name"].nunique())
    col3.metric("States", stock["State"].nunique())
    col4.metric("Facilities", stock["Facility_Name"].nunique())

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.link_button(
        "Dataset",
        "https://github.com/hamzaikram2026/Pharmaceutical-Inventory-Demand-Forecasting-using-Machine-Learning/tree/main/data", use_container_width=True
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
overflow-wrap:anywhere;
word-break:break-word;
">

<h3 style="color:white; margin-top:0;">Project Summary</h3>

<p style="font-size:clamp(0.95rem,1.6vw,1.25rem); line-height:1.8;">
Developed an end-to-end machine learning pipeline to analyze pharmaceutical inventory
across <b>25 healthcare facilities</b> in <b>5 Indian states</b>, leveraging historical stock
movement data to model medicine demand patterns and support data-driven inventory planning.
</p>

<p style="font-size:clamp(0.95rem,1.6vw,1.25rem); line-height:1.8;">
<b>Analytics & Machine Learning Workflow</b><br>
Data Integration • Exploratory Data Analysis • Lag & Rolling-Window Feature Engineering •
Recursive Feature Elimination (RFE) • Random Forest Regression • GridSearchCV •
5-Fold Cross-Validation
</p>

<p style="font-size:clamp(0.95rem,1.6vw,1.25rem); line-height:1.8;">
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
    
