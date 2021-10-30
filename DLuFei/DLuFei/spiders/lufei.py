import scrapy
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from DLuFei.items import DlufeiItem

class LufeiSpider(scrapy.Spider):
    """
        使用selenium+scrapy爬取路飞图像
    """
    name = 'lufei'
    start_urls = [
        'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1619588223486_R&pv=&ic=0&nc=1&z=0&hd=0&latest=0&copyright=0&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E8%B7%AF%E9%A3%9E']
    urls = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1619588223486_R&pv=&ic=0&nc=1&z=0&hd=0&latest=0&copyright=0&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E8%B7%AF%E9%A3%9E'
    chrome_options = Options()
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    # 解决浏览器受控制信息
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome = webdriver.Chrome(executable_path=r'D:\Python\Scripts\chromedriver.exe', options=chrome_options)

    def parse(self, response):
        uls = response.xpath('//*[@id="imgid"]/div/ul//li/@data-thumburl').extract()
        for ul in uls:
            item = FuleiItem()
            item['Purl'] = ul.strip()
            yield item

    def closed(self, spider):  ###关闭
        self.chrome.quit()
