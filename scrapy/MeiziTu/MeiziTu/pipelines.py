# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class MeizituPipeline(object):
    def process_item(self, item, spider):
        return item

from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from . import settings
class MeiziImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        request_objs=super(MeiziImagePipeline,self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item=item
        return request_objs

    def file_path(self, request, response=None, info=None):
        path = super(MeiziImagePipeline, self).file_path(request, response, info)
        category=request.item['category'][0]
        image_store=settings.IMAGES_STORE
        category_path = os.path.join(image_store, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
        image_name = path.replace("full/", "")
        image_path = os.path.join(category_path, image_name)
        return image_path

    def item_completed(self, results, item, info):
        image_path=[x['path'] for ok,x in results if ok]
        if not image_path:
            raise DropItem('Images Download Failed')
        return item

