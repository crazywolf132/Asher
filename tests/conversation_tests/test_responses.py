from unittest import TestCase
from samantha.conversation import Response


class ResponseTests(TestCase):

    def setUp(self):
        self.response = Response("A test response.")

