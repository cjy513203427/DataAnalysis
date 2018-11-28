#encoding=utf-8
import pandas as pd
import numpy as np
#创建一个6*4的数据框，randn函数用于创建随机数
czf_data = pd.DataFrame(np.random.randn(6,4),columns=list('ABCD'))
#将第二行置空
czf_data.ix[2,:]=np.nan

print(czf_data)
#调用插值方法
print czf_data.interpolate()