from tests.base_case import SamanthaTestCase
from samantha.adapters.logic import LogicAdapter
from samantha.conversation import Statement
from samantha.training.trainers import ListTrainer
import os


class DummyMutatorLogicAdapter(LogicAdapter):
    """
    This is a dummy class designed to modify a
    the resulting statement before it is returned.
    """

    def process(self, statement):
        statement.add_extra_data("pos_tags", "NN")

        self.context.storage.update(statement)

        return 1, statement


class DataCachingTests(SamanthaTestCase):

    def setUp(self):
        super(DataCachingTests, self).setUp()

        self.Samantha.logic = DummyMutatorLogicAdapter()
        self.Samantha.logic.set_context(self.Samantha)

        self.Samantha.set_trainer(ListTrainer)

        self.Samantha.train([
            "Hello",
            "How are you?"
        ])

    def test_additional_attributes_saved(self):
        """
        Test that an additional data attribute can be added to the statement
        and that this attribute is saved.
        """
        response = self.Samantha.get_response("Hello")
        found_statement = self.Samantha.storage.find("Hello")

        self.assertIsNotNone(found_statement)
        self.assertIn("pos_tags", found_statement.serialize())
        self.assertEqual(
            "NN",
            found_statement.serialize()["pos_tags"]
        )

