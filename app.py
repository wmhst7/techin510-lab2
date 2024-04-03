import streamlit as st
import pandas as pd
import time
from datetime import datetime, timedelta

# Load dataset
cities_df = pd.read_csv("my_dataset.csv")

# Sidebar filter
st.sidebar.title("Filter")
selected_cities = st.sidebar.multiselect("Select cities", cities_df["City"].unique())

# Filter data based on selected cities
if selected_cities:
    filtered_data = cities_df[cities_df["City"].isin(selected_cities)]
else:
    filtered_data = cities_df.copy()

# Show real-time clock
st.subheader("Real-time Clock")

def update_clock():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.markdown(f"Current Time (UTC): {current_time}")

cols = []

# Show city clocks and UNIX timestamps
if selected_cities:
    st.subheader("City Clocks")
    cols = st.columns(len(selected_cities))

    for i, city in enumerate(selected_cities):
        with cols[i]:
            city_data = filtered_data[filtered_data["City"] == city]
            timezone_offset = city_data["TimeZone"].values[0]

            def update_city_clock():
                utc_time = datetime.utcnow()
                city_time = utc_time + timedelta(hours=int(timezone_offset[:3]), minutes=int(timezone_offset[4:]))
                city_time_str = city_time.strftime("%Y-%m-%d %H:%M:%S")
                unix_timestamp = int(time.time())
                st.markdown(f"{city} Time: {city_time_str}")
                st.markdown(f"UNIX Timestamp: {unix_timestamp}")

            update_city_clock()

for i in range(1):
    time.sleep(1)
    update_clock()
    for city_clock in cols:
        city_clock.update_city_clock()
    st.experimental_rerun()