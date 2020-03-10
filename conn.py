# -*- coding=utf-8 -*-
import pymysql

conn=pymysql.connect(
  host='172.17.0.1',
  port=3306,
  user='Swing',
  passwd='12345qWe!@#',
  db='SRS',
  charset='utf8'
)

print("请选择进行的操作：1.查看；2.添加；3.删除")
num = input()

if num == 1:
 cur = conn.cursor()
 cur.execute("select * from stu")
 res = cur.fetchall()
 print(res)
 cur.close()
 conn.close()

if num == 2:
 cursor=conn.cursor()

 sql='insert into stu(id,name,homework) values(%s,%s,%s)'
 o=raw_input("请输入要添加的学号：")
 p=raw_input("请输入要添加的名称:")
 q=raw_input("请输入作业：")
 rows=cursor.execute(sql,
        (o,p,q))

 conn.commit()
 cursor.close()
 conn.close()

if num == 3:
 cursor=conn.cursor()

 sql='delete from stu where id = %s'
 a=raw_input("要删除的学号：")
 rows=cursor.execute(sql,(a))

 conn.commit()

 cursor.close()

 conn.close()

