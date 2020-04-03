# coding:utf-8

num1 = input('请输入数字1')
num2 = input('请输入数字2')
for i in range(len(num1)):
    if num1[i] == num2[i]:
        print('匹配成功')
    else:
        print('匹配不成功')
