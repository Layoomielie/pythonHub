#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1005052830678474',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if (response.status_code == 200):
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        weibo = {}
        weibo['id'] = items.get('id')
        weibo['text'] = pq(items.get('text')).text()
        weibo['attitudes'] = items.get('attitudes_count')
        weibo['comments'] = items.get('comments_count')
        weibo['reposts'] = items.get('reposts_count')
        yield weibo


if __name__ == '__main__':
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(json)
