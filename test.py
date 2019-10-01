#  -*- coding: utf-8 -*-
from lxml import etree  # 節點樹庫

#  打開html，讀取html內容
with open("test.html","r",encoding="utf-8") as f:
    html = f.read()
    selector = etree.HTML(html)
    print(selector)
    """
    提取標題
    提取關鍵字
    提取介紹
    提取鏈接地址
    提取圖片地址
    提取文本內容
    
    xpath路徑語法
    //忽綠上級節點
    text():獲取標籤包裹的內容
    @屬性名稱:獲取屬性內容
    """
    title = selector.xpath('//title/text()')[0]
    keywords = selector.xpath('//meta[@name="keywords"]/@content')[0]
    description = selector.xpath('//meta[@name="description"]/@content')[0]
    a = selector.xpath('//div[@id="abc"]/div[@class="efg"]/a/@href')[0]
    img = selector.xpath('//div[@id="abc"]/div[@class="efg"]/img/@src')[0]
    p = selector.xpath('//div[@id="abc"]/div[@class="efg"]/p/text()')[0]
    print(title)
    print(keywords)
    print(description)
    print(a)
    print(img)
    print(p)
