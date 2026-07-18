import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

import joblib


def show_feature_importance():

    st.header("Feature Importance")

    # Load trained model
    model = joblib.load("notebooks/model.pkl")

    # Load feature names
    feature_names = joblib.load("notebooks/feature_names.pkl")

    # Create DataFrame
    feature_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": model.feature_importances_
    })

    # Sort by importance
    feature_df = (
        feature_df
        .sort_values(by="Importance", ascending=False)
        .head(10)
    )

    # Plot
    fig = px.bar(
        feature_df,
        x="Importance",
        y="Feature",
        orientation="h",
        color="Importance",
        title="Top 10 Most Important Features"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        xaxis_title="Importance Score",
        yaxis_title="Feature"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "Feature importance indicates how much each feature contributed "
        "to the Random Forest model's predictions. Higher scores represent "
        "greater influence on predicting pharmaceutical inventory demand."
    )