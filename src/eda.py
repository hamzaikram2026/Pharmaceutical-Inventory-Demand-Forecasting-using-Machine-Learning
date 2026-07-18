
import plotly.express as px
import streamlit as st

def show_eda(stock):

    medicine_counts = (
        stock["Medicine_Name"]
        .value_counts()
        .head(10)
    )

    fig = px.bar(
        x=medicine_counts.index,
        y=medicine_counts.values,
        labels={
            "x": "Medicine",
            "y": "Number of Records"
        },
        title="Top 10 Medicines in Dataset"
    )

    st.plotly_chart(fig, use_container_width=True)

    state_counts = stock["State"].value_counts()

    fig = px.bar(
        x=state_counts.index,
        y=state_counts.values,
        title="Records by State",
        labels={
            "x": "State",
            "y": "Records"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

    facility_counts = stock["Facility_Type"].value_counts()

    fig = px.pie(
        values=facility_counts.values,
        names=facility_counts.index,
        title="Facility Type Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "This chart shows how medicine records are distributed across different states. "
        "It helps identify whether the dataset is balanced geographically."
    )


    st.subheader("Monthly Medicine Consumption")

    month_order = [
        "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    ]

    monthly = (
        stock.groupby("Month")["Consumption"]
        .sum()
        .reindex(month_order)
    )

    fig = px.line(
        x=monthly.index,
        y=monthly.values,
        markers=True,
        title="Monthly Medicine Consumption"
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Total Consumption"
    )

    st.plotly_chart(fig, use_container_width=True)


    st.subheader("Top Healthcare Facilities")

    facility = (
        stock.groupby("Facility_Name")["Consumption"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig = px.bar(
        x=facility.values,
        y=facility.index,
        orientation="h",
        title="Top 10 Facilities by Consumption"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Top Medicines by Consumption")

    medicine = (
        stock.groupby("Medicine_Name")["Consumption"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig = px.bar(
        x=medicine.index,
        y=medicine.values,
        title="Top Medicines by Consumption"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Closing Stock Distribution")

    fig = px.histogram(
        stock,
        x="Closing_Stock",
        nbins=30,
        title="Distribution of Closing Stock"
    )

    st.plotly_chart(fig, use_container_width=True)