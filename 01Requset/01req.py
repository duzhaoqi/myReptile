import requests

headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
kw={"wd":"魔兽"}

try:
    response = requests.get("https://www.baidu.com/",params=kw,headers=headers,timeout=1)
    print(response.status_code)
    #content 返回字节流数据
    # print(response.content.decode("UTF-8"))
    print(response.url)
    # print(response.encoding)
    # print(response.headers)
    print(response.request.headers)
except Exception as e:
    print(e)
