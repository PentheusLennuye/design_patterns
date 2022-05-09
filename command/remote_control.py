'''
File: design_patterns/command/remote_control.py
'''

from command import Command, NoCommand

class RemoteControl:
    '''This is the INVOKER'''
    def __init__(self):
        no_command = NoCommand()
        self.on_commands = [no_command] * 7  # Array of length 7
        self.off_commands = [no_command] * 7

    def set_command(
        self, slot: int, on_command: Command, off_command: Command
    ):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: int):
        self.on_commands[slot].execute()

    def off_button_was_pushed(self, slot: int):
        self.off_commands[slot].execute()

