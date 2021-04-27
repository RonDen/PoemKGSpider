from pymongo import MongoClient


class MongoDBClient(object):
    # 饿汉式 单例模式
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MongoDBClient, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        url = 'mongodb://poemkg:poemkg@localhost:27017/poemkg?authSource=admin&authMechanism=SCRAM-SHA-256'
        # self.client = MongoClient(
        #     host='loalhost',
        #     port=27017,
        #     username='poemkg',
        #     password='poemkg',
        #     authSource='admin',
        #     authMechanism='SCRAM-SHA-256'
        # )
        self.client = MongoClient(url)

    def get_connection(self):
        return self.client

    def __del__(self):
        self.client.close()

mongo_db = MongoDBClient().get_connection()
