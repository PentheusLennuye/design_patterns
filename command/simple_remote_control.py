'''
File: design_patterns/command/simple_remote_control.py
'''

from command import Command


class SimpleRemoteControl:
    '''In which a command is held in one slot, constrolling one device.'''
    def __init__(self):
        self.slot = None

    def set_command(self, command: Command):
        self.slot = command

    def button_was_pressed(self):
        self.slot.execute()

