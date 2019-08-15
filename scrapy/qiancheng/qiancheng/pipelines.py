# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo

class QianchengPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline():
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT')
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8', port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self,spider):
        self.db.close()

    def process_item(self,item,spider):
        data=dict(item)
        keys=','.join(data.keys())
        values=','.join(['%s']*len(data))
        table='qiancheng'
        sql='insert into %s (%s) values (%s)'%(table,keys,values)
        self.cursor.execute(sql,tuple(data.values()))
        self.db.commit()
        return item


class MongoPipeline(object):
    collection_name = 'qianchen'  # 这里的地方是连接的数据库表的名字

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URL'),  # get中有两个参数，一个是 配置的MONGO_URL ，另一个是localhost
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'local')  # 这里的两个参数,第一个是数据库配置的.第二个是它的表的数据库的名字
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item

