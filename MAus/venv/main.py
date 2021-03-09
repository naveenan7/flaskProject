from scrapy.crawler import CrawlerProcess
import scrapy

import requests
from scrapy.http import Request
from myspider import MySpider

if __name__ == '__main__':

  process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
  })

  process.crawl(MySpider, domain="https://asrc.org.au/")
  process.start()