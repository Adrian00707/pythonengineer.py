import webbrowser
import requests
import yaml
import json
import pandas as pd
from datetime import datetime, timedelta


class Weather:
    def __init__(self, api_key, city):
        self.api_key = api_key
        self.city = city
        self.weather_data = []
        self.df = pd.DataFrame()

    def weather_data(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={
            self.city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            self.weather_data = response.json()
        else:
            print("Error fetching data from API")

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.weather_data, file)

    def load_json(self, filename):
        self.weather_data = json.load(filename)

    def save_yaml(self, filename):
        yaml.dump(self.weather_data, filename)

    def load_yaml(self, filename):
        self.weather_data = yaml.safe_load(filename)

    def save_csv(self, filename):
        self.df.to_csv(filename, index=False)

    def load_csv(self, filename):
        self.df = pd.read_csv(filename)

    def display_weather_data(self):
        print(f"City: {self.weather_data['name']}")
        print(f"Temperature: {self.weather_data['main']['temp']}°C")
        print("Weather: {self.weather_data['weather'][0]['description']}")


def open_url(url):
    webbrowser.open(url)


open_url("https://meta.com")
