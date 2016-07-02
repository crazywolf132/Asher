from unittest import TestCase
from samantha.adapters.output import Mailgun


class MailgunAdapterTestCase(TestCase):

    def setUp(self):
        super(MailgunAdapterTestCase, self).setUp()
        self.adapter = Mailgun()
