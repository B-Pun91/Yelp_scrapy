import scrapy
import csv
from ..items import YelpdataextractItem

class YelpExtractSpider(scrapy.Spider):
    name = 'Yelp'
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'Erith.csv'
    }

    start_urls = []
    with open('Erith_urls.csv') as csvReader:
        tmp = csv.reader(csvReader)
        header = next(tmp)
        start_urls = [x[0] for x in tmp]

    # start_urls = [
    #     'https://www.yelp.co.uk/biz/sleepy-hollow-restaurant-newtownabbey'
    #     #'https://www.yelp.co.uk/biz/knags-bar-and-grill-glengormley'
    #     #'https://www.yelp.co.uk/search?find_desc=&find_loc='+location
    # ]


    def parse(self, response):

        items = YelpdataextractItem()
        Name = response.css('.undefined.heading--inline__373c0__10ozy::text').get(default='no_name')
        Address = response.css('.raw__373c0__3rcx7::text').extract()
        Address = " ".join(Address)
        if Address == "":
            Address = 'no_address'
        Phone = response.css('.border-color--default__373c0__3-ifU+ .border-color--default__373c0__3-ifU .border-color--default__373c0__3-ifU .text--offscreen__373c0__2NIm_+ .text-align--left__373c0__2XGa-::text').get(default='no_phone')
        Price_rate = response.css('.text-bullet--after__373c0__3fS1Z.text-size--large__373c0__3t60B::text').get(default='no_pricerate')
        Website = response.css('.text--offscreen__373c0__2NIm_+ .text-align--left__373c0__2XGa- .link-size--inherit__373c0__1VFlE::text').get(default='no_website')
        Speciality = response.css('.text-size--large__373c0__3t60B .link-size--inherit__373c0__1VFlE::text').extract()
        Speciality = " ".join(Speciality)
        if Speciality == "":
            Speciality = 'no_Speciality'
        Total_Reviews = response.css('.text-color--mid__373c0__jCeOG.text-size--large__373c0__3t60B::text').get(default= 'no_reviews')
        Reviews = response.css('.comment__373c0__3EKjH .raw__373c0__3rKqk::text').extract()
        Reviews = " ||| ".join(Reviews)
        if Reviews == "":
           Reviews = 'No Reviews'

        items['Name'] = Name
        items['Address'] = Address
        items['Phone'] = Phone
        items['Price_rate']= Price_rate
        items['Website'] = Website
        items['Speciality'] = Speciality
        items['Total_Reviews'] = Total_Reviews
        items['Reviews'] = Reviews

        yield items
