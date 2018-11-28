# encoding=utf-8
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import chisquare
from scipy.stats import ttest_ind
from scipy.stats import ttest_rel
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# 5.统计分析
# 5.1 t检验
# 5.1.1.独立样本t检验
# 独立样本t检验统计量为：
# 如图5-1所示
# S12和 S22为两样本方差；n1 和n2 为两样本容量。
# 两独立样本t检验就是根据样本数据对两个样本来自的两独立总体的均值是否有显著差异进行推断；
# 进行两独立样本t检验的条件是，两样本的总体相互独立且符合正态分布。
IS_t_test = pd.read_excel('E:\\python_project\\DataAnalysis\\resource\\data\\statistics.xlsx', 'Sheet1')
Group1 = IS_t_test[IS_t_test['group'] == 1]['data']
Group2 = IS_t_test[IS_t_test['group'] == 2]['data']
# 默认方差齐性,即认为两组方差相等或者误差不大
# 返回参数中t-statistic绝对值大于等于1.96是可接受的
print "默认方差齐性\n", ttest_ind(Group1, Group2)
# 方差不齐
print("方差不齐")
#print ttest_ind(Group1, Group2, equal_var=True)
print ttest_ind(Group1, Group2, equal_var=False)

# 5.1.2.配对样本t检验
# 配对样本总体之间是存在相关关系，如药量和药效的关系
print "配对样本t检验\n", ttest_rel(Group1, Group2)

# 5.2方差分析
# 5.2.1.单因素方差分析
# levene方差齐性检验,如果p<0.05,则方差不齐
w, p = stats.levene(Group1, Group2)
print "levene方差齐性检验\n", w, p
# 进行方差分析
f, p = stats.f_oneway(Group1, Group2)
print "进行方差分析\n", f, p

# 5.2.2.多因素方差分析
# 研究区组和营养素对体重的影响
# 数据导入
MANOVA = pd.read_excel('E:\\python_project\\DataAnalysis\\resource\\data\\MANOVA.xlsx', 'Sheet1')
print(MANOVA)
# 多因素方差分析
# (1)RFormula格式
# ~分隔目标和对象
# +合并对象，“+ 0”意味着删除空格
# :交互（数值相乘，类别二值化）
# . 除了目标外的全部列
# 更多RFormula细节参考：https://blog.csdn.net/sinat_33761963/article/details/54910936
formula = 'weight~id+nutrient+(nutrient):(weight)'
anova_results = anova_lm(ols(formula, MANOVA).fit())
print "多因素方差分析\n", anova_results

# 5.3卡方检验
# 卡方检验就是统计样本的实际观测值与理论推断值之间的偏离程度，
# 实际观测值与理论推断值之间的偏离程度就决定卡方值的大小，卡方值越大，越不符合；
# 卡方值越小，偏差越小，越趋于符合，若两个值完全相等时，卡方值就为0，表明理论值完全符合
observed = np.array([15, 95])
# 观测值：110学生中化妆的女生95人，化妆的男生15人
expected = np.array([55, 55])
# 理论值：110学生中化妆的女生55人，化妆的男生55人
chisquare(observed, expected)
print"卡方检验\n", (chisquare(observed, expected))
