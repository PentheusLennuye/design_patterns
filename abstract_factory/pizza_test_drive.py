#!/usr/bin/env python3
'''
File: design_patterns/factory/pizza_test_drive.py
'''


from pizza_store import NYPizzaStore, ChicagoPizzaStore


ny_store = NYPizzaStore()
chicago_store = ChicagoPizzaStore()

pizza = ny_store.order_pizza('cheese')
print('Ethan ordered a', pizza.get_name())

pizza = chicago_store.order_pizza('cheese')
print('Ethan ordered a', pizza.get_name())
