# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem

class YelpdataextractPipeline:
    def process_item(self, item, spider):
        if 'no_name' in item['Name']:
            raise DropItem('Missing restaurant name.')
        if 'no_address' in item['Address']:
            raise DropItem('Missing restaurant address.')
        return item
