#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from pyquery import PyQuery as pq

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}

url = 'https://www.zhihu.com/explore'

html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.explore-tab,feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    # a是为了不清空文件里的内容 r  rb  r+ rb+
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()

