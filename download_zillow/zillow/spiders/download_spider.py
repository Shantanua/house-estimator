
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
    list_of_links = ['10022',
			'10023',
			'10024',
			'10025',
			'10026',
			'10027',
			'10028',
			'10029',
			'10030',
			'10031',
			'10032',
			'10033',
			'10034',
			'10035',
			'10036',
			'10037',
			'10038',
			'10039']

    temp = ['http://www.zillow.com/homes/recently_sold/' + i for i in list_of_links] 
    print temp
    start_urls = temp
    rules = [
            Rule(LinkExtractor(allow = ['/homedetails/.*']), follow=False, callback = 'parse_item'),
            Rule(LinkExtractor(allow = ['/homes/recently_sold/\d{5}.*/\d+_p/']), follow = True)
    ]
        
    def parse(self, response):
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
