from .base_case import SamanthaTestCase


class ContextTests(SamanthaTestCase):

    def setUp(self):
        super(ContextTests, self).setUp()

    def test_modify_context(self):
        """
        When one adapter changes the context,
        the change should be the same in all
        other adapters.
        """
        self.Samantha.input.context.recent_statements = [5]
        data = self.Samantha.output.context.recent_statements

        self.assertIn(5, data)
