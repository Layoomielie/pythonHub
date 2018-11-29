#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

# soup = BeautifulSoup('<p>Hello</p>', 'lxml')
# print(soup.p.string)

html = """
<html><head> <title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class＝"story" > Once upon a time there were three little sisters; and their names were
<div class="div1"><a href＝"http://example.com/elsie" class= "sister" id＝"link1＂><!--Elsie--></a></div> ,
<a href＝"http:/ /example.com/lacie" class ＝"sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class ="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well. </p>
<p class=" story"> ... </p>
"""
soup = BeautifulSoup(html, 'lxml')
# print(soup.title)
# print(type(soup.title))
# print(soup.head)
# print(soup.p)

# 获取节点属性  attr返回为字典类型
# print(soup.p.attrs)
# print(soup.p.attrs['name'])

# print(soup.p['name'])

# 获取内容
# print(soup.p.string)

# 获取子元素
# 孩子属性 children
# print(soup.p.children)
# for i,child in enumerate(soup.p.children):
#     print(i,child)

# 子孙属性 descendants
# for i ,child in enumerate(soup.p.descendants):
#     print(i,child)

# find_all 查找所有符合条件的元素
# print(soup.find_all(name='a'))
# for a in soup.find_all(name='a'):
#     print(a.string)

# 通过属性进行查找
# print(soup.find_all(attrs={'class':'div1'}))

# find_parents 返回祖先元素  find_parent() 返回父类元素
# find_next_sibings 返回后面所有兄弟节点  find_next_sibing 返回后面第一个兄弟节点
# find_previous_siblings 前者返回前面所有节点     find_previous_sibing 返回前面第一个节点
# find_all_next 返回节点后所有符合条件的节点      find_next返回后者第一个符合条件的节点
# find_all_previous 返回借点钱符合条件的节点    find_previous 放回前面第一个符合条件的节点

# print(soup.find_parents(id='link1'))
#
# print(soup.find_previous_sibling(name='a',attrs={'id':'link3'}))