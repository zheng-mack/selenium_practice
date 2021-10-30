# Scrapy settings for DLuFei project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'DLuFei'

SPIDER_MODULES = ['DLuFei.spiders']
NEWSPIDER_MODULE = 'DLuFei.spiders'
LOG_LEVEL='ERROR'
DOWNLOAD_DELAY = 0.25
ROBOTSTXT_OBEY = False

IMAGES_STORE = './imgs'
DOWNLOADER_MIDDLEWARES = {
   'DLuFei.middlewares.DlufeiDownloaderMiddleware': 300,
}

ITEM_PIPELINES = {
   'DLuFei.pipelines.DlufeiPipeline': 543,
}