from unittest import TestCase
from samantha import Samantha
import os


class SamanthaTestCase(TestCase):

    def setUp(self):
        self.test_data_directory = 'test_data'
        self.test_database_name = self.random_string() + ".db"

        if not os.path.exists(self.test_data_directory):
            os.makedirs(self.test_data_directory)

        self.database_path = os.path.join(
            self.test_data_directory,
            self.test_database_name
        )

        self.Samantha = Samantha(
            "Test Bot",
            input_adapter="samantha.adapters.input.VariableInputTypeAdapter",
            output_adapter="samantha.adapters.output.OutputFormatAdapter",
            output_format='text',
            database=self.database_path
        )

    def random_string(self, start=0, end=9000):
        """
        Generate a string based on a random number.
        """
        from random import randint
        return str(randint(start, end))

    def remove_test_data(self):
        import shutil

        if os.path.exists(self.test_data_directory):
            shutil.rmtree(self.test_data_directory)

    def tearDown(self):
        """
        Remove the test database.
        """
        self.Samantha.storage.drop()
        self.remove_test_data()

