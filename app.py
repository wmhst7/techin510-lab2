import streamlit as st
import pandas as pd
import plotly.express as px
import time
from datetime import datetime

# Title and Introduction
st.title("Data Visualization Dashboard")
st.write("This app allows you to explore and visualize a dataset using various charts and filters.")

# Load dataset
dataset = pd.read_csv("your_dataset.csv")

# Sidebar filters
st.sidebar.title("Filters")
selected_columns = st.sidebar.multiselect("Select columns to display", dataset.columns)

# Filter data based on selected columns
filtered_data = dataset[selected_columns]

# Display data
st.write("Filtered Data:")
st.write(filtered_data)

# Charts
st.subheader("Visualizations")

# Line chart
st.subheader("Line Chart")
selected_line_columns = st.multiselect("Select columns for line chart", filtered_data.columns)
if selected_line_columns:
    line_chart = px.line(filtered_data, x=filtered_data.columns[0], y=selected_line_columns)
    st.plotly_chart(line_chart)

# Bar chart
st.subheader("Bar Chart")
selected_bar_column = st.selectbox("Select column for bar chart", filtered_data.columns)
bar_chart = px.bar(filtered_data, x=filtered_data.columns[0], y=selected_bar_column)
st.plotly_chart(bar_chart)

# Map
st.subheader("Map")
if "latitude" in filtered_data.columns and "longitude" in filtered_data.columns:
    map_chart = px.scatter_mapbox(filtered_data, lat="latitude", lon="longitude", zoom=3)
    st.plotly_chart(map_chart)

# Optional Lab: World Clock
st.sidebar.subheader("World Clock")
cities = st.sidebar.multiselect("Select cities", ["New York", "London", "Tokyo", "Sydney"])

def get_current_time(city):
    timezone_map = {
        "New York": "America/New_York",
        "London": "Europe/London",
        "Tokyo": "Asia/Tokyo",
        "Sydney": "Australia/Sydney",
    }
    tz = pytz.timezone(timezone_map[city])
    return datetime.now(tz).strftime("%H:%M:%S")

if cities:
    st.subheader("World Clock")
    cols = st.columns(len(cities))
    for i, city in enumerate(cities):
        with cols[i]:
            st.write(f"{city} Time:")
            current_time = get_current_time(city)
            st.write(current_time)

# Bonus: UNIX Timestamp
st.sidebar.subheader("UNIX Timestamp")
st.write("Current UNIX Timestamp:")
unix_timestamp = int(time.time())
st.write(unix_timestamp)

st.sidebar.subheader("Convert UNIX Timestamp")
input_timestamp = st.sidebar.number_input("Enter UNIX Timestamp")
if input_timestamp:
    converted_time = datetime.fromtimestamp(input_timestamp).strftime("%Y-%m-%d %H:%M:%S")
    st.sidebar.write(f"Human-readable Time: {converted_time}")