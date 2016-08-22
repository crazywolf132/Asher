from asher.conversation import Statement
from time import sleep
from os import system, listdir
import random
import re
import os
from asher.required.required import *
from subprocess import check_output


class Plugin:
    def __init__(self):
        """
        Please leave this here or it will cause errors.
        """
        self.the_command = ['push', 'all']

    def action(self, command, statement, ash):
        ash_print(ash, "Please wait a moment.")
        system('rm -rf push.sh')
        system('curl -L "https://raw.githubusercontent.com/crazywolf132/Ai-Setup/master/push-all.sh" > push.sh')
        system('bash push.sh')
        system('clear')
        ash_print(ash, "Finished sir.")
