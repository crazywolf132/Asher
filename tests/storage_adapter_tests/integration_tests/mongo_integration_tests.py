from unittest import SkipTest
from tests.base_case import SamanthaTestCase
from .base import StorageIntegrationTests
from samantha.adapters.storage import MongoDatabaseAdapter


class MongoStorageIntegrationTests(StorageIntegrationTests, SamanthaTestCase):

    def setUp(self):
        super(MongoStorageIntegrationTests, self).setUp()

        from pymongo.errors import ServerSelectionTimeoutError
        from pymongo import MongoClient

        # Skip these tests if a mongo client is not running
        try:
            client = MongoClient(
                serverSelectionTimeoutMS=0.2
            )
            client.server_info()

        except ServerSelectionTimeoutError:
            raise SkipTest("Unable to connect to mongo database.")

        self.Samantha.storage_adapters = []
        self.Samantha.storage = MongoDatabaseAdapter()
