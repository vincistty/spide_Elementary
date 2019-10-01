# -*- coding: utf-8 -*-
import os
import requests
from catch.spider_single import SpiderSingle
from multiprocessing.dummy import Pool
from multiprocessing import cpu_count


# 多進程爬蟲類
class SpiderMulti(SpiderSingle):
    # 執行請求的方法
    def catch_page_process(self, url, n):
        # 1.定義請求響應對象
        resp = requests.request(method="GET", url=url)

        # 2.判斷創建保存目錄
        if not os.path.exists(self.path):
            os.mkdir(self.path)

        # 3.保存抓取響應內容
        resp.encoding = "utf-8"
        save_path = os.path.join(self.path, "{}.html".format(n))
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(resp.text)
        # 4.輸出抓取日志
        self.log(resp.url, save_path)

    # 多進程的方法
    def catch_pages(self):
        cpu_num = cpu_count()  # 獲取cpu數量
        p = Pool(cpu_num)  # 定義進程池
        n = 1
        for url in self.urls:
            p.apply_async(self.catch_page_process, args=(url, n))  # 以進程池的方式運行請求方法
            n += 1
        p.close()  # 關閉
        p.join()  # 等待