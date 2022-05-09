'''
File: design_patterns/command/light.py
'''
 
from command import Command


class Light:
    def on(self):
        print("Light on")

    def off(self):
        print("Light off")


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

