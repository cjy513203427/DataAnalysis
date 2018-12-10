#coding=utf-8
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# +：　　加法运算
# -：　　减法运算
# *：　　乘法运算
# **：    幂运算
# /:  　　除法运算（如果有小数则返回结果为小数，如果都为整数则返回结果为整数）
# //：     整除，取整数部分
# %：　 取余

#e二次多项式拟合
def f_x2(x):
    return x ** 2 + 1

def f_fit_x2(x, y_fit):
    a, b, c = y_fit.tolist()
    return a * x ** 2 + b * x + c

x = np.linspace(-5, 5)
y = f_x2(x) + np.random.randn(len(x))  # 加入噪音
y_fit = np.polyfit(x, y, 2)  # 二次多项式拟合
y_show = np.poly1d(y_fit)  # 函数优美的形式
print(y_show)  # 打印
y1 = f_fit_x2(x, y_fit)
plt.figure(1)
plt.plot(x, f_x2(x), 'r', label='original')
plt.scatter(x, y, c='g', label='before_fitting')  # 散点图
plt.plot(x, y1, 'b--', label='fitting')
plt.title('polyfitting')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()  # 显示标签
plt.show()

#三次多项式拟合
def f_x3(x):
    return x ** 3 + 1

def f_fit_x3(x, y_fit):
    a, b, c, d = y_fit.tolist()
    return a * x ** 3 + b * x * 2 + c* x + d


x = np.linspace(-5, 5)
y = f_x3(x) + np.random.randn(len(x))  # 加入噪音
y_fit = np.polyfit(x, y, 3)  # 二次多项式拟合
y_show = np.poly1d(y_fit)  # 函数优美的形式
print(y_show)  # 打印
y1 = f_fit_x3(x, y_fit)
plt.figure(1)
plt.plot(x, f_x2(x), 'r', label='original')
plt.scatter(x, y, c='g', label='before_fitting')  # 散点图
plt.plot(x, y1, 'b--', label='fitting')
plt.title('polyfitting')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()  # 显示标签
plt.show()

#sin拟合
def f_sin(x):
    return 2*np.sin(x)+3
def f_sin_fit(x,a,b):
    return a*np.sin(x)+b
def f_sin_show(x,p_fit):
    a,b=p_fit.tolist()
    return a*np.sin(x)+b
x=np.linspace(-2*np.pi,2*np.pi)
y=f_sin(x)+0.5*np.random.randn(len(x))#加入了噪音
p_fit,pcov=curve_fit(f_sin_fit,x,y)#曲线拟合
print(p_fit)#最优参数
print(pcov)#最优参数的协方差估计矩阵
y1=f_sin_show(x,p_fit)
plt.figure(2)
plt.plot(x,f_sin(x),'r',label='original')
plt.scatter(x,y,c='g',label='before_fitting')#散点图
plt.plot(x,y1,'b--',label='fitting')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


