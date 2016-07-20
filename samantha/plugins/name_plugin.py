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
        self.the_command = ['what is my name']

    def action(self, command, statement, sam):
        name = 'dick head'
        sam_print(sam, 'Your name is... ' + name)
