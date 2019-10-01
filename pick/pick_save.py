#  -*- coding: utf-8 -*-
import os
import datetime
import mysql.connector
from lxml import etree
from models.configs import mysql_configs
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker  # 會話創建工具
from models.models import BsThemeProduct  # 導入模型


class PickSave:
    # 定義初始化的構造方法
    def __init__(self, path):
        self.path = path  # 把路徑賦值實例屬性self.path
        self.db = self.session

    # 定義連接會話(與mysql連接)
    @property
    def session(self):
        # 創建連接mysql引擎
        engine = create_engine(
            'mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'.format(
                **mysql_configs
            ),
            encoding="utf-8",
            echo=True,
            pool_size=100,
            pool_recycle=10,
            connect_args={'charset': 'utf8'}
        )  # pool_size: 連接池的大小 pool_recycle: 連接池生命週期 connect_args: 連接選項

        # 定義會話
        Session = sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=True,
            expire_on_commit=False
        )
        # bind:綁定連接引擎;
        # autocommit: True 自動提交, False 事務提交;
        # autoflush: True自動刷新權限，False 不自動;
        # expire_on_commit: True 自動提交, False 事務提交
        return Session()

    # 解析數據
    def pick(self):
        # 1.獲取抓取所有的html
        html_list = os.listdir(self.path)
        # print(html_list)
        data = []
        # 2.拼接路徑和html
        for html in html_list:
            html_path = os.path.join(self.path, html)
            # print(html_path)
            # 3.打開html
            with open(html_path, "r", encoding="utf-8") as f:
                # print(f.read())
                # 把html內容轉化為節點選擇企
                selector = etree.HTML(f.read())
                # print(selector)
                # 定義細胞選擇器
                items = selector.xpath('//div[@id="content"]/ul/li/div')
                # print(items)
                for item in items:
                    data.append(
                        dict(
                            title=str(item.xpath('div[2]/div[1]/a/text()')[0]),
                            logo=str(item.xpath('div[1]/a[1]/img/@src')[0]),
                            url=str(item.xpath('div[1]/a[1]/@href')[0]),
                            preview=str(item.xpath('div[1]/a[2]/@href')[0]),
                            cate=str(item.xpath('div[2]/div[1]/ul/li/a/text()')[0]),
                            price=float(item.xpath('div[2]/div[2]/p/span/text()')[0]),
                        )
                    )
        return data

    @property
    def dt(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 保存數據
    def save(self):
        # 事務處理的邏輯
        try:
            # 執行代碼塊
            # 獲取數據
            data = self.pick()
            for v in data:
                cd = dict(
                    createdAt=self.dt,
                    updatedAt=self.dt,
                    **v
                )
                bs_theme_product = BsThemeProduct(
                    **cd
                )
                self.db.add(bs_theme_product)  # 添加數據至數據庫中
        except Exception as e:
            # 出現異常代碼塊
            print(e)
            self.db.rollback()  # 回滾
        else:
            # 沒有出現異常代碼塊
            self.db.commit()  # 提交
        finally:
            # 無論是否發生異常都執行的代碼塊
            self.db.close()  # 關閉會話