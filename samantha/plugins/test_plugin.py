from samantha.conversation import Statement
from time import sleep
from os import system
import random
import os
import re
from samantha.required.required import *

application = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))+'/application.py'

class Plugin:
    def __init__(self):
        """
        Please leave this here or it will cause errors.
        """
        self.the_command = ['test']

    def action(self, command, statement, sam):
        sam_print(sam, 'Please dont think that this file is going to work.')
        system('clear')
        import urllib
        try :
            stri = "https://8.8.8.8/"
            data = urllib.urlopen(stri)
            sam_print(sam, 'Going to run an update now.')
            sleep(0.2)
            system('cd ~/')
            system('curl -L "https://raw.githubusercontent.com/crazywolf132/Ai-Setup/72f29e63108f40f052e95a1f87f7f94efef023a2/Update.sh" > update.sh')
            system('bash update.sh')
            sleep(3)
            system('clear')
            sam_print(sam, 'Going to restart system apply all updates.')
            execv('/usr/bin/env', ('env', 'python', application, 'All done.'))
        except e:
            sam_print(sam, 'Please connect to the internet to download any updates.')
