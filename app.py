import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
import pytz
import time

cities_data = pd.read_csv("cities.csv")

st.set_page_config(page_title="World Clock App", layout="wide")

st.sidebar.title("Filters")
selected_countries = st.sidebar.multiselect("Select Countries", cities_data["Country"].unique())

filtered_data = cities_data[cities_data["Country"].isin(selected_countries)] if selected_countries else cities_data

st.title("World Clock App")

selected_cities = st.multiselect("Select Cities for World Clock", filtered_data["City"])

if selected_cities:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Current Time")
        while True:
            for city in selected_cities:
                timezone = filtered_data[filtered_data["City"] == city]["TimeZone"].values[0]
                current_time = datetime.datetime.now(pytz.timezone(timezone))
                unix_timestamp = int(current_time.timestamp())
                formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                st.write(f"{city}: {formatted_time} (UNIX: {unix_timestamp})")
            time.sleep(1)
            st.rerun()

st.subheader("Data Visualization")

city_counts = filtered_data["Country"].value_counts()
fig_bar = px.bar(city_counts, x=city_counts.index, y=city_counts.values, labels={"x": "Country", "y": "Number of Cities"})
st.plotly_chart(fig_bar)

fig_map = px.scatter_geo(filtered_data, lat=filtered_data["City"].apply(lambda x: 0), lon=filtered_data["City"].apply(lambda x: 0),
                         hover_name="City", color="Country", projection="natural earth")
st.plotly_chart(fig_map)
