from samantha import Samantha

class run():
   def startmain(self):
      # Create a new instance of Samantha
      bot = Samantha("Samantha",
          storage_adapter="samantha.adapters.storage.JsonDatabaseAdapter",
            logic_adapters=[
                "samantha.adapters.logic.ClosestMatchAdapter"
            ],
            input_adapter="samantha.adapters.input.VariableInputTypeAdapter",
            output_adapter="samantha.adapters.output.OutputFormatAdapter",
            database="./database.db"
      )

      print("Type something to begin...")

      # The following loop will execute each time the user enters input
      while True:
          try:
              # We pass None to this method because the parameter
              # is not used by the TerminalAdapter
              bot_input = bot.get_response(None)

          # Press ctrl-c or ctrl-d on the keyboard to exit
          except (KeyboardInterrupt, EOFError, SystemExit):
              break