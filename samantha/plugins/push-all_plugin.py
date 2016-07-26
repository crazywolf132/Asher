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
        system('cd ~/')
        system('cd ~/projects')
        a = check_output('ls').split()
        for folder in a:
            system('cd ' + folder)
            system('git pull')
            system('git add .')
            system('git commit -m "Pushed by SAMANTHA!"')
            system('git push')
            system('cd ..')
