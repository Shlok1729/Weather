import streamlit as st
import requests
from dotenv import load_dotenv
import os
load_dotenv()

# Get the API key
api_key = os.getenv("OPENWEATHER_API_KEY")

# Function to fetch weather data
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit UI
st.title("🌤️ Real-Time Weather App")
st.write("Enter a city name to get the current weather information.")

city = st.text_input("City Name", "Mumbai")

if st.button("Get Weather"):
    data = get_weather(city)

    if data:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']
        wind = data['wind']['speed']

        st.subheader(f"Weather in {city.title()}")
        st.write(f"🌡️ Temperature: {temp}°C")
        st.write(f"💧 Humidity: {humidity}%")
        st.write(f"🌥️ Condition: {condition.title()}")
        st.write(f"💨 Wind Speed: {wind} m/s")
    else:
        st.error("City not found or API error.")
