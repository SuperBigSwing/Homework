# coding:utf-8

list = raw_input["请输入一组数字："]
for i in list:
    if list.count(i) > 1:
        print(str(i)+'出现多次')
    else:
        print(str(i)+'没有重复出现')
