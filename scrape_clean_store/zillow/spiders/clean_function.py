
# coding: utf-8

# In[ ]:

def cleanSingleLines(alist):
            import re
            req = {}
            x_indic, y_indic, z_indic = 0,0,0
            
            for items in alist:
                x = re.search('Built in \d{4}', items)
                if x!= None:
                    req['built_in'] = int(re.findall('\d{4}', items)[0])
                    x_indic = 1
                y = re.search('\d+ days on Zillow', items)
                if y!= None:
                    req['days_on_zillow'] = int(re.findall('\d+', items)[0])
                    y_indic = 1
                z = re.search('\d+ shoppers? saved this home',items)
                if z!= None:
                    req['shopper_saved_this'] = int(re.findall('\d+', items)[0])
                    z_indic = 1
                    
            if x_indic == 0:
                req['built_in'] = None
            if y_indic == 0:
                req['days_on_zillow'] = None
            if z_indic == 0:
                req['shopper_saved_this'] = None       
                        
            others = {'Attic','Garden','Fireplace','Finished basement','Dishwasher','Microwave','Refrigerator','Dryer','Range / Oven','Washer','Doorman','Elevator','Pool','Patio','Cooperative','Condo'}
            for item in others:
                if item in alist:
                    req[''.join((re.sub('\W+',"",item)).split(' ')).lower()] = 1  
                else:
                    req[''.join((re.sub('\W+',"",item)).split(' ')).lower()] = None
                    
            return req

def cleanDicts(adict):
            import re
            req = {}
            
            imp = {'Cooling','CookingFuel','Heating','Water','Fuel Information','Stories','Unit count','Views since listing','Last remodel year'}
            for keys in imp:
                if keys in adict:
                    req[''.join(keys.split(' ')).lower()] = adict[keys]
                else:
                    req[''.join(keys.split(' ')).lower()] = None
            
            imp2 = ['Floor size','Price/sqft','Lot depth', 'Lot width','Lot','All time views']
            for items in imp2:
                if items in adict:
                    x = re.sub('\W+',"",adict[items])
                    req[''.join((re.sub('\W+',"",items)).split(' ')).lower()] = int(re.findall('(\d+)',x)[0])
                else:
                    req[''.join((re.sub('\W+',"",items)).split(' ')).lower()] = None
                    
            if 'Last sold' in adict:
                    groups = re.findall('(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s(\d{4})\s(\w{3})\s(\$.*)',adict['Last sold'])[0]
                    month_dict = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4,'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
                    req['last_sold_on'] = str(month_dict[groups[0]]) + '/' + str(groups[1])
                    req['last_sold_for'] = int(re.sub('\W+',"",groups[3]))
            else:
                    req['last_sold_on'] = None
                    req['last_sold_for'] = None
                
            imp3 = ['MLS #','Parcel #','Zillow Home ID']
            for items in imp3:
                if items in adict:
                    req[''.join((re.sub('\W+',"",items)).split(' ')).lower()] = re.sub('\s+',"",adict[items])
                else:
                    req[''.join((re.sub('\W+',"",items)).split(' ')).lower()] = None
            
            imp4 = ['Flooring','Exterior material']
            for items in imp4:
                if items in adict:
                    req[''.join(items.split(' ')).lower()] = adict[items].split(',')[0]
                else:
                    req[''.join(items.split(' ')).lower()] = None
            return req