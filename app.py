import streamlit as st
import pandas as pd
import plotly.express as px
import time
from datetime import datetime
import pytz

# Load dataset
dataset = pd.read_csv("my_dataset.csv")

# Sidebar filter
st.sidebar.title("Filter")
selected_cities = st.sidebar.multiselect("Select cities", dataset["City"].unique())

# Filter data based on selected cities
if selected_cities:
    filtered_data = dataset[dataset["City"].isin(selected_cities)]
else:
    filtered_data = dataset.copy()

# Show real-time clock
st.subheader("Real-time Clock")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.write(f"Current Time: {current_time}")

# Show city clocks and UNIX timestamps
if selected_cities:
    st.subheader("City Clocks")
    cols = st.columns(len(selected_cities))
    for i, city in enumerate(selected_cities):
        with cols[i]:
            city_data = filtered_data[filtered_data["City"] == city]
            timezone = city_data["Country"].values[0]
            tz = pytz.timezone(pytz.country_timezones[timezone][0])
            city_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
            unix_timestamp = int(time.time())
            st.write(f"{city} Time: {city_time}")
            st.write(f"UNIX Timestamp: {unix_timestamp}")