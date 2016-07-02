from samantha.adapters.input import InputAdapter
from samantha.conversation import Statement
from samantha.utils.read_input import input_function


class TerminalAdapter(InputAdapter):
    """
    A simple adapter that allows Samantha to
    communicate through the terminal.
    """

    def process_input(self, *args, **kwargs):
        """
        Read the user's input from the terminal.
        """
        user_input = input_function()
        return Statement(user_input)
