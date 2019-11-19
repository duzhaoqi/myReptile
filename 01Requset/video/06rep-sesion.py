import requests

ssion = requests.session()
headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
}
url01='http://weibo.com/a/bind/login'
data={"usernmae":"18738399739","password":"duzhaoqi2015"}
ssion.post(url01,data=data,headers=headers)

reposon = ssion.get('https://weibo.com/u/6259768047/home')

print(reposon.text)