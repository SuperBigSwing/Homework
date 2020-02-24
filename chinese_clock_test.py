# -*- coding: UTF-8 -*-

import unittest

from chinese_clock import chinese2digits

class ClockTest(unittest.TestCase):

 def test_chinese2digits(self):
  num =[1 ,25 ,15 ,10 ,20 ]
  for i in range(len(num)):
    store = ['一','二十五','十五','十','二十']
    self.assertEqual('chinese2digits(num,i)','store[i]')

unittest.main()
