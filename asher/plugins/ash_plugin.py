from asher.conversation import Statement
from time import sleep
from os import system
import random
import re
from asher.required.required import *


class Plugin:
    def __init__(self):
        """
        Please leave this here or it will cause errors.
        """

        self.who = ['who are you', '?']
        self.help = ['help']
        self.exit = ['exit please', 'quit']
        self.clear = ['clear']
        self.download = ['download plugins']
        self.joke = ['joke']
        self.life = ['meaning of life']
        self.push = ['push', 'all']
        self.turd = ['polish', 'turd']
        self.update = ['update']
        self.name = ['my name']

        self.the_command = self.who + self.help + self.exit + self.clear + self.download + self.joke + self.life + self.push + self.turd + self.update + self.name

    def action(self, command, statement, ash):

        if command in self.who:
            ash_print(ash, 'My name is Andrew. I am here to help and serve you.')
            sleep(1)
            ash_print(ash, 'Feel free to ask me anything. If i do not know it, I will learn it.')
        elif command in self.help:
            ash_print(ash, 'what with?')
        elif command in self.exit:
            ash_print(ash, 'Good bye.')
            exit()
        elif command in self.bye:
            ash_print(ash, 'Good bye.')
            exit()
        elif command in self.clear:
            ash_print(ash, 'Terminal is cleared.')
            system('clear')
        elif command in self.download:
            ash_print(ash, 'Downloading all.')
            sytem('cd ~/')
            ash_print(ash, 'I will restart when done.')
            sytem('bash start.sh download')
        elif command in self.joke:
            ash_print(ash, 'Why did the calf cross the road?')
            sleep(2)
            ash_print(ash, 'To get to the udder side.')
        elif command in self.life:
            messages = ["It's 42, you idiot.",
                        "It's 42. How many times do I have to tell you?",
                        "The oposite of death!"]
            message = random.choice(messages)
            ash_print(ash, message)
        elif command in self.push:
            ash_print(ash, "Please wait a moment.")
            system('rm -rf push.sh')
            system('curl -L "https://raw.githubusercontent.com/crazywolf132/Ai-Setup/master/push-all.sh" > push.sh')
            system('bash push.sh')
            system('clear')
            ash_print(ash, "Finished.")
        elif command in self.turd:
            ash_print(ash, 'You can\'t polish a turd, but you can roll it in glitter!')
        elif command in self.update:
            ash_print(ash, 'Please wait a second.')
            system('cd ~/')
            ash_print(ash, 'When I am done updating, I will restart.')
            system('bash start.sh update')
        elif command in self.name:
            ash_print(ash, "wanker")
