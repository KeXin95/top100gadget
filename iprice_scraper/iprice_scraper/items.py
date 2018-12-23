# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags
import re

# def clean_name(value):
#     return re.search('<b>(.*)</b>',value).group(1) + " " +\
#             (re.search('</b>(.*)</div>',value).group(1)).strip()

def clean_name(value):
    return value.replace('&amp;','&').replace('"','')

def clean_price(value):
    return value.replace('S$','').strip()

def clean_discount(value):
    return value[1:-1]

class IpriceScraperItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakerFirst()
        )
    name = scrapy.Field(
        input_processor = MapCompose(remove_tags, str.strip, clean_name),
        output_processor = TakeFirst() 
        )
    price = scrapy.Field(
        input_processor = MapCompose(clean_price),
        output_processor = TakeFirst() 
    )
    ori_price = scrapy.Field(
        input_processor = MapCompose(clean_price),
        output_processor = TakeFirst() 
    )
    brand = scrapy.Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    discount = scrapy.Field(
        input_processor = MapCompose(clean_discount),
        output_processor = TakeFirst()
    )
