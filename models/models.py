# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base  # 用來創建模型繼承父類
from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, DECIMAL, DATETIME  # 大整型,變長字符串類型，浮點型， 日期時間
from sqlalchemy import Column  # 用來創建模型字段
# from models.configs import mysql_configs  # 導入mysqL連接配置

# 定義父類
Base = declarative_base()

# 創建元類
metadata = Base.metadata

"""
設計bootstrap主題產品模型
分析字段:
    1.編號, id, 大整型(bigint), 主鍵(auto_increment key)，自動遞增
    2.標題, title, 字符串, 非空
    3.封面, logo, 字符串, 非空
    4.詳情地址, url, 字符串, 非空
    5.預覽地址, preview, 字符串, 非空
    6.分類, cate, 字符串, 非空
    7.價格, price, 浮點型, 非空
    8.保存時間, createdAt, 日期時間, 非空
    9.修改時間, updatedAt, 日期時間, 非空

"""


# 創建模型
class BsThemeProduct(Base):
    # 指定數據表原始名稱
    __tablename__ = "bs_theme_product"
    id = Column(BIGINT, primary_key=True)  # 編號
    title = Column(VARCHAR(255), nullable=False)  # 標題
    logo = Column(VARCHAR(255), nullable=False)  # 封面
    url = Column(VARCHAR(255), nullable=False)  # 詳情地址
    preview = Column(VARCHAR(255), nullable=False)  # 預覽地址
    cate = Column(VARCHAR(100), nullable=False)  # 分類
    price = Column(DECIMAL(6, 2), nullable=False)  # 價格
    createdAt = Column(DATETIME, nullable=False)  # 保存時間
    updatedAt = Column(DATETIME, nullable=False)  # 修改時間


# 如果程序結構等於自己
if __name__ == "__main__":
    import mysql.connector  # 導入數據庫連接驅動
    from sqlalchemy import create_engine  # 導入創建連接引擎函數

    # 創建連接引擎
    """
    數據庫配置
    db_host: 主機名稱
    db_port: 端口
    db_user: 用戶名
    db_pwd: 密碼
    db_name: 數據庫名稱
    
    創建引擎參數
    第一項參數: 連接字符串
    encoding: 編碼
    echo: 是否輸出日誌, True輸出, False不輸出
    """
    mysql_configs = dict(
        db_host="127.0.0.1",
        db_port=3306,
        db_user="root",
        db_pwd="f3310453",
        db_name="spider_data"
    )

    engine = create_engine(
        "mysql+mysqlconnector://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}".format(
            **mysql_configs
        ),
        encoding="utf-8",
        echo=True
    )
    # 將模型生成數據表
    metadata.create_all(engine)
    print("**********恭喜你，創建成功! **********")
