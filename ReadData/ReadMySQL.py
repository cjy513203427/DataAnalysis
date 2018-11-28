#coding=utf-8
import pandas
import pymysql
#1.2读取mysql
mysql_cn= pymysql.connect(host='localhost', port=3306,user='root', passwd='123456', db='dota2_databank')
dataFrame = pandas.read_sql('select * from item_compound;', con=mysql_cn)
print(dataFrame)
mysql_cn.close()