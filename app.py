import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
import pytz

# Read the cities data from CSV
cities_data = pd.read_csv("cities.csv")

# Set page title and layout
st.set_page_config(page_title="World Clock App", layout="wide")

# Sidebar filters
st.sidebar.title("Filters")
selected_countries = st.sidebar.multiselect("Select Countries", cities_data["Country"].unique())

# Filter data based on selected countries
filtered_data = cities_data[cities_data["Country"].isin(selected_countries)] if selected_countries else cities_data

# Main content
st.title("World Clock App")

# City selection for world clock
selected_cities = st.multiselect("Select Cities for World Clock", filtered_data["City"])

# World clock
if selected_cities:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Current Time")
        for city in selected_cities:
            timezone = filtered_data[filtered_data["City"] == city]["TimeZone"].values[0]
            current_time = datetime.datetime.now(pytz.timezone(timezone)).strftime("%Y-%m-%d %H:%M:%S")
            st.write(f"{city}: {current_time}")
    
    with col2:
        st.subheader("UNIX Timestamp")
        unix_timestamp = int(datetime.datetime.now().timestamp())
        st.write(f"UNIX Timestamp: {unix_timestamp}")

# Data visualization
st.subheader("Data Visualization")

# Bar chart of cities by country
city_counts = filtered_data["Country"].value_counts()
fig_bar = px.bar(city_counts, x=city_counts.index, y=city_counts.values, labels={"x": "Country", "y": "Number of Cities"})
st.plotly_chart(fig_bar)

# Map of cities
fig_map = px.scatter_geo(filtered_data, lat=filtered_data["City"].apply(lambda x: 0), lon=filtered_data["City"].apply(lambda x: 0),
                         hover_name="City", color="Country", projection="natural earth")
st.plotly_chart(fig_map)