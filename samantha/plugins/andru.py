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
        self.the_command = ['who are you', 'help', '?']

    def action(self, command, statement, sam):
        sam_print(sam, 'My name is Andrew. I am here to help and serve you.')
        sleep(1)
        sam_print(sam, 'Feel free to ask me anything. If i do not know it, I will learn it.')
