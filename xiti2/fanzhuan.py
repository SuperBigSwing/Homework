# coding:utf-8

def fanzhuan():
    xiaoxie = 'qwertyuiopasdfghjklzxcvbnm'
    daxie = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str1 = input('please input your string')
    x = len(str1)
    str2 = []
    str3 = ""
    for i in range(x):
        if str1[i] in xiaoxie:
            str2.append(str1[i].upper())
        elif str1[i] in daxie:
            str2.append(str1[i].lower())
        else:
            str2.append(str1[i])
    for j in str2:
        str3 += str(j)
    print(str3)
