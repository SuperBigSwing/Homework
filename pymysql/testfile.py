# -*- coding=utf-8 -*-
import pymysql
import re

conn=pymysql.connect(
  host='172.17.0.1',
  port=3306,
  user='Swing',
  passwd='12345qWe!@#',
  db='SRS',
  charset='utf8'
)

cur = conn.cursor()

with open("/home/gaoyiyun/stu/testfile.txt") as file:
 data_list = file.readlines()
 
 for t in data_list:
  
  text_list = re.split(r"\n",t)
  text = re.split(r"\t",text_list[0])

  sql = "insert into user_test values (%s,%s,%s)"
  print(sql)

  row_count = cur.execute(sql,[text[0],text[1],text[2]])
 

conn.commit()
cur.close()
conn.close()
