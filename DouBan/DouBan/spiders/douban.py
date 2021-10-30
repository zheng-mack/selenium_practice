import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from DouBan.items import DoubanItem
from scrapy_redis.spiders import RedisCrawlSpider


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    redis_keys = 'db'

    # start_urls = ['https://movie.douban.com/top250']
    link1 = LinkExtractor(restrict_xpaths='//*[@id="content"]/div/div[1]/div[2]')
    link2 = LinkExtractor(restrict_xpaths='//*[@id="content"]/div/div[1]/ol')
    rules = (
        Rule(link1, follow=True),  # 解析页面链接
        Rule(link2, callback='parse_item', follow=False),  # 解析每一部剧的内容

    )

    def parse_item(self, response):
        item = RedisTestItem()
        item['name'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract_first().strip()
        item['daoyan'] = response.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract_first()
        item['bianju'] = ''.join(response.xpath('//*[@id="info"]/span[3]/span[2]//text()').extract())
        item['zhuyang'] = ''.join(response.xpath('//*[@id="info"]/span[3]//text()').extract())
        item['leixing'] = ''.join(response.xpath('//*[@id="info"]//span[@property="v:genre"]//text()').extract())
        item['juqing'] = ''.join(response.xpath('//span[@property="v:summary"]//text()').extract()).strip()
        yield item