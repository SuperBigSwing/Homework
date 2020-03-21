import random
N=random.randint(2,100)
lis=[]
for i in range(N):
　　n=random.randint(0,230)
　　lis.append(n)
lis2=[]
for i in range(N):
　　lis2.append(lis[random.randint(0,N-1)])
lis2.sort()
print lis2
