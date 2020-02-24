# -*- coding: UTF-8 -*-

import unittest

from chinese_clock import chinese2digits

date_map ={0:'〇',1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九'}

class ClockTest(unittest.TestCase):

 def test_chinese2digits(self):
  num =[1 ,25 ,15 ,10 ,20 ]
  for i in range(0,4):
    store = ['一','二十五','十五','十','二十']
    result = chinese2digits(num,'i')
    self.assertEqual('result','store[i]')

if __name__=="__main__":
 unittest.main()
