'''
File: design_patterns/command/garage.py
'''
 
from command import Command


class GarageDoor:
    def up(self):
        print("Garage door opened")

    def down(self):
        print("Garage door closed")

    def stop(self):
        print("Garage door stop in place")

    def light_on(self):
        print("Garage door light on")

    def light_off(self):
        print("Garage door light off")


class GarageDoorOpenCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()
