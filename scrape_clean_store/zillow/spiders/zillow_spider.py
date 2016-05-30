
# coding: utf-8

# In[ ]:

from __future__ import absolute_import
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from zillow.items import zillowItem


class nzillowpider(CrawlSpider):
    name = "zillow_s"
    allowed_domains = ["www.zillow.com"]
    start_urls = ['http://www.zillow.com/homes/for_sale/08540']
    x = 0
    rules = [
            Rule(LinkExtractor(allow = ['/homedetails/.*']), callback = 'parse_item'),
            Rule(LinkExtractor(allow = ['/homes/for_sale/\d{5}.*/\d_p/']), callback = 'parse_item', follow = True)
    ]
    """
    def parse(self, response):
        links = Selector(response=response).xpath('//a[@class = "hdp-link routable"]')
        print 'Jamba Juice!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        #print links
        for link in links:
            #print response
            item = zillowItem()
            item['link'] = link.xpath('@href').extract()
            item['title'] = link.xpath('@title').extract()
            item['z_id'] = link.xpath('@id').extract()
            #print item['link'], item['title']
            yield item
        print 'Jamba Juice!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    """
    def parse_item(self, response):
        print response.url
        self.x += 1
        print self.x
        #print 'Yeahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    #def parse_item2(self, response):
        #print response.url