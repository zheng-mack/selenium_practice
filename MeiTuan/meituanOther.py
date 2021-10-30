from toExcel import createtrExcel
import re


class MeiTuanOther:
    def __int__(self, driver):
        self.driver = driver
        self.excel = createtrExcel('美团', '其他')

    def huoqu_dp(self):  # 获取除了美食，结婚，酒吧以外的店铺连接
        meun = self.driver.find_elements_by_xpath('//div[@class="abstract-item"]//a')
        xxjs_dianpu = []
        for meun in meun:
            xxjs_dianpu.append(meun.get_attribute("href"))
        return xxjs_dianpu  # 返回店铺的连接

    def huoquxx_xxjs(self):  # 获取休闲娱乐和健身的信息
        xxjs_dianpu = self.huoqu_dp()
        self.driver.get(xxjs_dianpu[0])
        name = self.driver.find_element_by_xpath('//h1[@class="seller-name"]').text
        address = self.driver.find_element_by_xpath('//div[@class="seller-info-body"]/div[1]/a/span').text
        tel = self.driver.find_element_by_xpath('//div[@class="seller-info-body"]/div[2]/span[2]').text
        one_images = self.driver.find_element_by_xpath('//div[@class="now-img"]').get_attribute("style")
        two_images = self.driver.find_element_by_xpath('//div[@class="album-ul"]/div[1]').get_attribute("style")
        three_images = self.driver.find_element_by_xpath('//div[@class="album-ul"]/div[2]').get_attribute("style")
        four_images = self.driver.find_element_by_xpath('//div[@class="album-ul"]/div[3]').get_attribute("style")
        five_images = self.driver.find_element_by_xpath('//div[@class="album-ul"]/div[4]').get_attribute("style")
        images = [one_images, two_images, three_images, four_images, five_images]
        for i in range(5):
            images[i] = re.match(r'background-image: url\("(.*?)"\);', images[i]).group(1)
            print(images[i])
        print(name, address, tel, images)

        self.write_excel([name, address, tel]+images)

    def huoquxx_Cxxjs(self):
        xxjs_dianpu = self.huoqu_dp()
        self.driver.get(xxjs_dianpu[0])
        name = self.driver.find_element_by_xpath('//h1[@class="seller-name"]').text
        address = self.driver.find_element_by_xpath('//div[@class="seller-info-body"]/div[1]/a/span').text
        tel = '无联系方式'
        one_images = self.driver.find_element_by_xpath('//div[@class="now-img"]').get_attribute("style")
        two_images = self.driver.find_element_by_xpath('//div[@class="album-ul clearfix"]/div[1]').get_attribute("style")
        three_images = self.driver.find_element_by_xpath('//div[@class="album-ul clearfix"]/div[2]').get_attribute("style")
        four_images = self.driver.find_element_by_xpath('//div[@class="album-ul clearfix"]/div[3]').get_attribute("style")
        five_images = self.driver.find_element_by_xpath('//div[@class="album-ul clearfix"]/div[4]').get_attribute("style")
        images = [one_images, two_images, three_images, four_images, five_images]
        for i in range(5):
            images[i] = re.match(r'background-image: url\("(.*?)"\);', images[i]).group(1)
            print(images[i])
        print(name, address, tel, images)
        self.write_excel([name, address, tel]+images)

    def write_excel(self, dataList):
        self.excel.createrWookbook()
        self.excel.pandas_insert(data=dataList)
