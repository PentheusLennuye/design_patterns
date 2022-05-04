'''
File: design_patterns/factory/ingredients.py
'''

from abc import ABCMeta, abstractmethod

class Garlic:
    pass


class Onion:
    pass


class Mushroom:
    pass


class RedPepper:
    pass


class Spinach:
    pass


class Eggplant:
    pass


class BlackOlives:
    pass


class SlicedPepperoni:
    pass


class MarinaraSauce:
    pass


class PlumTomatoSauce:
    pass


class FreshClams:
    pass


class FrozenClams:
    pass


class ReggianoCheese:
    pass


class MozzarellaCheese:
    pass


class ThickCrustDough:
    pass


class ThinCrustDough:
    pass


class PizzaIngredientFactory(metaclass=ABCMeta):  # interface
    '''Demonstrates the ABSTRACT FACTORY'''
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'create_dough') and
                callable(subclass.create_dough) and
                hasattr(subclass, 'create_sauce') and
                callable(subclass.create_sauce) and
                hasattr(subclass, 'create_cheese') and
                callable(subclass.create_cheese) and
                hasattr(subclass, 'create_veggies') and
                callable(subclass.create_veggies) and
                hasattr(subclass, 'create_pepperoni') and
                callable(subclass.create_pepperoni) and
                hasattr(subclass, 'create_clam') and
                callable(subclass.create_clam) or
                NotImplemented)

    @abstractmethod
    def create_dough(self):
        raise NotImplementedError

    @abstractmethod
    def create_sauce(self):
        raise NotImplementedError

    @abstractmethod
    def create_cheese(self):
        raise NotImplementedError

    @abstractmethod
    def create_veggies(self):
        raise NotImplementedError

    @abstractmethod
    def create_pepperoni(self):
        raise NotImplementedError

    @abstractmethod
    def create_clam(self):
        raise NotImplementedError


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    @staticmethod
    def create_dough():
        return ThinCrustDough()

    @staticmethod
    def create_sauce():
        return MarinaraSauce()

    @staticmethod
    def create_cheese():
        return ReggianoCheese()

    @staticmethod
    def create_veggies():
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    @staticmethod
    def create_pepperoni():
        return SlicedPepperoni()

    @staticmethod
    def create_clam():
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    @staticmethod
    def create_dough():
        return ThickCrustDough()

    @staticmethod
    def create_sauce():
        return PlumTomatoSauce()

    @staticmethod
    def create_cheese():
        return MozzarellaCheese()

    @staticmethod
    def create_veggies():
        return [BlackOlives(), Eggplant(), Spinach()]

    @staticmethod
    def create_pepperoni():
        return SlicedPepperoni()

    @staticmethod
    def create_clam():
        return FrozenClams()


if __name__ == '__main__':
    n = NYPizzaIngredientFactory()
    c = ChicagoPizzaIngredientFactory()
