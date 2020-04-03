# coding:utf-8

N=int(raw_input('pls input a number:'))
F=raw_input('pls input a file name:')
f=open(F,'r')
alllines=f.readlines()
f.close()
for i in range(N):
    print alllines[i]
