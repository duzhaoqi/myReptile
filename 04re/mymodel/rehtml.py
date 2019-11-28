import requests
import re

def down(url):
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
    reponse = requests.get(url,headers)
    html = reponse.text
    #html = reponse.content.decode('gb2312')
    return html

def get_title(html):
    ret = re.compile(r'<title>(.*?)</title>',re.M|re.S)
    obj = ret.search(html)
    title = obj.group(1)
    print(title)


def get_a(html):
    ret = re.compile(r'<a .*?>(.*?)</a>',re.M|re.S)
    return ret.findall(html)

def get_table(html):
    ret = re.compile(r'<td .*?>(.*?)</td>\n<td .*?><(.*?)></td>',re.M|re.S)
    return ret.findall(html)


def get_href(html):
    ret = re.compile(r'<a href="(.+?)" .*?>(.*?)</a>',re.M|re.S)
    return ret.findall(html)