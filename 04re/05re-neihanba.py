import requests
import re
from lxml import etree

def down(url):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}
    reponse=requests.get(url,headers=headers)
    html = reponse.content.decode('utf-8')
    return html

def get_data(html):
    #lv0 = re.compile(r'<div class="text-column-item box box-790">(.*?</div>.*?</div>.*?</div>.*?</div>.*?</div>).*?</div>',re.M|re.S)
    lv0 = etree.HTML(html)
    data01 = lv0.xpath("//div[@class='text-column-item box box-790']")
    for i in data01:
        print(i.xpath('./text()'))
        print('='*60)

def main(ends):
       for page in range(1,ends+1):
        if page == 1:
            url="https://www.neihan-8.com/wenzi/"
        else:
            url="https://www.neihan-8.com/wenzi/index_{}.html".format(str(page))
        
        html = down(url)
        get_data(html)
        

if __name__ == "__main__":
    ends=5
    main(ends)
 