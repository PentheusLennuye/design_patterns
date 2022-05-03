'''
File: design_patterns/decorator/decaf.py
'''

from beverage import Beverage

class Decaf(Beverage):
    def __init__(self):
        self.description = 'Decaf Coffee'

    def cost(self) -> float:
        return 1.05 
