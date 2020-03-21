# coding:utf-8

a1=1
a2=5
a3=10
a4=25

money=raw_input("please input a coin: ")
while int(money)>100 or int(money) <=0:
　　money=raw_input("please input a coin: ")
money=int(money)
for i in range(101):
　　for j in range(21):
　　　　for k in range(11):
　　　　　　for l in range(5):
　　　　　　　　money_end=l*25+k*10+j*5+i*1
　　　　　　　　if money_end==money:
　　　　　　　　　　print i ,j ,k ,l
　　　　　　　　　　break
　　　　　　if money_end==money:
　　　　　　　　break
　　　　if money_end==money:
　　　　　　break
　　if money_end==money:
　　　　break
print "you can use this way: %d 25coin %d 10coin %d 5coin %d 1coin" % (l,k,j,i)
