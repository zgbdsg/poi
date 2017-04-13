# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class IpPipeline(object):
    def __init__(self):
        self.file = open('ip.csv', 'w')

    def process_item(self, item, spider):
        line = "%s\t%s\n"%(item['ip'],item['port'])
        self.file.write(line.encode('utf8'))
        return item
