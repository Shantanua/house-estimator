# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
#import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request
#import mysql.connector
import psycopg2

class ZillowPipeline(object):
    
    def __init__(self):
            self.cnx = psycopg2.connect(user = 'postgres', password = 'postgres', dbname = 'zillow_db', host = '127.0.0.1')
            self.cursor = self.cnx.cursor()
    
    def process_item(self, item, spider):    
        try:
            self.cursor.execute("""INSERT INTO homessold (zillowhomeid,
            sale_price,
            address,
            zipcode,
            city,
            state,
            street,
            road,
            avenue,
            beds,
            baths,
            floorsize,
            lot,
            pricesqft,
            lotdepth,
            lotwidth,
            built_in,
            last_sold_for,
            last_sold_on,
            mls,
            parcel,
            alltimeviews,
            days_on_zillow,
            viewssincelisting,
            shopper_saved_this,
            lastremodelyear,
            exteriormaterial,
            flooring,
            attic,
            condo,
            cooperative,
            dishwasher,
            microwave,
            rangeoven,
            refrigerator,
            washer,
            dryer,
            doorman,
            elevator,
            fireplace,
            garden,
            finishedbasement,
            patio,
            pool,
            stories,
            unitcount,
            water,
            cookingfuel,
            cooling,
            fuelinformation,
            heating)  
                                    VALUES (%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s,
%s
)""", 
                                   (item['title']['zillowhomeid'],
item['title']['sale_price'],
item['title']['address'],
item['title']['zipcode'],
item['title']['city'],
item['title']['state'],
item['title']['street'],
item['title']['road'],
item['title']['avenue'],
item['title']['beds'],
item['title']['baths'],
item['title']['floorsize'],
item['title']['lot'],
item['title']['pricesqft'],
item['title']['lotdepth'],
item['title']['lotwidth'],
item['title']['built_in'],
item['title']['last_sold_for'],
item['title']['last_sold_on'],
item['title']['mls'],
item['title']['parcel'],
item['title']['alltimeviews'],
item['title']['days_on_zillow'],
item['title']['viewssincelisting'],
item['title']['shopper_saved_this'],
item['title']['lastremodelyear'],
item['title']['exteriormaterial'],
item['title']['flooring'],
item['title']['attic'],
item['title']['condo'],
item['title']['cooperative'],
item['title']['dishwasher'],
item['title']['microwave'],
item['title']['rangeoven'],
item['title']['refrigerator'],
item['title']['washer'],
item['title']['dryer'],
item['title']['doorman'],
item['title']['elevator'],
item['title']['fireplace'],
item['title']['garden'],
item['title']['finishedbasement'],
item['title']['patio'],
item['title']['pool'],
item['title']['stories'],
item['title']['unitcount'],
item['title']['water'],
item['title']['cookingfuel'],
item['title']['cooling'],
item['title']['fuelinformation'],
item['title']['heating']
)
                               )
            self.cnx.commit()

        except psycopg2.Error as e:
            print "Error %s" % (e.pgerror)


        return item
        
        
