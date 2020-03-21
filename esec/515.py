# coding:utf-8
from hcf import hcf
from lcm import lcm

num3 = int(input("最大公约数请按1，最小公倍数请按2 "))
if num3 ==1: 
 num1 = int(input("输入第一个数字: "))
 num2 = int(input("输入第二个数字: "))
 print(hcf(num1, num2))
if num3 ==2:
 num1 = int(input("输入第一个数字: "))
 num2 = int(input("输入第二个数字: "))
 print(lcm(num1, num2))
