'''
File: design_patterns/observer/current_conditions_display.py
'''

from interfaces import Observer, DisplayElement
from weather_data import WeatherData

class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        super().__init__()
        weather_data.register_observer(self)

    def update(self):
        self.temperature = self.weather_data.get_temperature()
        self.humidity = self.weather_data.get_humidity()
        self.pressure = self.weather_data.get_pressure()
        self.heat_index = self.weather_data.get_heat_index()
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature} F, "
              f"{self.pressure} kPA and {self.humidity}% humidity.")
        print(f"The heat index is {self.heat_index:.2f}")

