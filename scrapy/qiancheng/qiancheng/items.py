# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item ,Field

class QianchengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position=Field()
    company = Field()
    city = Field()
    region = Field()
    date = Field()
    time = Field()
    maxPrice = Field()
    minPrice = Field()
    avgPrice = Field()
    profession = Field()
    companyType = Field()
    location = Field()
    cotype = Field()
    degree = Field()
    workyear = Field()
    companySize = Field()
    jobTerm = Field()
    positionUrl=Field()


    pass
