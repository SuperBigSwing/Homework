# coding:utf-8

gongshi=raw_input("请输入公式（单公式不能累加，例如只能1+2,不能1+2+3）： ")
for i in range(len(gongshi)):
　　coporate=gongshi[i]
　　if coporate not in['0','1','2','3','4','5','6','7','8','9']:
　　　　print "操作符为："+coporate
　　　　break
if gongshi[i] not in['+','-','*','/','%','^']:
　　print "你输入的公式有误，请重新运行程序并正确输入公式。。"
　　exit()
num=gongshi.split(gongshi[i])
print num[0],num[1]
temp_num =list(gongshi)
temp_num.remove(coporate)
if coporate == '+':
　　print "计算结果为：" + gongshi + "=" + str(float(num[0])+float(num[1]))
elif coporate == '-':
　　print "计算结果为：" + gongshi + "=" + str(float(num[0])-float(num[1]))
elif coporate == '*':
　　print "计算结果为：" + gongshi + "=" + str(float(num[0])*float(num[1]))
elif coporate == '/':
　　print "计算结果为：" + gongshi + "=" + str(float(num[0])/float(num[1]))
elif coporate == '%':
　　print "计算结果为：" + gongshi + "=" + str(float(num[0])%float(num[1]))
elif int(float(num[1]))==float(num[1]):
　　print "计算结果为：" + gongshi + "=" + str(float(num[0])**float(num[1]))
else:
　　print "乘方计算时，指数不能为小数,请重新运行程序并正确输入公式。"
