# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SourceItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    itemsid = scrapy.Field()
    price = scrapy.Field()
    descript = scrapy.Field()
    star = scrapy.Field()
    comments_url = 'https://www.amazon.cn/product-reviews/' + itemsid +'/ref=acr_search_see_all?ie=UTF8&showViewpoints=1'
    comments_number = scrapy.Field()
