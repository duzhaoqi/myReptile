from bs4 import BeautifulSoup


htmlx="""
<html>
<head>
<title>hahah</title>
</head>
<body>
<div>
    <ul>
        <li class="item-0"><a href="www.baidu.com">baidu</a>
        <li class="item-1"><a href="https://blog.csdn.net/qq_25343557">myblog</a>
        <li class="item-2"><a href="https://www.csdn.net/">csdn</a>
        <li class="item-3"><a href="https://hao.360.cn/?a1004">hao123</a>
    </ul>
</div>
</body>
</html>
"""

soup = BeautifulSoup(htmlx,'lxml')

print(soup.prettify())

print(soup.title)
print(soup.a)
print(soup.head)
print(soup.head.string)
print(soup.ul)

print(soup.li.attrs)
print(soup.li["class"][0])
print(soup.li.string)