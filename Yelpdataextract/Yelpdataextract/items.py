# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YelpdataextractItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = scrapy.Field()
    Address = scrapy.Field()
    Phone = scrapy.Field()
    Price_rate = scrapy.Field()
    Website = scrapy.Field()
    Speciality = scrapy.Field()
    Total_Reviews = scrapy.Field()
    Reviews = scrapy.Field()

    pass
