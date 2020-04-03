# coding:utf-8

def stringqu():
    x = 0
    num1 = input('''please input a number\n''')
    y = int(len(num1))
    z = y
    for i in range(y):
        if num1[i] == " ":
            x += 1
        else:
            break
    for j in range(y):
        if num1[-j] == " ":
            z -= 1
        else:
            break
    right_str = num1[x:z]
    print(right_str)
stringqu()
