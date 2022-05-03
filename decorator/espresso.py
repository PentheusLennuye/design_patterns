'''
File: design_patterns/decorator/espresso.py
'''

from beverage import Beverage

class Espresso(Beverage):
    def __init__(self):
        self.description = 'Espresso'

    def cost(self) -> float:
        return 1.99
