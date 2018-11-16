import requests
# data={
#     'name':'germey',
#     'age':22
# }
# r=requests.get("http://httpbin.org/get",params=data)
# print(r.text)
# print(r.json())

# request 加 header  访问网页
# headers={
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
# }
# r=requests.get("https://www.zhihu.com/explore",headers=headers)
# print(r.text)

#调用post方法  这个url只能用post访问
# data={
#     'name':'germey',
#     'age':22
# }
# r=requests.post("http://httpbin.org/post",data=data)
# print(r.text)

#调用cookie登陆知乎
# headers={
#     'Cookie':'_zap=c4fbe94e-6ba3-4e7e-ab6e-f178c2a67a72; d_c0="AMCg6zNzgw6PTqMssdgCgOAb6nXfP1t7vHU=|1542119629"; q_c1=fc0dfe90571e4a5ca3bcbec89fec17af|1542119630000|1542119630000; tgw_l7_route=56f3b730f2eb8b75242a8095a22206f8; l_n_c=1; _xsrf=a30e635c5f627d2d8c26a89614d9c9a4; r_cap_id="NDhjMjA2YjAyZjI5NDE1ZGJlNGI3N2VkYWZkZDY3NTg=|1542388543|641c9443b10c9e06c9d99bbca8e425bbcca3d27d"; cap_id="ZTBkYjNkMTM3ZGRlNGRlZTg0MzFkZTUxYTRiZjExMjk=|1542388543|e47fe66e2d78f540779efabcc8a6d7c5c5865013"; l_cap_id="OGZjMmQ3ZjllNDU4NDkxODlkZjczYjJkNDM4OTU0NGM=|1542388543|5456f4c4bb44a26b80c2241bdeda8f10d8c14bad"; n_c=1; __utma=51854390.84353974.1542388547.1542388547.1542388547.1; __utmb=51854390.0.10.1542388547; __utmc=51854390; __utmz=51854390.1542388547.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _xsrf=7G3XX3kT0HGYxMLxnPIij3uAFRcDJjqm; capsion_ticket="2|1:0|10:1542389034|14:capsion_ticket|44:NDczZGRlY2VhNTgxNGRjNDk4MjBmMjk1YmZhODY3YWQ=|b7384283e3f84f3787102f25eab0ee66d5581d6e67c5c192330297d2be652326"; z_c0="2|1:0|10:1542389050|4:z_c0|92:Mi4xTlA4UEJ3QUFBQUFBd0tEck0zT0REaVlBQUFCZ0FsVk5Pa3ZjWEFCaTNKMjhRNUwzbUFadmdtcUZBWnl3S1ZBODFR|71a69225bfff7b7aec955a5abbdf77622a099b03c3901dec04ad7268a89141e7"; __utmv=51854390.100--|2=registration_date=20171228=1^3=entry_date=20171228=1',
#     'Host':'www.zhihu.com',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
# }
# r=requests.get('https://www.zhihu.com',headers=headers)
# print(r.text)

# 利用session 会话维持

# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r=requests.get('http://httpbin.org/cookies')
# print(r.text)

# s=requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r=s.get('http://httpbin.org/cookies')
# print(r.text)

# 有些网站可能需要证书 可以用verify=false 来忽略证书 也可以加上本地证书 cert=（crt文件路径，key文件路径）
# response=requests.get("http://www.12306.cn")
# print(response.status_code)

#设置代理 调用 proxies  超时设置 timeout

# 身份验证
# from requests .auth import HTTPBasicAuth
# auth=HTTPBasicAuth(’username',’ password')

# 使用Prepared Request  可以将请求转换为一个request方法 构建队列 用send发送
# from requests import Request,Session
# url='http://httpbin.org/post'
# data={
#     'name':'germy'
# }
# headers={
#      'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
# }
# s=Session()
# req=Request('POST',url,data=data,headers=headers)
# prepped=s.prepare_request(req)
# r=s.send(prepped)
# print(r.text)

