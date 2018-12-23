# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from scrapy.loader import ItemLoader
from iprice_scraper.items import IpriceScraperItem

class IpriceSpider(scrapy.Spider):
    name = 'iprice'
    #allowed_domains = ['iprice.sg/search/?term=']
    start_urls = ['http://iprice.sg']

    def __init__(self):
        self.data = pd.read_csv('../../../100.csv',index_col=0)
        self.base_url = 'https://iprice.sg/search/?term='

    def start_requests(self):

        for index, row in self.data.iterrows():

            yield scrapy.Request(url = self.base_url+row['prod_names'].replace(' ','+') + '&sort=_desc',
                                callback = self.parse)


    def parse(self, response):
        for row in response.xpath(
            "//div[@class='pu product relative no-underline w-50 w-33-m w-25-ol w-20-xl white']"
            ):
            loader = ItemLoader(item=IpriceScraperItem(), selector=row, response=response)
            loader.add_value('url', response.url)
            loader.add_xpath('name', ".//a/figure/figcaption/div[1]")
            loader.add_xpath('price', ".//a/figure/figcaption/div[2]/span[@class='accent']/text()")
            loader.add_xpath('ori_price', ".//a/figure/figcaption/div[2]/span[@class='f11 lh-11 original strike db mb3']/text()")
            loader.add_xpath('brand', ".//a/figure/figcaption/div[3]/div/div/div[@class='s-n gray-dark overflow-hidden f13']/strong/text()")
            loader.add_xpath('discount', ".//a/figure/div/span[2]/text()")
            yield loader.load_item()

            # yield {
            #     'url': response.url,
            #     #'link': 'https://iprice.sg' + row.xpath(".//a[@class='no-underline pv1-5']/@href").extract_first(),
            #     'name': row.xpath(".//a/figure/figcaption/div[1]").extract_first(),
            #     'price': row.xpath(".//a/figure/figcaption/div[2]/span[@class='accent']/text()").extract_first(),
            #     'brand': row.xpath(".//a/figure/figcaption/div[3]/div/div/div[@class='s-n gray-dark overflow-hidden f13']/strong/text()").extract_first(),
            #     'discount_percent': row.xpath(".//a/figure/div/span[2]/text()").extract_first()
                
            # }
       

