import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from toExcel import createtrExcel
from selenium.webdriver import ActionChains


class MeiTuan:
    def __init__(self, driver):
        """
        : return list_information:店铺信息列表[店名，地址，电话，图片1...5]
        """
        self.HTTP = 'https:'
        self.driver = driver
        self.excel = createtrExcel('美团', '美食')

    def pageHandle(self):
        try:
            dianjia_urls = []
            wait = WebDriverWait(self.driver, 4, 2)
            # 获取下一页连接
            next_url = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'icon-btn_right')))

            # 获取店家连接
            dianjia_url = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="img"]//a')))
            for d in dianjia_url:
                if ('4164973' and '73697') in d.get_attribute('href'):
                    continue
                dianjia_urls.append(d.get_attribute('href'))
            if len(self.driver.window_handles) == 1:
                self.driver.execute_script('window.open()')
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.dianjiaInformation(dianjia_urls)
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(random.uniform(2.5, 4.0))

            if 'disabled' in next_url.get_attribute('class'):
                print('no next!')
                """
                封装跳转连接
                """
            else:
                next_url.click()
                self.pageHandle()
        except Exception as e:
            print(e.args)
            self.driver.quit()

        # 店家连接
    def dianjiaInformation(self, dianjia_url):
        list_information = []
        try:
            i = 0
            while i < len(dianjia_url):
                # 申请店家页面
                self.driver.get(dianjia_url[i])
                wait = WebDriverWait(self.driver, 4, 2)
                if self.driver.current_url != dianjia_url[i]:
                    time.sleep(4)
                    """###验证模块
                    # hukuai = wait.until(
                    #     EC.presence_of_element_located((By.ID, 'yodaBox')))
                    # print(hukuai.size)
                    # ActionChains(self.driver).click_and_hold(hukuai).perform()
                    # i = 0
                    # # 模拟缓慢的滑动
                    #
                    # while i <= 2000:
                    #     time.sleep(0.2)
                    #     ActionChains(self.driver).move_by_offset(40,33).perform()
                    #     i += 5
                    # # 释放鼠标
                    # ActionChains(self.driver).release().perform()
                    """
                    # time.sleep(2)
                    while True:
                        if self.driver.current_url == dianjia_url[i]:
                            time.sleep(2)
                            break
                        else:
                            time.sleep(20)
                # 店家页面详情

                details = wait.until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section/div/div[2]')))

                name = details.find_element_by_xpath('./div[1]/div[1]').text.split('\n')                    # 店家名字
                newname = name[0].strip() if len(name) == 1 else name[1].strip()
                address = details.find_element_by_xpath('./div[1]/div[3]/p[1]').text.split('：')[1].strip()  # 店铺地址
                tel = details.find_element_by_xpath('./div[1]/div[3]/p[2]').text.split('：')[1].strip()      # 电话
                one_images = details.find_element_by_xpath('./div[2]/div/div/img').get_attribute('src')      # 第一张图
                imagesList = details.find_elements_by_xpath('./div[2]/ul//li/div')                           # 其余四张
                image_list = [newname, address, tel, one_images]
                for image in imagesList:
                    image_list.append(image.find_element_by_xpath('./img').get_attribute('src'))
                list_information.append(image_list)
                print(list_information)
                time.sleep(random.uniform(4.0, 5.0))    # 随机休眠
                i += 1
            self.write_excel(list_information)
        except Exception as e:
            print(e.args)
            self.write_excel(list_information)
            self.driver.quit()

    def write_excel(self, dataList):
        self.excel.createrWookbook()
        self.excel.pandas_insert(data=dataList)
