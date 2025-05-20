import requests
import streamlit as st
from config import API_KEY

st.title("🌤️ Weather App")

city = st.text_input("Enter City Name (e.g., London,UK or Delhi,IN):")
city = city.strip().title()

if city:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        st.success(f"✅ Weather in {city}")
        st.write(f"🌡️ Temperature: {data['main']['temp']}°C")
        st.write(f"💧 Humidity: {data['main']['humidity']}%")
        st.write(f"💨 Wind Speed: {data['wind']['speed']} m/s")
        st.write(f"🌥️ Weather: {data['weather'][0]['description'].title()}")
    else:
        st.error(f"❌ City not found. Please check spelling or try format like 'City,CountryCode' (e.g., Paris,FR).")
