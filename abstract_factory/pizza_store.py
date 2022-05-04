'''
File: design_patterns/factory/pizza_store.py
'''

from abc import ABC, abstractmethod

from pizza import Pizza, CheesePizza, VeggiePizza, ClamPizza, PepperoniPizza

from ingredients import NYPizzaIngredientFactory, ChicagoPizzaIngredientFactory

class PizzaStore(ABC):
    '''Abstract class setting up Factory Method Pattern'''
    def order_pizza(self, pizza_type: str) -> Pizza:
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
    def __init__(self):
        self.ingredient_factory = NYPizzaIngredientFactory()

    def _create_pizza(self, pizza_type: str) -> Pizza:
        jump_table = {
            'cheese': CheesePizza,
            'veggie': VeggiePizza,
            'clam': ClamPizza,
            'pepperoni': PepperoniPizza
        }
        if pizza_type in jump_table:
           pizza = jump_table[pizza_type](self.ingredient_factory)
           pizza.set_name('New York Style ' + pizza_type.title() + ' Pizza')
           return pizza
        return None


class ChicagoPizzaStore(PizzaStore):
    def __init__(self):
        self.ingredient_factory = ChicagoPizzaIngredientFactory()

    def _create_pizza(self, pizza_type: str) -> Pizza:
        jump_table = {
            'cheese': CheesePizza,
            'veggie': VeggiePizza,
            'clam': ClamPizza,
            'pepperoni': PepperoniPizza
        }
        if pizza_type in jump_table:
           pizza = jump_table[pizza_type](self.ingredient_factory)
           pizza.set_name('Chicago Style ' + pizza_type.title() + ' Pizza')
           return pizza
        return None

