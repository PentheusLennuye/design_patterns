#!/usr/bin/env python3
'''
File: design_patterns/command/test.py
'''

from simple_remote_control import SimpleRemoteControl
from light import Light, LightOnCommand
from garage import GarageDoor, GarageDoorOpenCommand

remote = SimpleRemoteControl()
light = Light()
light_on = LightOnCommand(light)
remote.set_command(light_on)
remote.button_was_pressed()

garage_door = GarageDoor()
garage_door_open = GarageDoorOpenCommand(garage_door)
remote.set_command(garage_door_open)
remote.button_was_pressed()

