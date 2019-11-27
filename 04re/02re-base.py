import re

regex = re.compile(r'\d+')
s1 = 'one12twothree34four'
s2 = 'hello 233456.765'

m = regex.findall(s1)
print(m)

m = regex.finditer(s2)
for item in m:
    print(item.group())