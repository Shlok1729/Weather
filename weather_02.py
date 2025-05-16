import requests
import tkinter as tk
from tkinter import messagebox

from dotenv import load_dotenv
import os
load_dotenv()

# Get the API key
api_key = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if response.status_code == 200:
            city_name = data["name"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"].title()
            
            result = f"City: {city_name}\nTemperature: {temp} °C\nHumidity: {humidity}%\nCondition: {description}"
            result_label.config(text=result)
        else:
            message = data.get("message", "City not found.")
            messagebox.showerror("API Error", message)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch data: {e}")

# Tkinter UI
root = tk.Tk()
root.title("🌦️ Weather App")
root.geometry("350x300")

title_label = tk.Label(root, text="Check Weather", font=("Arial", 16))
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14), width=25)
city_entry.insert(0, "e.g. Mumbai,IN")
city_entry.pack(pady=5)

search_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12))
search_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

root.mainloop()
