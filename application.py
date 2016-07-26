from samantha import Samantha
from sys import argv
import random

messages = ['\033[1;31m',
            '\033[1;32m',
            '\033[1;33m',
            '\033[1;34m',
            '\033[1;35m',
            '\033[1;36m']
message = random.choice(messages)

# Create a new instance of the AI
bot = Samantha("No Output",
        storage_adapter="samantha.adapters.storage.JsonDatabaseAdapter",
        logic_adapters=[
            "samantha.adapters.logic.ClosestMatchAdapter"
        ],
        input_adapter="samantha.adapters.input.TerminalAdapter",
        output_adapter="samantha.adapters.output.TerminalAdapter",
        database="./Ai-DB/database.db"
    )


print(message + "Type something to begin...\033[0m")

if len(argv) >= 2:
    print argv[1]

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter

        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
