import streamlit as st

def show_performance():

	st.header("Model Performance")

	st.divider()

	st.subheader("Evaluation Metrics")

	metrics = {
	"Metric": [
	"R² Score",
	"RMSE",
	"MAE",
	"Cross Validation RMSE"
	],
	"Value": [
	"0.95",
	"124.1",
	"87.3",
	"126.8"
	]
	}

	st.table(metrics)
	st.subheader("Performance Summary")

	st.success("""
	The optimized Random Forest Regressor achieved strong predictive
	performance with a high R² score and low prediction error.

	Cross-validation results indicate consistent model performance
	across different data splits.
	""")