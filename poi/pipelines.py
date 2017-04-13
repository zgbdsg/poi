# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PoiPipeline(object):
    def __init__(self):
        self.file = open('poi.csv', 'a')

    def process_item(self, item, spider):
        line = "%s\t%s\t%s\t%s\t%s\t%s\t%s\n"%(item['name'],item['address'],item['call'],item['catergary'],item['bigloc'],item['marsloc'],item['baiduloc'])
        self.file.write(line.encode('utf8'))
        return item
