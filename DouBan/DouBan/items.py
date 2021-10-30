# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    name = scrapy.Field()
    daoyan = scrapy.Field()
    bianju = scrapy.Field()
    zhuyang = scrapy.Field()
    leixing = scrapy.Field()
    yuyang = scrapy.Field()
    juqing = scrapy.Field()