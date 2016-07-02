from tests.base_case import SamanthaTestCase
from .base import StorageIntegrationTests
from samantha.adapters.storage import JsonDatabaseAdapter


class JsonStorageIntegrationTests(StorageIntegrationTests, SamanthaTestCase):

    def setUp(self):
        super(JsonStorageIntegrationTests, self).setUp()

        self.Samantha.storage_adapters = []
        self.Samantha.storage = JsonDatabaseAdapter()
