
# coding: utf-8

# In[ ]:




# In[ ]:

from __future__ import absolute_import
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from zillow.items import zillowItem
from zillow.spiders.clean_function import cleanDicts
from zillow.spiders.clean_function import cleanSingleLines
import re


class nzillowpider(CrawlSpider):
    name = "zillow_s2"
    allowed_domains = ["www.zillow.com"]
    start_urls = ['http://www.zillow.com/homedetails/11-Westcott-Rd-Princeton-NJ-08540/39007353_zpid']
 
     
    def parse(self, response):
        item = zillowItem()
        req = {}     
        
        # Get house address #
        try: 
            address = Selector(response=response).xpath('//header[@class = "zsg-content-header addr"]/h1/text()').extract()[0].split(',')[0]
            req['address'] = address
        except:
            req['address'] = None
        
        # Get street number from address #
        try:
            street = re.findall('\s(\w+)\sSt',address)[0]
            req['street'] = street
        except:
            req['street'] = None  
            
        try:
            avenue = re.findall('\s(\w+)\sAve',address)[0]
            req['avenue'] = avenue
        except:
            req['avenue'] = None           
            
        try:
            avenue = re.findall('\s(\w+)\sRd',address)[0]
            req['road'] = avenue
        except:
            req['road'] = None 
        
        # Get sale price #
        try:
            sale_price = Selector(response=response).xpath('//div[@class = "main-row  home-summary-row"]/span/text()').extract()[0]
            req['sale_price'] = int(re.sub('\W+',"",sale_price))
        except:
            sale_price = Selector(response=response).xpath('//div[@class = "main-row status-icon-row recently-sold-row home-summary-row"]/span/text()').extract()[0]
            req['sale_price'] = int(re.sub('\W+',"",sale_price))   
        
        # Get address specifics #
        try:
            address = Selector(response=response).xpath('//span[@class = "zsg-h2 addr_city"]/text()').extract()[0]
            groups = re.findall('(.+)\,\s(\w{2})\s(\d{5})',address)[0]
            req['city'] = groups[0]
            req['state'] = groups[1]
            req['zipcode'] = groups[2]
        except:
            req['city'] = None
            req['state'] = None
            req['zipcode'] = None
        
        # Get rooms types #
        
        links1 = Selector(response=response).xpath('//span[@class = "addr_bbs"]/text()').extract()
        try:
            k = re.search('Studio',links1[0])
            j = re.search('(\d+)',links1[0])
            if k != None:
                req['beds'] = 0.5
            elif j != None:
                req['beds'] = int(re.findall('(\d+)',links1[0])[0])
            else:
                req['beds'] = None
        except:
            req['beds'] = None
        
        try:
            req['baths'] = int(re.findall('(\d+)',links1[1])[0])
        except:
            req['baths'] = None
        
        # Get house details #
        links2 = Selector(response=response).xpath('//ul[@class = "zsg-list_square zsg-lg-1-3 zsg-md-1-2 zsg-sm-1-1"]')
        item['title'] = []
        for link in links2:
            item['title'].extend(link.xpath('li/text()').extract())
        info2 = item['title']
        info3 = {}
        info4 = []
        for items in info2:
            try:
                if ':' in items:
                    x = re.split(':\s',items)
                    info3[x[0]] = x[1]
                else: info4.append(items)
            except:
                continue
        item['title'] = cleanDicts(info3)
        item['title'].update(cleanSingleLines(info4))
        item['title'].update(req)
        
        # Return all the acquired information #
        yield item
    
