# -*- coding: utf-8 -*-
import scrapy

from qianming.items import QianmingItem


class QmSpider(scrapy.Spider):
    name = 'qm'
    allowed_domains = ['qzone.cc']
    start_urls = ['http://www.qzone.cc/qianming/hot/']
    for i in range(2,16):
        nextUrl='http://www.qzone.cc/qianming/hot/list_'+str(i)+'.html'
        start_urls.append(nextUrl)

    def parse(self, response):
        dlElements=response.css('#refreshDiv dl')
        for dlElement in dlElements:
            item=QianmingItem()
            item['content']=dlElement.css('dd.feed_content p::text').extract_first()
            yield item

