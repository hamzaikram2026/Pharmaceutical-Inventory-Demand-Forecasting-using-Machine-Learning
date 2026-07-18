import streamlit as st
import pandas as pd
import plotly.express as px


def show_prediction():

    st.header("Prediction Results")

    prediction_df = pd.read_csv(
        "notebooks/predictions.csv"
    )

    st.subheader("Prediction Sample")

    st.dataframe(
        prediction_df.head(20),
        use_container_width=True
    )

    st.divider()

    fig = px.scatter(
        prediction_df,
        x="Actual Closing Stock",
        y="Predicted Closing Stock",
        title="Actual vs Predicted Closing Stock",
        opacity=0.7
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    fig = px.histogram(
        prediction_df,
        x="Error",
        nbins=30,
        title="Prediction Error Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.download_button(
        "Download Predictions",
        prediction_df.to_csv(index=False),
        "predictions.csv",
        "text/csv"
    )