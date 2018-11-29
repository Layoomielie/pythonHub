#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

# content='Hello 123 4567a World_This is a Regex Demo'
#
# print(len(content))
#
# #result=re.match('^Hello\s\d{3}\s(\d+)\s\S{7,20}',content)
# result=re.match('^Hello.*?(\d+\s\w*).*?Demo$',content)
# print(result)
# print(result.span())
# print(result.group(1))

html = '''< div id="songs-list">
<h2 class =title ">经典老歌</h2>
<p class=" introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href ="/2.mp3 " singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3 " singer="齐泰">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">尤辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈琳">记事本</a></li>
<li data-view="5’'>
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''

# search 方法会搜寻整个HTML文本  将符合的第一个内容返回
# result=re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
# if result:
#     print(result.group(1),result.group(2))


# findall 会匹配所有文本  re.S 可以避免换行符
# result=re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
# if result:
#      print(result[0],result[1],result[2])

#  re sub 用正则替换信息
# content = '54aK53yuf76JKdas62jfas7'
# content = re.sub('\d+', '', content)
# print(content)

# results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S);
#  for result in results:
#      print(result[1])

# 用re替换html
# html = re.sub('<a.*?>|</a>', '', html)
#  print(html)
# results = re.findall('<li.*?>(.*?)</li>', html, re.S)
# for result in results:
#     print(result.strip())
