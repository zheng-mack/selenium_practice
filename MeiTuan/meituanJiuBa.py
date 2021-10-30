import re
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from toExcel import createtrExcel


class jiuba:
    def __init__(self, driver):
        """
        : return list_information:店铺信息列表[店名，地址，电话，图片1...5]
        """
        self.HTTP = 'https:'
        self.driver = driver
        self.excel=createtrExcel('美团', '玩乐')

    def pageHandle(self):
        try:
            dianjia_urls=[]
            wait = WebDriverWait(self.driver, 4, 2)
            # 获取下一页连接
            next_url = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'next-btn')))

            # 获取店家连接
            dianjia_url=wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'list-item-desc-top')))

            for d in dianjia_url:
                dianjia_urls.append(d.find_element_by_xpath('./a').get_attribute('href'))
            # 切换窗口
            if len(self.driver.window_handles) == 1:
                self.driver.execute_script('window.open()')
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.dianjiaInformation(dianjia_urls)
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(random.uniform(2.5,4.0))

            if 'active' in next_url.get_attribute('class'):
                next_url.click()
                self.pageHandle()
            else:
                print('no next!')

        except Exception as e:
            print('1',e.args)
            self.driver.quit()

    def dianjiaInformation(self, dianjia_url):
        try:
            list_information = []
            i = 0
            while i < len(dianjia_url):
                # 申请店家页面
                self.driver.get(dianjia_url[i])
                # 店家页面详情
                wait = WebDriverWait(self.driver, 4, 2)

                details = wait.until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'poi-detail')))
                name = details.find_element_by_xpath('./div[1]/h1').text                                         # 店家名字
                address = details.find_element_by_xpath('./div[1]/div[2]/div[1]/a/span').text                    # 店铺地址
                tel = details.find_element_by_xpath('./div[1]/div[2]/div[2]/span[2]').text                       # 电话
                one_images = details.find_element_by_xpath('./div[2]/div/div[1]/div[1]').get_attribute('style')  # 第一张图
                one_image = re.findall('background-image: url(.*?);', one_images)[0]

                imagesList = details.find_elements_by_xpath('./div[2]/div/div[2]/div[3]/div//div')  # 其余四张
                image_list = [name, address, tel, one_image]
                for image in imagesList:
                    image_list.append(re.findall('background-image: url(.*?);', image.get_attribute('style'))[0])
                list_information.append(image_list)
                time.sleep(random.uniform(3.5, 5.0))  # 随机休眠
                i += 1
            self.write_excel(list_information)
        except Exception as e:
            print(e.args)
            self.write_excel(list_information)
            self.driver.quit()

    def write_excel(self, dataList):
        self.excel.createrWookbook()
        self.excel.pandas_insert(data=dataList)
