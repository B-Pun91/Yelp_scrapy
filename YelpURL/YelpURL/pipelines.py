# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class YelpurlPipeline(object):
    def process_item(self, item, spider):
        if not '/biz/' in item['restaurant_url']:
             raise DropItem('Dropped: '+item['restaurant_url'])
        return item
