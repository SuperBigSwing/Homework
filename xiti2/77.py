# coding:utf-8

dict_test1 = {1:'a',2:'b',3:'c'}
dict_test2 = {}
for key in dict_test1:
    dict_test2.setdefault(dict_test1[key],key)
    
print dict_test2
