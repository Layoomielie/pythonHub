# -*- coding: utf-8 -*-
import  redis

pool=redis.ConnectionPool(host='localhost',port=6379,decode_responses=True)

r=redis.Redis(connection_pool=pool)
r2=redis.Redis(connection_pool=pool)

r.set('apple','a')
print(r.get('apple'))

r2.set('banana','b')
print(r2.get('banana'))

print(r.client_list())
print(r2.client_list())