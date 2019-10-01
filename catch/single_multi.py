# -*- coding: utf-8 -*-
import time  # 導入時間庫
import datetime  # 導入日期時間庫
from multiprocessing.dummy import Pool
from multiprocessing import  cpu_count

"""
1.對比單進程與多進程執行時間

"""


# 定義一個返回日期時間函數
def dt():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# 運行函數
def run(v):
    print("{}:[{}]開始運行".format(dt(), str(v).zfill(2)))
    time.sleep(2)  # 休息兩秒
    print("{}:[{}]結束運行".format(dt(), str(v).zfill(2)))


# 單進程串型方式運行
def single():
    for v in range(0, 16):
        run(v)


# 多進程串型方式運行
def multi():
    # 判斷cpu核心數量,
    # 根據cpu核心數量來開啟多進程
    # 以進程池的方式來運行函數
    n = cpu_count()
    # 創建進程池
    p = Pool(n)
    for v in range(0, 16):
        p.apply_async(run, args=(v,))  #以進程池方式非同步運行函數，第一個參數函數名稱，args參數元祖
    p.close()  # 關閉進程池
    p.join()  # 等待進程結束


if __name__ == "__main__":
    star_time = time.time()
    # single()
    multi()
    print("總計用時：{}s".format(time.time() - star_time))