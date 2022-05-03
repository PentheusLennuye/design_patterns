#!/usr/bin/env python3
'''
File: design_patterns/decorator/star_buzz.py
'''

from beverage import Espresso, DarkRoast, HouseBlend
from condiment_decorator import Mocha, Whip, Soya

beverage = Espresso()
print("{} ${:.2f}".format(beverage.get_description(), beverage.cost()))

# Double mocha + whip
beverage2 = DarkRoast()
beverage2 = Mocha(beverage2)
beverage2 = Mocha(beverage2)
beverage2 = Whip(beverage2)
print("{} ${:.2f}".format(beverage2.get_description(), beverage2.cost()))

# Soya, mocha + whip
beverage3 = HouseBlend()
beverage3 = Soya(beverage3)
beverage3 = Mocha(beverage3)
beverage3 = Whip(beverage3)
print("{} ${:.2f}".format(beverage3.get_description(), beverage3.cost()))

