# encoding=utf-8
import warnings

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

warnings.filterwarnings("ignore")
# 6 可视化
# 直接从github上读取数据
tips = sns.load_dataset('tips')
# 画出总账单和小费回归关系图
sns.lmplot("total_bill", "tip", tips,
           scatter_kws={"marker": "+", "color": "slategray"},
           line_kws={"linewidth": 1, "color": "indianred"}).savefig('../resource/image/picture2')

# 对拥有相同x水平的y值进行映射
plt.figure()
sns.lmplot('size', 'tip', tips, x_estimator=np.mean).savefig('../resource/image/picture3')
# 用x_jitter可以让数据点发生水平的扰动.但扰动的幅度不宜过大
sns.lmplot('size', 'tip', tips, x_jitter=.15).savefig('../resource/image/picture4')
# seaborn还可以做出xkcd风格的图片
with plt.xkcd():
    sns.color_palette('husl', 8)
    sns.set_context('paper')
    sns.lmplot(x='total_bill', y='tip', data=tips, ci=65).savefig('../resource/image/picture1')
# 以day进行分类
with plt.xkcd():
    sns.lmplot('total_bill', 'tip', data=tips, hue='day')
    plt.xlabel('hue = day')
    plt.savefig('../resource/image/picture5')
# 以smoker进行分类
with plt.xkcd():
    sns.lmplot('total_bill', 'tip', data=tips, hue='smoker')
    plt.xlabel('hue = smoker')
    plt.savefig('../resource/image/picture6')

sns.set_style('dark')
sns.set_context('talk')
sns.lmplot('size', 'total_bill', tips, order=2)
plt.title('# poly order = 2')
plt.savefig('../resource/image/picture7')
plt.figure()
sns.lmplot('size', 'total_bill', tips, order=3)
plt.title('# poly order = 3')
plt.savefig('../resource/image/picture8')
sns.jointplot("total_bill", "tip", tips).savefig('../resource/image/picture9')