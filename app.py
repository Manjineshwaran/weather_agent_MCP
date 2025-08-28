import streamlit as st
from weather_agent import get_weather_data
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Simple UI
st.title("🌤️ Weather App")
city = st.text_input("Enter city name:")

if st.button("Get Weather", key="get_weather_btn"):
    if city:
        try:
            result = get_weather_data(city)
            st.write("### Weather in", city)
            st.write(result)
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a city name")
