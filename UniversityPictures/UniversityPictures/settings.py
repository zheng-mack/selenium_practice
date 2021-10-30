# Scrapy settings for UniversityPictures project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'UniversityPictures'

SPIDER_MODULES = ['UniversityPictures.spiders']
NEWSPIDER_MODULE = 'UniversityPictures.spiders'

ITEM_PIPELINES = {
   'UniversityPictures.pipelines.UniversitypicturesPipeline': 300,
}
# 伪装请求载体身份
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
DOWNLOAD_DELAY=0.25
LOG_LEVEL='ERROR'
IMAGES_STORE = './imgs'
ROBOTSTXT_OBEY = False
