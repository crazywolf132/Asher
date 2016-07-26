from samantha.conversation import Statement
from time import sleep
from os import system, listdir
import random
import re
import os
from samantha.required.required import *
from subprocess import check_output


class Plugin:
    def __init__(self):
        """
        Please leave this here or it will cause errors.
        """
        self.the_command = ['push', 'all']

    def action(self, command, statement, sam):
        sam_print(sam, "Please wait a moment.")
        system('rm -rf push.sh')
        system('curl -L "https://raw.githubusercontent.com/crazywolf132/Ai-Setup/master/push-all.sh" > push.sh')
        system('bash push.sh')
        system('clear')
        sam_print(sam, "Finished sir.")
