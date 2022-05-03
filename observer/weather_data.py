'''
File: design_patterns/observer/weather_data.py

Weather Data class as a demo
'''

from interfaces import Subject, Observer


class WeatherData(Subject):
    '''Subject in the OBSERVER pattern'''

    def __init__(self):
        self.observers = []
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.heat_index = None

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure

    def get_heat_index(self):
        return self.heat_index

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(o)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.__compute_heat_index()
        self.measurements_changed()

    def __compute_heat_index(self):
        t = self.temperature
        rh = self.humidity  # rh = "relative humidity"
        i = ((16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh) + \
        (0.00941695 * (t * t)) + (0.00728898 * (rh * rh)) + \
        (0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) + \
        (0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 * \
        (rh * rh * rh)) + (0.00000142721 * (t * t * t * rh)) + \
        (0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) + \
        0.000000000843296 * (t * t * rh * rh * rh)) - \
        (0.0000000000481975 * (t * t * t * rh * rh * rh)))
        self.heat_index = i

