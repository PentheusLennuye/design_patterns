#!/usr/bin/env python3

from weather_data import WeatherData
from current_conditions_display import CurrentConditionsDisplay


weather_data = WeatherData()
current_display = CurrentConditionsDisplay(weather_data)

weather_data.set_measurements(80, 65, 30.4)
