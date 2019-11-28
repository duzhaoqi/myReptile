import requests
import re

def down(url):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}
    reponse=requests.get(url,headers=headers)
    html = reponse.content.decode('utf-8')
    return html


if __name__ == "__main__":
    url="https://www.neihan-8.com/wenzi/"
    html = down(url)
    print(html)