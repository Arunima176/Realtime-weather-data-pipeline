import requests
import pandas as pd
from datetime import datetime
import os

def fetch_weather_data(city, api_key, file_path):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather = {
        'city': [city],
        'temperature': [data['main']['temp']],
        'humidity': [data['main']['humidity']],
        'weather': [data['weather'][0]['main']],
        'description': [data['weather'][0]['description']],
        'datetime': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    }

    df = pd.DataFrame(weather)
    os.makedirs("data", exist_ok=True)
    df.to_csv(file_path, index=False)
    print("✅ Weather data saved to CSV.")

fetch_weather_data("Chennai", "4092d92f7eabc9964f3f4c2c4d41e0bc", "data/weather.csv")

