from scrapyd_api import ScrapydAPI

scrapyd=ScrapydAPI('http://139.224.233.92:6800')

#egg = open('some_egg.egg', 'rb')

#scrapyd.delete_version('zhihuuser','197ca468135511e9a5281dbc0d0a2d2c')

print(scrapyd.list_projects())

#print(scrapyd.list_spiders('zhihuuser'))

#print(scrapyd.job_status('zhihuuser','9d4d8078135511e9a5281dbc0d0a2d2c'))

#scrapyd.delete_version('zhihuuser','9d4d8078135511e9a5281dbc0d0a2d2c')

#scrapyd.schedule('zhihuuser', '9d4d8078135511e9a5281dbc0d0a2d2c')