import re

ret = re.match('[A-Z][a-z]a*','Chinaaaaaaaaaaa')
print(ret.group())

ret = re.match('[A-Z][a-z]*?a*','Chinaaaaaaaaaaa')
print(ret.group())

ret = re.match('[A-Z][a-z]*?a','Chinaaaaaaaaaaa')
print(ret.group())

ret = re.match('[a-zA-Z0-9_]+','__init__')
print(ret.group())


ret = re.match('^\w{4,22}@163\.com$','duzhaoqi@163.com')
print(ret.group())


ret = re.match(r'<(\w+)><(\w+)>.+</\2></\1>','<html><h1>www.qq.com</h1></html>')
print(ret.group())


ret = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>.+</(?P=name2)></(?P=name1)>','<html><h1>www.qq.com</h1></html>')
print(ret.group())


s = """first line
second line
third line"""

regex = re.compile(r'.+')
print(regex.findall(s))
print(regex.match(s).group())

regex = re.compile(r'.+',re.S)
print(regex.findall(s))
print(regex.match(s).group())

print("====================")

regex = re.compile(r'\d+')
s = 'one12twothree34four'

m = regex.match(s)
print(m)

m = regex.match(s,3,18)
print(m.group())

print(m.start())
print(m.end())
print(m.span())


m = regex.search(s)
print(m.group())
m = regex.search(s,5,18)
print(m.group())
print(m.span())



