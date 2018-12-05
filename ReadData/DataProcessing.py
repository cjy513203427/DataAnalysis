# encoding=utf-8
import json
import pandas as pd
import numpy as np
from pandas import DataFrame

# 接ReadCsv.py笔记
# 4.3缺失值处理
path = 'E:\\python_project\\DataAnalysis\\resource\\data\\usagov_bitly_data2012-03-16-1331923249.txt'  # 根据自己的路径填写
# 内置或第三方模块可以将JSON字符串转换成python字典对象
records = [json.loads(line) for line in open(path)]
frame = DataFrame(records)
frame['tz']
print(frame['tz'])
# 缺失值是NaN，不是空字符串
# 用数字或字符填充缺失值
print(frame['tz'].fillna('Starcraft2'))

# 用前一个数据代替缺失值
# print frame['tz'].fillna(method='pad')

# 用后一个数据代替缺失值
# print frame['tz'].fillna(method='bfill')

# 删除缺失行
# frame['tz'].dropna(axis='index')
# 删除缺失列
# print frame['tz'].dropna(axis='columns')
