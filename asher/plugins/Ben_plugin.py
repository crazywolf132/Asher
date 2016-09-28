from asher.conversation import Statement
from time import sleep
from os import system
import random
import re
from asher.required.required import *


class Plugin:
    def __init__(self):
        """
        Please leave this here or it will cause errors.
        """
        self.the_command = ['Help me']

    def action(self, command, statement, ash):
        ash_print(ash, 'How, I am only an AI')
