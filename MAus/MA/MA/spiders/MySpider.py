import scrapy
import re
from scrapy.linkextractors import LinkExtractor
import uuid
import requests
from scrapy.http import Request


class MySpider1(scrapy.Spider):

    name = 'myspider'

    def __init__(self, domain=None, *args, **kwargs):
        #domain = input('please enter the domain:')
        self.domain = domain

    def start_requests(self):

        web_sites = self.domain

        for web_site in web_sites:
            yield scrapy.Request(url=web_site)

    def parse(self, response):

        sitename = str(response.xpath("//title/text()").get())
        sitename = re.sub('[^A-Za-z0-9]+', '', sitename)
        if sitename == '':
            sitename = uuid.uuid4()
        page = response.url.split("/")[-2]
        filename = f'HOME-{sitename}-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        link = LinkExtractor()
        links = link.extract_links(response)
        links.append(response.request.url)
        '''
        with open('listfile.txt', 'w') as filehandle:
            filehandle.writelines("%s\n" % place for place in links)
        '''
        for _link in links:
            yield scrapy.Request(_link.url, callback=self.parse_list, meta={'site_name': sitename})

    def parse_list(self, response):

        basename = response.url.split("/")[-1]
        page = response.url.split("/")[-2]
        getsitename = response.meta.get('site_name')
        filename = f'pages-{getsitename}-{basename}-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

#scrapy crawl myspider
