import scrapy
import json
import csv

from ..items import YelpamenitiesItem

class YelpamenitiesSpider(scrapy.Spider):
    name = 'Amenities'

    # start_urls = [
    #     'https://www.yelp.co.uk/biz/sleepy-hollow-restaurant-newtownabbey'
    # ]

    start_urls = []
    with open('Glengormley_urls.csv') as csvReader:
        tmp = csv.reader(csvReader)
        header = next(tmp)
        start_urls = [x[0] for x in tmp]

    def parse(self, response):
        #items = YelpamenitiesItem
        a = response.xpath('//script[@type="application/json"]//text()').extract()[2]
        d = a.replace('-->', '').replace('<!--', '')

        d = json.loads(d)

        amenities = d['bizDetailsPageProps']['moreBusinessInfoProps']
        #print(amenities)


        # with open('data1.json', 'w', encoding='utf-8') as f:
        #     json.dump(amenities, f, ensure_ascii=False, indent=4)

        yield amenities