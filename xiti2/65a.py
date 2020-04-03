# coding:utf-8

wode = input('请输入文字')
l = len(wode)
x = 0
while x <= l-1:
    print(wode[x])
    x += 1
for i in wode:
    print(i)
for i in wode[::-1]:
    print(i)
