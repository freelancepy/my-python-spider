import requests
from lxml import etree
import pandas

h = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
    "cookie": "buvid3=7F0FD658-E73C-26CF-F2DB-4855DDACF0CD99164infoc; b_nut=1770106399; _uuid=9D5B2BEE-4646-357F-33EC-BF58C4EFA110200588infoc; buvid4=FE9A0FE8-4EE0-F104-64AC-0DC3B5E7789399809-026020316-jI3d0cR19eZFpJCyTwDbZAHKEtRHGx7qXslTjepnnCK9lQKQQ6AbqgG3uUJFBY07; buvid_fp=b18da68462a6c1a0ecce70ed1d46a54c; home_feed_column=5; CURRENT_QUALITY=0; rpdid=0zbfvSgdr5|1apr6uZ8|3O6|3w1VP0kc; bsource=search_baidu; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzM1NTkyMzYsImlhdCI6MTc3MzI5OTk3NiwicGx0IjotMX0.xvbIAo_W8GVHwXitimoft1fJQbuvOEZPvA9WoPzM9oc; bili_ticket_expires=1773559176; sid=5kohjq1l; ogv_device_support_hdr=0; ogv_device_support_dolby=0; browser_resolution=1600-865; CURRENT_FNVAL=4048; b_lsid=F73C2578_19CE1096386",
    "referer": "https://www.autohome.com.cn/ziyang/"
}
k_list = []

for i in range(1,4):
    url = f"https://www.autohome.com.cn/price/fueltypedetail_1-levelid_101-price_8_10/x-x-x-x-{i}"
    # print(url)
    res = requests.get(url=url,headers=h)
    # print(res.text)
    data = etree.HTML(res.text)
    datas = data.xpath('//div[@class="tw-mb-[30px]"]/div')
    # print(len(datas))

    for w in datas:
        name = w.xpath('.//a/text()')[0]    # 车名
        # print(name)
        jie_gou = w.xpath('.//div[@class="tw-flex tw-flex-wrap tw-items-center tw-justify-between"]/a/span[2]/text()')[0]   #级别/车身结构
        # print(jie_gou)
        fa_dj = w.xpath('.//div[@class="tw-flex tw-flex-wrap tw-items-center tw-justify-between"]/a/span[2]/text()')[1]     #发动机
        fa_d_j =fa_dj.split("/")[0]
        # print(fa_d_j)
        bsx = w.xpath('.//div[@class="tw-flex tw-flex-wrap tw-items-center tw-justify-between"]/a/span[2]/text()')[1].split("/")[1]     #变速箱
        # print(bsx)
        price = w.xpath('.//div[@class="tw-mb-2.5 tw-flex tw-items-center tw-whitespace-nowrap tw-text-sm tw-text-[#828CA0]"]/a/text()')[0]   # 指导价
        # print(price)
        min_price = price.replace("万","").strip().split("-")[0]
        max_price = price.replace("万","").strip().split("-")[1]

        # 保存为xlsx文件
        k_dict = {
            "车名":name,
            "级别/车身结构":jie_gou,
            "发动机":fa_d_j,
            "变速箱":bsx,
            "最低指导价":min_price,
            "最高指导价":max_price
        }
        k_list.append(k_dict)
        df = pandas.DataFrame(k_list)
        df.to_excel("燃油轿车8-10万.xlsx",index=False)

print("执行完毕")

