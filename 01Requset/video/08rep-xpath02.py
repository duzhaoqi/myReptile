from lxml import etree
import requests
import random
from time import sleep
import pymysql





def down(url):
    headers = {}
    headers["User-Agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/78.0.3904.97 Safari/537.36"
    reponse = requests.get(url,headers=headers)
    html = reponse.content.decode('utf-8')
    return html

def parase(html):
    html = etree.HTML(html)
    ls = html.xpath('//li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
    print("这是第{}页,本页有{}个: ".format(page_num,len(ls)))
    for item in ls:
        link = item.xpath('.//div[@class="info clear"]/div[@class="title"]/a/@href')[0]
        detail_html = down(link)
        detail_html = etree.HTML(detail_html)

        title = detail_html.xpath('.//div[@class="title"]/h1[@class="main"]/text()')[0]
        try:
            total_price = detail_html.xpath('.//div[@class="price "]/span[@class="total"]/text()')[0]
        except IndexError:
            total_price='0'
        try:
            unit_price = detail_html.xpath('.//div[@class="unitPrice"]/span[@class="unitPriceValue"]/text()')[0]
        except IndexError:
            unit_price='0'
        community_name = detail_html.xpath('.//div[@class="communityName"]/a[@class="info "]/text()')[0]

        area01 = detail_html.xpath('.//div[@class="areaName"]/span[@class="info"]/a/text()')[0]
        area02 = detail_html.xpath('.//div[@class="areaName"]/span[@class="info"]/a/text()')[1]
        try:
            area03 = detail_html.xpath('.//div[@class="areaName"]/a[@class="supplement"]/text()')[0]
        except IndexError as f:
            position_info = area01+" "+area02
        else:
            position_info = area01+" "+area02+" "+area03

        house_record = detail_html.xpath('.//div[@class="houseRecord"]/span[@class="info"]/text()')[0]

        base=detail_html.xpath('.//div[@class="base"]/div[@class="content"]/ul/li')


        house_type = base[0].xpath('./text()')[0]
        pos_floor = base[1].xpath('./text()')[0]
        area_size = base[2].xpath('./text()')[0]
        house_structure = base[3].xpath('./text()')[0]
        area_in = base[4].xpath('./text()')[0]
        build_type = base[5].xpath('./text()')[0]
        house_direction = base[6].xpath('./text()')[0]
        build_structure = base[7].xpath('./text()')[0]
        dec_status = base[8].xpath('./text()')[0]
        ele_per = base[9].xpath('./text()')[0]
        try:
            heating_type = base[10].xpath('./text()')[0]
        except IndexError:
            heating_type='None'
        try:
            is_ele = base[11].xpath('./text()')[0]
        except IndexError:
            is_ele='None'
        try:
            house_property = base[12].xpath('./text()')[0]
        except IndexError:
            house_property='None'

        ls1 = [house_record,community_name,position_info,total_price,unit_price,link,title]
        ls2 = [house_type,pos_floor,area_size,house_structure,area_in,build_type,house_direction,build_structure,dec_status,ele_per,heating_type,is_ele,house_property]
        ls1.extend(ls2)
        saveDate(ls1)


def saveDate(list):

    # with codecs.open('./data/lianjia-b.csv','a',encoding='utf-8') as csv_w:
    #     wr = csv.writer(csv_w)
    #     wr.writerow(list)
    strSql = 'insert into lianjia_info VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cur.execute(strSql,list)
    conn.commit()


if __name__ == "__main__":
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='eos',password='duzhaoqi2015',db='eos')
    cur = conn.cursor()
    page_num = 0
    for page in range(1,100):
        page_num += 1
        if page == 1:
            url='https://zz.lianjia.com/ershoufang/'
        else:
            url='https://zz.lianjia.com/ershoufang/pg{}/'.format(str(page))
        html = down(url)
        parase(html)
        sleep(random.random()*2)








        # print("标题:",title)
        # print("总价:",total_price)
        # print("平米价:",unit_price)
        # print("小区:",community_name)
        # print("位置:",position_info)
        # print("链家编号:",house_record)
        # print("链接地址:",link)
        #
        # print("房屋户型:",house_type)
        # print("所在楼层:",pos_floor)
        # print("建筑面积:",area_size)
        # print("房屋结构:",house_structure)
        # print("套内面积:",area_in)
        # print("建筑类型:",build_type)
        # print("房屋朝向:",house_direction)
        # print("建筑结构:",build_structure)
        # print("装修情况:",dec_status)
        # print("梯户比例:",ele_per)
        # print("供暖类型:",heating_type)
        # print("配备电梯:",is_ele)
        # print("房屋产权:",house_property)
