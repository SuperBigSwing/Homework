#coding=utf-8
def Payment(x,y):
　　print "0 $ 0.00 $%.2f" %x
　　i=0
　　while x>=y:
　　　　print "%d $%.2f $ %.2f " %(i,y,(x-y))
　　　　i+=1
　　　　x=x-y
　　print "%d $%.2f $ %.2f " %(i,x,0.00)
　　pass

balance = float(raw_input("Enter opening balance:"))
payment1 = float(raw_input("Enter monthly payment:"))
if balance < payment:
　　print "Error, please run!"
　　exit()
print "Amount Remaining"
print "Pymt# Paid Balance"
print "----- ------ ---------"
Payment(balance,payment1)
