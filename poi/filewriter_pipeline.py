# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FileWriterPipeline(object):
    def __init__(self):
        self.file = open('url.csv', 'w')

    def process_item(self, item, spider):
        line = "%s\n"%item['url']
        self.file.write(line)
        return item
