# -*- coding:utf-8 -*-

from elasticsearch_dsl import DocType, Nested, Date, Boolean, analyzer, Completion, Text, Keyword, Integer, Document, \
    Double
from elasticsearch_dsl.connections import connections

# 新建连接
connections.create_connection(hosts="10.100.23.92")


class ArticleType(Document):
    # 文章类型
    id = Integer()
    position = Keyword()
    company = Keyword()
    city = Keyword()
    region = Keyword()
    date = Date()
    time = Date()
    maxPrice = Double()
    minPrice = Double()
    avgPrice = Double()
    profession = Keyword()
    companyType = Keyword()
    location = Keyword()
    cotype = Keyword()
    degree = Keyword()
    workyear = Keyword()
    companySize = Keyword()
    jobTerm = Keyword()
    positionUrl = Keyword()

    class Index:
        # 数据库名称和表名称
        name = "qiancheng"
        type="doc"


if __name__ == '__main__':
    ArticleType.init()
