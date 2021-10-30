from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import re

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('lang=zh_CN.UTF-8')
# 解决浏览器受控制信息
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36')
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
path = r'D:\Python\Scripts\chromedriver.exe'


class entrance:
    def __int__(self):
        self.driver = webdriver.Chrome(executable_path=path, options=chrome_options)

    def choice_city(self):
        """
        :return:返回选择的城市Ctiy
        """
        self.driver.get("https://www.meituan.com/changecity/")
        while True:
            time.sleep(0.5)
            F_url = self.driver.current_url
            if re.search('changecity', F_url) is None:
                time.sleep(2)
                T_url = self.driver.current_url
                break
        T_url = re.match(r'https://(.*?).meituan', T_url).group(1)
        return T_url

    def denglu_test(self, T_url, driver):
        url = "https://" + T_url + ".meituan.com"  # 不带项目的网址
        """
            待封装链接
        """
        ###
        self.driver.get(url + "/meishi/pn1/")  # 改为自定义（城市+项目+页数）
        time.sleep(1)
        currentPageUrl = self.driver.current_url  # 获取当前网页url,判断是否需要登录
        currentPageUrl = re.match(r'https://(.*?).meituan', currentPageUrl).group(1)
        if currentPageUrl == 'passport':
            '''登录
            user= 'xxxxxx'
            password= 'xxxx'
            ？？？
            for i in range(len(user)):            #输入账号        
                driver.find_element_by_id('login-email').send_keys(user[i])
                sjs = random.random()
                time.sleep(sjs)
            for i in range(len(password)):             #输入密码
                driver.find_element_by_id('login-password').send_keys(password[i])
                sjs = random.random()
                time.sleep(sjs)
            driver.find_element_by_css_selector("input[value='登录']").click()
            '''
            while True:  # 判断是否要验证
                time.sleep(2)
                currentPageUrl = driver.current_url
                if currentPageUrl == (url + '/meishi/pn1/'):
                    break
            time.sleep(3)

    def close_driver(self):
        self.driver.quit()
