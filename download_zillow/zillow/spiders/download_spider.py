
# coding: utf-8

# In[ ]:




# In[ ]:

from __future__ import absolute_import
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from zillow.items import zillowItem
import re
import pickle

class dzillowpider(CrawlSpider):
    name = "download_z"
    allowed_domains = ["www.zillow.com"]
    list_of_links = ['10472',
		'10473',
		'10474',
		'10475',
		'10301',
		'10302',
		'10303',
		'10304',
		'10305',
		'10306',
		'10307',
		'10308',
		'10309',
		'10310',
		'10312',
		'10314']

    temp = ['http://www.zillow.com/homes/recently_sold/' + i for i in list_of_links] 
    print temp
    start_urls = temp
    rules = [
            Rule(LinkExtractor(allow = ['/homedetails/.*']), follow=False, callback = 'parse_item'),
            Rule(LinkExtractor(allow = ['/homes/recently_sold/\d{5}.*/\d+_p/']), follow = True)
    ]
        
    def parse_item(self, response):
       try:
           body_fileName = re.sub('\/+','_',response.url)
           body_fileName2 = re.sub('\:','_', body_fileName)
           print "fileName:" + body_fileName2
           html_dump = response.body
           with open('html_save/' + body_fileName2,'wb') as handle:
               pickle.dump(html_dump, handle)
       except:
           print "Unexpected error:", sys.exc_info()[0]
           pass
