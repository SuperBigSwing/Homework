# -*- coding: utf-8 -*-
import datetime
date_map ={0:'〇',1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九'}

def chinese2digits(num,type):
 str_num = str(num)
 result = ''
 if type == 0:
  for i in str_num:
   result = '{}{}'.format(result, date_map.get(int(i)))
 if type == 1:
  result = '{}十{}'.format(date_map.get(int(str_num[0])),date_map.get(int(str_num[1])))
 if type == 2:
  result = '十{}'.format(date_map.get(int(str_num[1])))
 if type == 3:
  result = '十'
 if type == 4:
  result = '二十'
 return result

year =chinese2digits(datetime.datetime.now().year,0)
print(year+'年'),
date_month=datetime.datetime.now().month
if date_month == 10:
 month = chinese2digits(date_month,3)
 print(month+'月'),
if date_month > 10:
 month = chinese2digits(date_month,2)
 print(month+'月'),
if date_month < 10:
 month = chinese2digits(date_month,0)
 print(month+'月'),
date_day = datetime.datetime.now().day
if date_day < 10:
 day = chinese2digits(date_day,0)
 print(day+'日'),
if 10 < date_day < 20:
 day = chinese2digits(date_day,2)
 print(day+'日'),
if date_day > 20:
 day = chinese2digits(date_day,1)
 print(day+'日'),
if date_day == 10:
 day = chinese2digits(date_day,3)
 print(day+'日'),
if date_day == 20:
 day = chinese2digits(date_day,4)
 print(day+'日'),
time_hour = datetime.datetime.now().hour
if time_hour < 10:
 hour = chinese2digits(time_hour,0)
 print(hour+'时'),
if time_hour == 10:
 hour = chinese2digits(time_hour,3)
 print(hour+'时'),
if time_hour > 10:
 hour = chinese2digits(time_hour,2)
 print(hour+'时'),
time_minu = datetime.datetime.now().minute
if time_minu < 10:
 minu = chinese2digits(time_minu,0)
 print(minu+'分'),
if time_minu == 10:
 minu = chinese2digits(time_minu,3)
 print(minu+'分'),
if time_minu > 10:
 minu = chinese2digits(time_minu,1)
 print(minu+'分'),
time_sec = datetime.datetime.now().second
if time_sec < 10:
 sec = chinese2digits(time_sec,0)
 print(sec+'秒'),
if time_sec == 10:
 sec = chinese2digits(time_sec,3)
 print(sec+'秒'),
if time_sec > 10:
 sec = chinese2digits(time_sec,1)
 print(sec+'秒'),
