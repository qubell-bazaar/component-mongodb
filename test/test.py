import os

from qubell.api.testing import *

@environment({
    "default": {}
})
class MongodbComponentTestCase(BaseComponentTestCase):
    name = "component-mongodb"
    apps = [{
        "name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name))
    }]

    @instance(byApplication=name)
    def test_mongo_connection(self, instance):
        import pymongo
        from pymongo import MongoClient
        url = instance.returnValues['mongo.url']
        user = instance.revision['parameters']['configuration.user']
        client = MongoClient(url)
        db = client.user
