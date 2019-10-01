# -*- coding: utf-8 -*-

# Python 編碼默認是ascii格式，沒修改編碼的情況下無法編寫中文，所以中文會報錯，解決方式就是將ascii改成utf-8

import os  # 導入文件目錄操作庫
import datetime  # 導入日期時間庫
import requests  # 導入http客戶端庫

"""
1.requests http 客戶端請求庫怎麼用 ?
以 Google : http://www.google.com為例

url = "http://www.google.com"

#  定義請求，請求結果賦值響應對象
#  method:　請求方法
#  url: 請求地址
response = requests.request(method="GET", url=url)
print(response)  # 印出響應對象
print(dir(response))  # 響應對象可以調用的屬性與方法
#  response.text # 響應的內容
print(response.text)
#  response.encoding # 響應的字符集
print(response.encoding)
#  response.headers # 響應的頭信息
print(response.headers)
#  response.status_code # 響應的狀態碼
print(response.status_code)
#  response.cookies # 響應的會話信息
print(response.cookies)

#  怎麼把響應內容裡面的亂碼轉化為正常字符
response.encoding = "utf-8"
print(response.text)
"""

"""
2.封裝單進程爬蟲
"""


class SpiderSingle(object):
    #  定義一個初始化的構造方法
    #  1.urls地址生成器, 2.保存html目錄
    def __init__(self, urls, path):
        self.urls = urls  # 把urls賦值給self.urls這個實例屬性
        self.path = path  # 把path賦值給self.path這個實例屬性

    # 創建打印日志方法
    def log(self, url, save_path):
        # %Y: 年 %m: 月 %d:日 %H: 時　%M:分　%S：秒
        print("{dt}:{url}->{save_path}".format(
                dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                url=url,
                save_path=save_path
        ))

    # 單進程爬取頁面的邏輯
    def catch_pages(self):
        # 1.定義請求的生成器
        resps = (
            requests.request(method="GET", url=url) for url in self.urls
        )

        # 2. 判斷並創建保存html的路徑
        if not os.path.exists(self.path):
            os.mkdir(self.path)

        # 3.迭代請求生成器, 把響應內容保存到html中，再把html保存到保存目錄中
        n = 1
        for resp in resps:
            resp.encoding = "utf-8"  # 設置響應內容的編碼為utf-8
            save_path = os.path.join(
                self.path,
                "{}.html".format(
                        n
                )
            )  # 拼接保存目錄路徑和html的名稱
            # 以寫的方式，字符集為utf-8打開html
            with open(save_path, "w", encoding="utf-8") as f:
                # 寫入響應的內容
                f.write(resp.text)
            self.log(resp.url, save_path)
            n += 1  # 每次循環迭代的時候，n遞增
