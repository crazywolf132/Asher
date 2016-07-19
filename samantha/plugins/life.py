from samantha.conversation import Statement
from time import sleep
from os import system
import random
import re
from samantha.required.required import *


class Plugin:
    def __init__(self):
        """
        Please leave this here or it will cause errors.
        """
        self.the_command = ['life']

    def action(self, command, statement, sam):
        messages = ["It's 42, you idiot.",
                    "It's 42. How many times do I have to tell you?"]
        message = random.choice(messages)
        sam_print(sam, message)
