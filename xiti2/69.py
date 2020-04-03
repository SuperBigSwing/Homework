# coding:utf-8

def time():
    time1 = int(input('please input time number'))
    if time1 < 60:
        print('0'+str(time1))
    else:
        (i,j) = divmod(time1,60)
        print(str(i)+":"+str(j))
time()
