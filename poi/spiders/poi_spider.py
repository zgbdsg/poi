import scrapy
import os
from poi.items import Poi
import pkgutil
import sqlite3

class PoiSpider(scrapy.Spider):
    name = "poi"
    allowed_domains = ["www.poi86.com"]

    start_urls = []
    f = open('url.csv')
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute('select * from URL')
    values = cursor.fetchall()

    count = 0
    for line in f:
        count += 1
        url = "http://www.poi86.com%s"%line.strip()
        cursor.execute('select * from URL where u=\'%s\''%url)
        values = cursor.fetchall()
        if len(values) > 0:
            continue
        start_urls.append(url)
        #if count > 30:
        #    break
    
    cursor.close()
    print "start_url:",len(start_urls)


    def parse(self, response):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        cursor.execute('insert into url (u) values (\'%s\')'%response.url)
        conn.commit()
        cursor.close()

        item = Poi()
        
        name = response.xpath('//h1/text()').extract()
        #print name[0]
        item['name'] = name[0]
        text = response.xpath('//ul/li/text()').extract()
        address = text[-6]
        call = text[-5]
        catergary = text[-4]
        ground = text[-3]
        mars = text[-2]
        baidu = text[-1]
        #print address,call,catergary,ground,mars,baidu
        item['address'] = address
        item['call'] = call
        item['catergary'] = catergary
        item['bigloc'] = ground
        item['marsloc'] = mars
        item['baiduloc'] = baidu

        return item
