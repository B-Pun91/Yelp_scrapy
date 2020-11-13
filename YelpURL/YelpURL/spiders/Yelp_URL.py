
import scrapy
from ..items import YelpurlItem

class YelpURLSpider(scrapy.Spider):
    name = 'YelpURL'
    change_page = 30
    location = 'Erith'
    total_page_num = 4
    start_urls = [
        'https://www.yelp.co.uk/search?cflt=restaurants&find_loc=' + location,
    ]

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'Erith_urls.csv',
        'HTTPPROXY_ENABLED': True
    }

    # rules = [Rule(LinkExtractor(allow='biz/'), callback='parse', follow= True)]

    def parse(self, response):

        restaurant_url = response.xpath("//a/@href").extract()
        restaurant_url = [x.split('?')[0] for x in restaurant_url]
        for x in list(set(restaurant_url)):
            item = YelpurlItem()
            item['restaurant_url'] = 'https://www.yelp.co.uk' + x
            yield item


        if YelpURLSpider.change_page <= 150:
            location = 'Erith'
            next_page = 'https://www.yelp.co.uk/search?cflt=restaurants&find_loc='+location+'&start='+str(YelpURLSpider.change_page)
            YelpURLSpider.change_page += 30
            yield response.follow(next_page, callback = self.parse)

