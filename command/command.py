'''
File: design_patterns/command/command.py
'''

from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):  # interface
    '''Demonstrates the COMMAND pattern'''
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'execute') and
                callable(subclass.execute) and
                hasattr(subclass, 'execute') and
                callable(subclass.execute) or
                NotImplemented)

    @abstractmethod
    def execute(self):
        raise NotImplementedError

    @abstractmethod
    def undo(self):
        raise NotImplementedError


class NoCommand(Command):
    def execute(self):
        pass

