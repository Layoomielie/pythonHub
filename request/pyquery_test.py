#!/usr/bin/python
# -*- coding: utf-8 -*-

html = '''
<div>
<ul id="contains">
<li class="item-0">first item</li>
<li class="item-1 "><a href＝"link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-1"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''

from pyquery import PyQuery as pq

doc = pq(html)
# print(doc)
# print(doc('#contains .item-0'))

# doc=pq(url='https://cuiqingcai.com')
# print(doc('title'))

# 查找子节点
# items=doc('#contains')
# lis=items.find('li')
# lis=items.children()
# print(lis)

# 查找父节点
# items=doc('.bold')
# parent=items.parent()
# print(print())

items=doc.find('.bold')
print(items.text())

# 节点操作 addClass removeClass   可以用html()方法改变文本内容
