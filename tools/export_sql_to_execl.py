import pymysql
import datetime
import os
import xlwt

"""
将数据库表的信息导入到execl表格
不完善,以后继续完善
"""


class Export:
    def __init__(self, table_name=None):
        self.host = ''
        self.password = ''
        self.user = ''
        self.port = 3306
        self.name = ''
        self.table_name = table_name

    
    def run(self):
        self.conn_mysql()
        self.exec_sql()
        self.save_execl()
        self.close_sql()

    def conn_mysql(self):
        self.conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               password=self.password,
                               db=self.name,
                               charset='utf8')
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def close_sql(self):    
        self.cur.close()
        self.conn.close()

    def exec_sql(self):
        """将查询的数据写到execl表格中
        """
        sql = f'select * from {self.table_name}'
        self.cur.execute(sql)
        self.data = self.cur.fetchall()


    def save_execl(self):
        """
        将数据保存到execl文件中
        """

        row_num = 0
        data = list()
        title_list = list(self.data[0].keys())
        for v in self.data:
            temp = list()
            for key, value in v.items():
                if isinstance(value, int) or isinstance(value, str) or isinstance(value, float):
                    temp.append(value)
                elif isinstance(value, datetime.datetime):
                    temp.append(value.strftime('%Y-%m-%d %H:%M:%S'))
                else:
                    temp.append('') # 不导入
            data.append(temp)
            
        filename = os.path.join(os.path.abspath(os.path.curdir), f'{self.table_name}.xls')
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet1 = workbook.add_sheet('Sheet1')
        
        for col in range(len(title_list)):
            sheet1.write(0, col, title_list[col])
        for vul in data:
            row_num += 1
            vul.insert(0, row_num)
            for col_num in range(len(vul)):
                sheet1.write(row_num, col_num, vul[col_num])
        workbook.save(filename)  # 保存工作簿
        print("xls格式表格写入数据成功！")
    
    
if __name__ == "__main__":
    e = Export('username')
    e.run()
