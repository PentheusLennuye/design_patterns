'''
File: design_patterns/decorator/dark_roast.py
'''

from beverage import Beverage

class DarkRoast(Beverage):
    def __init__(self):
        self.description = 'Dark Roast Coffee'

    def cost(self) -> float:
        return 0.99
