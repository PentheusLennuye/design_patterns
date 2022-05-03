'''
File: design_patterns/observer/beverage.py
'''


class Beverage:
    def __init__(self):
        self.description = None

    def get_description(self):
        return self.description

    def cost(self):
        raise NotImplementedError
