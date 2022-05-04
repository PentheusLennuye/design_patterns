'''
File: design_patterns/factory/pizza.py
'''

from abc import ABC, abstractmethod


class Pizza(ABC):
    '''The "Product" class and subclasses'''
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = []

    def prepare(self):
        print(f"Preparing {self.name}")
        print('Tossing dough ...')
        print('Adding sauce ...')
        print('Adding toppings: ', ', '.join(self.toppings))

    @staticmethod
    def bake():
        print('Bake for 25 minutes at 350°F')

    @staticmethod
    def cut():
        print('Cutting the pizza into diagonal slices')

    @staticmethod
    def cut():
        print('Cutting the pizza into diagonal slices')

    @staticmethod
    def box():
        print('Placing the pizza in the official PizzaStore box')
    
    def get_name(self):
        return self.name


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'NY Style Sauce and Cheese Pizza'
        self.dough = 'Thin Crust Dough'
        self.sauce = 'Marinara Sauce'

        self.toppings.append('Grated Reggiano Cheese')


class NYStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'NY Style Veggie Pizza'
        self.dough = 'Thin Crust Dough'
        self.sauce = 'Marinara Sauce'

        self.toppings.append('Mushrooms Broccoli Onions Tomatoes'.split())


class NYStyleClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'NY Style Clam Pizza'
        self.dough = 'Thin Crust Dough'
        self.sauce = 'Marinara Sauce'

        self.toppings.append('Mozzarella Clams Capers'.split())


class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'NY Style Pepperoni Pizza'
        self.dough = 'Thin Crust Dough'
        self.sauce = 'Marinara Sauce'

        self.toppings.append('Mozzarella Clams Capers'.split())


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'Chicago Style Deep Dish Cheese Pizza'
        self.dough = 'Extra Thick Crust Dough'
        self.sauce = 'Plum Tomato Sauce'

        self.toppings.append('Shredded Mozzarella Cheese')

    @staticmethod
    def cut():
        print('Cutting the pizza into square slices')


class ChicagoStyleVeggiePizza(Pizza):
    pass


class ChicagoStyleClamPizza(Pizza):
    pass


class ChicagoStylePepperoniPizza(Pizza):
    pass

