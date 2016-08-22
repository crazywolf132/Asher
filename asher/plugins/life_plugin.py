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
        self.the_command = ['meaning of life']

    def action(self, command, statement, sam):
        messages = ["It's 42, you idiot.",
                    "It's 42. How many times do I have to tell you?",
                    "The oposite of death!"]
        message = random.choice(messages)
        sam_print(sam, message)
