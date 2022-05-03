#!/usr/bin/env python3
'''
File: design_patterns/decorator/star_buzz.py
'''

from espresso import Espresso

beverage = Espresso()
print(beverage.get_description() + ' $' + beverage.cost())
