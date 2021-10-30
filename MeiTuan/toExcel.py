""" excel"""
import pandas as pd
import os


class createtrExcel():
    """
        @请不要在excel打开的时候进行插入操作
    """
    def __init__(self, filename, sheetname):
        """
        :param filename:excel名字
        :param sheetname: 表名
        """
        self.filename = r'./' + filename + '.xlsx'
        self.sheetname = sheetname

    def createrWookbook(self):
        if os.path.exists(self.filename) is False:
            print('创建', self.filename)
            df = pd.DataFrame(columns=["店铺名", "店铺地址", '联系', '图一', '图片二', '图片三', '图片四', '图片五', ])
            df.to_excel(self.filename, index=False, sheet_name=self.sheetname)

    # def addSheet(self):
    #     df = pd.DataFrame()
    #     book = load_workbook(self.filename)
    #     writer = pd.ExcelWriter(self.filename, engine='openpyxl')
    #     writer.book = book
    #     df.to_excel(writer, self.sheetname)
    #     writer.save()

    def pandas_insert(self,data):
        """
        :param data:列表页面数据存进二维list里，如[[店1]，[店2]，[店3]，[店4]....]
        :return:
        """
        table = pd.read_excel(self.filename, sheet_name=self.sheetname, engine='openpyxl', keep_default_na=False)
        d1 = pd.DataFrame(data, columns=["店铺名", "店铺地址", '联系', '图一', '图片二', '图片三', '图片四', '图片五', ])
        # columns=["店铺名", "店铺地址",'联系','图一','图片二','图片三','图片四','图片五',],
        d1.fillna('NaN')
        df_new = pd.concat([table, d1], ignore_index=True, )
        df_new.to_excel(self.filename, sheet_name=self.sheetname, index=False, header=True)
