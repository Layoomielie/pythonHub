# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item ,Field


class UserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    avatar_url_template=Field()
    name=Field()
    url=Field()
    gender=Field()
    headline=Field()
    id=Field()
    url_token=Field()
    answer_count=Field()
    articles_count=Field()
    badge=Field()
    employments=Field()
    follower_count=Field()
    type=Field()
