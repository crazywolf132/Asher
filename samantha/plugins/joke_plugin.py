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
        self.the_command = ['joke']

    def action(self, command, statement, sam):
        sam_print(sam, 'What do you call a blonde who died their hair brown?')
        sleep(0.3)
        sam_print(sam, 'Artificial Inteligence!')
