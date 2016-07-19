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
        self.the_command = ['download']

    def action(self, command, statement, sam):
        sam_print(sam, 'I see you want to download some new plugins...')
        sam_print(sam, 'Going to download all the plugins that the Developers have made.')
        system('')
        sam_print(sam, '')
        system('')
        sam_print(sam, 'Finished.')
        sleep(3)
        sam_print(sam, 'Going to restart system apply all updates.')
