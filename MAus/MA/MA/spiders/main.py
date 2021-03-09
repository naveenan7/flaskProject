from scrapy.crawler import CrawlerProcess
from MySpider import MySpider1

if __name__ == '__main__':

  CrawlerProcess.crawl(MySpider1, myurls=[
    'https://asrc.org.au/'
  ])