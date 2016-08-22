from asher.conversation import Statement
from time import sleep
from os import system, execv
import os
import random
import re
from asher.required.required import *

application = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))+'/application.py'

class Plugin:
    def __init__(self):
        """
        Please leave this here or it will cause errors.
        """
        self.the_command = ['download']

    def action(self, command, statement, ash):
        ash_print(ash, 'I see you want to download some new plugins...')
        ash_print(ash, 'Going to download all the plugins that the Developers have made.')
        system('cd')
        system('cd Asher')
        system('cd Asher/plugins')
        system('clear')
        ash_print(ash, '2')
        system('clear')
        ash_print(ash, 'Finished.')
        sleep(3)
        ash_print(ash, 'Going to restart system apply all updates.')
        execv('/usr/bin/env', ('env', 'python', application, 'Welcome back.'))
