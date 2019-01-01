import pymongo
class MongoPipeline(object):
    def __init__(self,mongo_url,mongo_db):
        self.mong_url=mongo_url
        self.mong_db=mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_url=crawler.settings.get('MONGO_URL'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(host='139.224.233.92', port=27017)
        self.db=self.client[self.mong_db]

    def process_item(self,item,spider):
        name='quotes'
        self.db[name].insert(dict(item))
        return item

    def close_spider(self,spider):
        self.client.close()

from scrapy.exceptions import DropItem

class TextPipeline(object):
    def __init__(self):
        self.limit=50

    def process_item(self,item,spider):
        if item['text']:
            if len(item['text'])>self.limit:
                item['text']=item['text'][0::self.limit].rstrip()+'...'
            return item
        else:
            return DropItem('Missing Text')
