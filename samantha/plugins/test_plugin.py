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
        self.the_command = ['test']

    def action(self, command, statement, sam):
        sam_print(sam, 'Please dont think that this file is going to work.')
        system('clear')
        sam_print(sam, 'Going to run an update now.')
        sleep(0.2)
        system('cd')
        system('cd Samantha')
        system('bash update.sh')
        sam_print(sam, 'Update done. Going to restart now.')
        system('bash restart.sh')
