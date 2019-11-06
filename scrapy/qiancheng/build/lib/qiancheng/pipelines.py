# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from elasticsearch import Elasticsearch
import time, datetime
from pandas._libs import json


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

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        data = dict(item)
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        table = 'qiancheng'
        sql = 'insert into %s (%s) values (%s)' % (table, keys, values)
        self.cursor.execute(sql, tuple(data.values()))
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


class ESPipeline(object):
    collection_name = 'qiancheng'  # 这里的地方是连接的数据库表的名字
    index = "qiancheng"
    type = "doc"

    def __init__(self, es_host):
        self.es_host = es_host
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        self.index = self.index + "-" + str(year) + "-" + str(month)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            es_host=crawler.settings.get('ES_HOST'),
        )

    def open_spider(self, spider):
        self.es = Elasticsearch([self.es_host])

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        # result = self.es.index(index=self.index, doc_type='doc', body=item)
        if item != None:
            item_dict = dict(item)
            timestr = item_dict['time']
            timeArray = time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
            otherStyleTime = time.strftime("%Y-%m-%dT%H:%M:%S", timeArray)
            item_dict['time'] = otherStyleTime
            # json_str =json.dumps(item_dict)+','
            # position=item['position']
            # obj={"position":position}
            # print(item_dict)
            result = self.es.index(index=self.index, doc_type='doc', body=item_dict)
