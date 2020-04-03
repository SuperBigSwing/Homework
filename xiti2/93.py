# coding:utf-8

F=raw_input('pls input a file name:')
f=open(F,'r')
alllines=f.readlines()
f.close()
print len(alllines)
