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

    def action(self, command, statement, sam):
        sam_print(sam, 'I see you want to download some new plugins...')
        sam_print(sam, 'Going to download all the plugins that the Developers have made.')
        system('cd')
        system('cd Asher')
        system('cd Asher/plugins')
        system('clear')
        sam_print(sam, '2')
        system('clear')
        sam_print(sam, 'Finished.')
        sleep(3)
        sam_print(sam, 'Going to restart system apply all updates.')
        execv('/usr/bin/env', ('env', 'python', application, 'Welcome back.'))
