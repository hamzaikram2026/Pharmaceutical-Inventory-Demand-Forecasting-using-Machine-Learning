import streamlit as st

def show_profile(stock):
	st.header("Dataset Overview")

	col1, col2,col3,col4 = st.columns(4)

	with col1:
		st.metric("Rows", stock.shape[0])
	with col2:
		st.metric("Columns", stock.shape[1])
	with col3:
		st.metric("Missing Values", stock.isnull().sum().sum())
	with col4:
		st.metric("Duplicate Rows", stock.duplicated().sum())

	st.write("### Preview of Medicine Stock Dataset")
	st.dataframe(stock.head(10), use_container_width=True)