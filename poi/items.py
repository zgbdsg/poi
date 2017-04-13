# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Poi(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    distinct = scrapy.Field()
    address = scrapy.Field()
    call = scrapy.Field()
    catergary = scrapy.Field()
    bigloc = scrapy.Field()
    marsloc = scrapy.Field()
    baiduloc = scrapy.Field()

    pass

class Url(scrapy.Item):
    url = scrapy.Field()
    pass


class Ip(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    pass
