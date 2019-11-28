
from mymodel.rehtml import down,get_title,get_a,get_table,get_href



if __name__ == "__main__":
    url = 'https://fanyi.baidu.com'
    html = down(url)
    get_title(html)

    url = 'https://www.baidu.com'
    html= down(url)
    x  = get_a(html)
    print(x)

    url='http://www.ttlsa.com/zabbix/zabbix-create-trigger/'
    #html= down(url)
    #print(html)
    #x  = get_table(html)
    #print(x)


    url = 'http://www.chinamedevice.cn/product/1212/1/1.html'
    html= down(url)
    x  = get_href(html)
    print(x)