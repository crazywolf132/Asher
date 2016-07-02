from tests.base_case import SamanthaTestCase
from samantha import Samantha
from samantha.training.trainers import ListTrainer


class TrainingTests(SamanthaTestCase):

    def test_trainer_not_set(self):
        with self.assertRaises(Samantha.TrainerInitializationException):
            self.Samantha.train()
