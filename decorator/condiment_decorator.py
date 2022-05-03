'''
File: design_patterns/decorator/condiment_decorator.py
'''

from beverage import Beverage


class CondimentDecorator(Beverage):  # extension
    def __init__(self):
        self.beverage = None
        super().__init__()

    def get_description(self):
        raise NotImplementedError


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Mocha'

    def cost(self) -> float:
        return self.beverage.cost() + 0.20


class Soya(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Soya'

    def cost(self) -> float:
        return self.beverage.cost() + 0.15


class Whip(CondimentDecorator):
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Whip'

    def cost(self) -> float:
        return self.beverage.cost() + 0.10
