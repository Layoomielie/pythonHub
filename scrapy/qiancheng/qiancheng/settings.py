# -*- coding: utf-8 -*-

# Scrapy settings for qiancheng project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qiancheng'

SPIDER_MODULES = ['qiancheng.spiders']
NEWSPIDER_MODULE = 'qiancheng.spiders'

MYSQL_HOST='47.101.171.168'
MYSQL_DATABASE='scrapy'
MYSQL_PORT=3306
MYSQL_USER='root'
MYSQL_PASSWORD='44253432'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'qiancheng (+http://www.yourdomain.com)'


MONGO_URL = '47.101.171.168'
MONGO_DATABASE = 'local'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# redis配置
# 改用redis的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 改用redis的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

REDIS_HOST = '47.101.171.168'
REDIS_PORT = 6379
#REDIS_PASSWORD = "44253432"

#REDIS_URL = 'redis://root:44253432@47.101.171.168:6379'
#设置断点续爬
SCHEDULER_PERSIST = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False
RANDOM_DELAY=2
# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'referer':'https://search.51job.com'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'qiancheng.middlewares.QianchengSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'qiancheng.middlewares.QianchengDownloaderMiddleware': 543,
  #  'qiancheng.middlewares.RandomDelayMiddleware':999,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'qiancheng.pipelines.QianchengPipeline': 300,
#    'qiancheng.pipelines.MysqlPipeline': 301,
    'qiancheng.pipelines.MongoPipeline': 301,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
