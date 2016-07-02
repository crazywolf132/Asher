from tests.base_case import SamanthaTestCase
from samantha.training.trainers import samanthaCorpusTrainer


class samanthaCorpusTrainingTests(SamanthaTestCase):

    def setUp(self):
        super(samanthaCorpusTrainingTests, self).setUp()
        self.Samantha.set_trainer(samanthaCorpusTrainer)

    def test_train_with_english_greeting_corpus(self):
        self.Samantha.train(
            "samantha.corpus.english.greetings"
        )

        statement = self.Samantha.storage.find("Hello")
        self.assertIsNotNone(statement)

    def test_train_with_multiple_corpora(self):
        self.Samantha.train(
            "samantha.corpus.english.greetings",
            "samantha.corpus.english.conversations",
        )

        statement = self.Samantha.storage.find("Hello")
        self.assertIsNotNone(statement)

    def test_train_with_english_corpus(self):
        self.Samantha.train(
            "samantha.corpus.english"
        )

        statement = self.Samantha.storage.find("Hello")
        self.assertIsNotNone(statement)

