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
        self.the_command = ['motivation']

    def action(self, command, statement, sam):
        messages = ["Think of something in life that could be fixed Now, go out and change it.",
                    "You are 17 year's old... How have you changed the world in this amount of time?",
                    "Failure is just success hideing."]
        message = random.choice(messages)
        sam_print(sam, message)
