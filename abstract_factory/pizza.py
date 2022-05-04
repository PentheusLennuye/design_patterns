'''
File: design_patterns/factory/pizza.py
'''

from abc import ABC, abstractmethod

from ingredients import PizzaIngredientFactory


class Pizza(ABC):  # ABC for Abstract, ABCMeta for Interface
    '''The "Product" class and subclasses'''
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.veggies = []
        self.cheese = None
        self.pepperoni = None
        self.clam = None

    @abstractmethod
    def prepare(self):
        raise NotImplementedError

    @staticmethod
    def bake():
        print('Bake for 25 minutes at 350°F')

    @staticmethod
    def cut():
        print('Cutting the pizza into diagonal slices')

    @staticmethod
    def box():
        print('Placing the pizza in the official PizzaStore box')
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()


class VeggiePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()


class PepperoniPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()


