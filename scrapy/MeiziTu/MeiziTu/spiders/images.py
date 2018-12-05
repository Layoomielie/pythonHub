# -*- coding: utf-8 -*-
import scrapy
from MeiziTu.items import MeizituItem


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['mzitu.com']
    urls = ['https://www.mzitu.com/xinggan/page/', 'https://www.mzitu.com/japan/page/',
            'https://www.mzitu.com/taiwan/page/', 'https://www.mzitu.com/mm/page/']
    start_urls = []
    for url in urls:
        for i in range(1, 100):
            nextUrl = url + str(i) + '/'
            start_urls.append(nextUrl)

    def parse(self, response):
        liElements = response.css('.main-content .postlist #pins li')
        for liElement in liElements:
            self.title = liElement.css('a img::attr(alt)').extract()
            self.nextUrl = liElement.css('span a::attr(href)').extract_first()
            yield scrapy.Request(url=self.nextUrl, callback=self.parse2,
                                 meta={'title': self.title, 'url': self.nextUrl})

    def parse2(self, response):
        url = response.meta['url']
        title = response.meta['title']
        aElements = response.css('div.pagenavi a')
        pageNo = len(aElements)
        num = aElements[pageNo - 2].css('span::text').extract_first()
        for i in range(1, int(num)):
            self.nextUrl2 = url + '/' + str(i)
            yield scrapy.Request(url=self.nextUrl2, callback=self.parse3, meta={'title': title})

    def parse3(self, response):
        item = MeizituItem()
        item['image_urls'] = response.css('.main-image img::attr(src)').extract()
        item['category'] = response.meta['title']
        yield item
