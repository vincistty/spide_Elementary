# -*- coding: utf-8 -*-
import os  # 導入文件目錄操作
from catch.spider_single import SpiderSingle  # 導入單進程爬蟲類
from catch.spider_mutil import SpiderMulti  # 導入多進程爬蟲類
from pick.pick_save import PickSave  # 導入提取保存類
from pprint import pprint

if __name__ == "__main__":
    # 定義請求地址生成器
    urls = (
         "https://themes.getbootstrap.com/shop/page/{}/?orderby=popularity".format(v)
         for v in range(1, 6)
    )
    # 定義保存的路徑, os.path.dirname(__file__): 獲取當前腳本所在的路徑
    path = os.path.join(
        os.path.dirname(__file__),
        "result/bs_theme_product"
    )
    # s = SpiderSingle(urls, path)  # 實例化單進程爬蟲類
    # s.catch_pages()  # 執行單進程抓取頁面
    m = SpiderMulti(urls, path)  # 實例化多進程爬蟲類
    m.catch_pages()  # 執行多進程抓取頁面
    print("-----------------------------------------")
    ps = PickSave(path)  # 實例化類
    # pprint(ps.pick())  # 提取數據
    ps.save()  # 保存數據