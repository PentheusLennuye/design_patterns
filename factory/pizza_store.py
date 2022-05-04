'''
File: design_patterns/factory/pizza_store.py
'''

from abc import ABC, abstractmethod

import pizza


class PizzaStore(ABC):
    '''Abstract class setting up Factory Method Pattern'''
    def order_pizza(self, pizza_type: str) -> pizza.Pizza:
        pizza = self._create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def _create_pizza(self, pizza_type: str):
        pass


class NYPizzaStore(PizzaStore):
    def _create_pizza(self, pizza_type: str) -> pizza.Pizza:
        jump_table = {
            'cheese': pizza.NYStyleCheesePizza,
            'veggie': pizza.NYStyleVeggiePizza,
            'clam': pizza.NYStyleClamPizza,
            'pepperoni': pizza.NYStylePepperoniPizza
        }
        if pizza_type in jump_table:
            return jump_table[pizza_type]()
        return None


class ChicagoPizzaStore(PizzaStore):
    def _create_pizza(self, pizza_type: str) -> pizza.Pizza:
        jump_table = {
            'cheese': pizza.ChicagoStyleCheesePizza,
            'veggie': pizza.ChicagoStyleVeggiePizza,
            'clam': pizza.ChicagoStyleClamPizza,
            'pepperoni': pizza.ChicagoStylePepperoniPizza
        }
        if pizza_type in jump_table:
            return jump_table[pizza_type]()
        return None


class CaliforniaPizzaStore(PizzaStore):
    def _create_pizza(self, pizza_type: str) -> pizza.Pizza:
        jump_table = {
            'cheese': pizza.CaliforniaStyleCheesePizza,
            'veggie': pizza.CaliforniaStyleVeggiePizza,
            'clam': pizza.CaliforniaStyleClamPizza,
            'pepperoni': pizza.CaliforniaStylePepperoniPizza
        }
        if pizza_type in jump_table:
            return jump_table[pizza_type]()
        return None

