
# coding: utf-8

# In[ ]:

def cleanDicts(adict):
            import re
            req = {}
            imp = {'Cooling',
                    'Exterior material',
                    'Floor Description',
                    'Flooring',
                    'Fuel Information',
                    'Heating',
                    'MLS #',
                    'Parcel #',
                    'Stories',
                    'Unit count',
                    'Views since listing', 
                    'Zillow Home ID',
                    'Last remodel year'
                    }
            for items in adict:
                if items in imp:
                    req[items] = adict[items]
                elif items in ['Floor size','Price/sqft','Lot depth', 'Lot width'] :
                    x = re.sub('\W+',"",adict[items])
                    req[items] = re.findall('(\d+)',x)[0]
                elif items == 'Last sold':
                    groups = re.findall('(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s(\d{4})\s(\w{3})\s(\$.*)',adict[items])[0]
                    month_dict = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4,'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
                    req['last_sold_on'] = str(month_dict[groups[0]]) + '/' + str(groups[1])
                    req['last_sold_for'] = re.sub('\W+',"",groups[3])
                elif items in ['MLS #','Parcel #','Zillow Home ID']:
                    req[items] = re.sub('\s+',"",adict[items])
            return req

