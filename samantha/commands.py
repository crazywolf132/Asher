from .conversation import Statement
from time import sleep
from os import system

IS_COMMAND = True
NOT_COMMAND = False

class Command:
    """
    A simple class to load all the commands that the user
    can use with Samantha.
    """
    def process_input(self, statement, sam):
        input_statement = sam.get_last_input_statement()
        i_s = input_statement
        sam_print = lambda x: sam.output.process_response(Statement(x))
        if statement == 'clear':
            system('clear')
            sam_print('Ok, all done.')
            return IS_COMMAND
        elif statement == 'quit':
            sam_print('Killing myself.')
            sam_print('See you next time.')
            exit()
            return IS_COMMAND
        elif statement == 'end':
            sam_print('Killing myself.')
            sam_print('See you next time.')
            exit()
            return IS_COMMAND
        elif statement == 'shutdown':
            sam_print('Shutting down now.')
            sam_print('See you next time.')
            system('sudo shutdown -h now')
            return IS_COMMAND
        elif statement == 'tell me a joke':
            sam_print('Why did hitler kill himself?')
            sleep (3)
            sam_print('He saw his gas bill!')
            return IS_COMMAND
        elif statement == 'on':
            sam_print('Im already on silly.')
            return IS_COMMAND
        elif statement == 'off':
            sam_print('Turning off.')
            #.. We need to make a stop listening to everything apart from on.
            return IS_COMMAND
        elif statement == 'mirror on':
            sam_print('Turning mirror on.')
            #.. Smart mirror command to turn it on.
            sam_print('Mirror is on.')
            return IS_COMMAND
        elif statement == 'update':
            sam_print('Going to pause the system to run the update.')
            sam_print('Please hold.')
            system('cd')
            system('cd Samantha')
            system('bash update.sh')
            sam_print('Should be done. Feel free t test out my new knollege base.')
            sleep (0.2)
            sam_print('If i was updated...')
            return IS_COMMAND
        return NOT_COMMAND
