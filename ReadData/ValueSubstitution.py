#encoding=utf-8
import pandas as pd
import numpy as np
#4.5 值替换
#首先创造一个Series（没有数据情况自己造）
Series = pd.Series([8,7,2,3,6,5])
print"原来的Series\n",(Series)

#数值替换，888
print "单元素替换\n",Series.replace(0,888)

#列和列的替换同理
print "列替换\n",Series.replace([8,7,2,3,6,5],[11111,222222,3333333,44444,55555,666666])