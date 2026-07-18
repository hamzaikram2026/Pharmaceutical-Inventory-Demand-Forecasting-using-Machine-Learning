import streamlit as st

def show_model():

    st.header("Machine Learning Model")

    col1, col2 = st.columns(2)

    col1.metric("Algorithm", "Random Forest")
    col2.metric("Target Variable", "Closing_Stock")

    with st.expander("Feature Engineering"):

        st.markdown("""
        - Lag Features
        - Rolling Mean
        - Rolling Standard Deviation
        - Time-based Features
        """)

    with st.expander("Validation"):

        st.markdown("""
        - Train/Test Split
        - GridSearchCV Hyperparameter Tuning
        - Cross Validation
        """)
