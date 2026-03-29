import requests
from bs4 import BeautifulSoup
import json
url = "https://www.weather.com.cn/weather/101010100.shtml"
h = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}
res = requests.get(url=url,headers=h)
res.encoding = "utf-8" # 字符编码格式
# print(res.text)
data = BeautifulSoup(res.text,"html.parser") # 解析标签
day = data.find_all("li",class_="sky")
daylist = []
for i in day: # 循环标签里的数据
    riqi = i.find("h1").text  # 日期
    # print(riqi)
    tianqi = i.find("p",class_="wea").text # 天气
    # print(tianqi)
    max = i.find("p",class_="tem").find("span").text # 最高温度
    # print(max)
    min = i.find("p",class_="tem").find("i").text # 最低温度
    # print(min)
    # 汇总
    info = {
        "日期":riqi,
        "天气":tianqi,
        "最高气温":max,
        "最低气温":min
    }
    daylist.append(info)
# print(daylist)
with open("7天天气信息.json","w",encoding="utf-8") as f:
    json.dump(daylist,f,ensure_ascii=False)
print("执行完毕")