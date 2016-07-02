from samantha import Samantha
from .base_case import SamanthaTestCase


class AdapterValidationTests(SamanthaTestCase):

    def test_invalid_storage_adapter(self):
        with self.assertRaises(Samantha.InvalidAdapterException):
            self.Samantha = Samantha(
                "Test Bot",
                storage_adapter="samantha.adapters.input.TerminalAdapter",
                database=self.database_path
            )

    def test_valid_storage_adapter(self):
        try:
            self.Samantha = Samantha(
                "Test Bot",
                storage_adapter="samantha.adapters.storage.JsonDatabaseAdapter",
                database=self.database_path
            )
        except Samantha.InvalidAdapterException:
            self.fail("Test raised InvalidAdapterException unexpectedly!")

    def test_invalid_input_adapter(self):
        with self.assertRaises(Samantha.InvalidAdapterException):
            self.Samantha = Samantha(
                "Test Bot",
                input_adapter="samantha.adapters.storage.JsonDatabaseAdapter",
                database=self.database_path
            )

    def test_valid_input_adapter(self):
        try:
            self.Samantha = Samantha(
                "Test Bot",
                input_adapter="samantha.adapters.input.TerminalAdapter",
                database=self.database_path
            )
        except Samantha.InvalidAdapterException:
            self.fail("Test raised InvalidAdapterException unexpectedly!")

    def test_invalid_output_adapter(self):
        with self.assertRaises(Samantha.InvalidAdapterException):
            self.Samantha = Samantha(
                "Test Bot",
                output_adapter="samantha.adapters.input.TerminalAdapter",
                database=self.database_path
            )

    def test_valid_output_adapter(self):
        try:
            self.Samantha = Samantha(
                "Test Bot",
                output_adapter="samantha.adapters.output.TerminalAdapter",
                database=self.database_path
            )
        except Samantha.InvalidAdapterException:
            self.fail("Test raised InvalidAdapterException unexpectedly!")

    def test_invalid_logic_adapter(self):
        with self.assertRaises(Samantha.InvalidAdapterException):
            self.Samantha = Samantha(
                "Test Bot",
                logic_adapters=[
                    "samantha.adapters.input.TerminalAdapter",
                ],
                database=self.database_path
            )

    def test_valid_logic_adapter(self):
        try:
            self.Samantha = Samantha(
                "Test Bot",
                logic_adapters=[
                    "samantha.adapters.logic.ClosestMatchAdapter"
                ],
                database=self.database_path
            )
        except Samantha.InvalidAdapterException:
            self.fail("Test raised InvalidAdapterException unexpectedly!")


class MultiAdapterTests(SamanthaTestCase):

    def test_add_logic_adapter(self):
        count_before = len(self.Samantha.logic.adapters)

        self.Samantha.add_adapter(
            "samantha.adapters.logic.ClosestMatchAdapter"
        )
        self.assertEqual(len(self.Samantha.logic.adapters), count_before + 1)
