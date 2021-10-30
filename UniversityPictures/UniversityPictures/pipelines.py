# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from itemadapter import ItemAdapter
import scrapy


class ImgproPipeline(object):
    item = None

    def process_item(self, item, spider):
        return item


class UniversitypicturesPipeline:
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['Purl'])

    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-5]
        return file_name

    def item_completed(self, results, item, info):
        return item  # 该返回值会传递给下一个即将被执行的管道类