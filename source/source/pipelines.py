# -*- coding: utf-8 -*-
from scrapy import signal
import json
import codecs

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SourcePipeline(object):
	def __init__(self):
		self.file = codecs.open('amazon_items_info.json','w',encoding='utf-8')

    def process_item(self, item, spider):
    	line = json.dumps(dict(item),ensure_ascii=False)+"\n"
    	self.file.write(line)
        return item

    def spider_closed(self,spider):
    	self.file.close()
    	
