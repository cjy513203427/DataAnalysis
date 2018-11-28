# encoding=utf-8
import pandas
# 一.数据导入和导出
# 网络读取
# data_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv" #填写url读取
# 本地读取直接写路径名
dataFrame = pandas.read_csv("E:\\python_project\\DataAnalysis\\resource\\data\\test.csv")

# 二.提取和筛选需要的数据
#（一）提取和查看相应数据
# 读取前五条
print"读取前五条\n", (dataFrame.head())
# 读取后五条
print"读取后五条\n", (dataFrame.tail())
print(dataFrame.columns)
print(dataFrame.index)

# 打印10~20行前三列数据
print "打印10~20行前三列数据\n", dataFrame.ix[10:20, 0:3]  #

print "打印第(1,2),(1,4),(3,2),(3,4),(5,2),(5,4)的数据\n", dataFrame.iloc[[1, 3, 5], [2, 4]]

# 专门提取某一个数据，这个例子提取的是第3行，第2列数据（默认从0开始算哈）
print "专门提取一个数据(3,2)\n", dataFrame.iat[3, 2]

# 打印维度
print "打印维度\n", dataFrame.shape

# 选取第3行
print"选取第3行\n", dataFrame.iloc[3]

# 选取第2到3行
print"选取第三到五行\n ", dataFrame.iloc[2:4]  # 选取第2到第3行

#选取第0行1列的元素
print"选取第0行1列的元素\n",dataFrame.iloc[0,1]

#(二)筛选出需要的数据
#example:假设我们要筛选出小费大于$8的数据
print"假设我们要筛选出小费大于$8的数据\n",dataFrame[dataFrame.tip>8]

#筛选出小费大于$7或总账单大于$50的数据
print "筛选出小费大于$7或总账单大于$50的数据\n",dataFrame[(dataFrame.tip>7)|(dataFrame.total_bill>50)]

#筛选出小费大于$7且总账单大于$50的数据
print "筛选出小费大于$7且总账单大于$50的数据\n",dataFrame[(dataFrame.tip>7)&(dataFrame.total_bill>50)]

#假如加入了筛选条件后，我们只关心day和time
print"假如加入了筛选条件后，我们只关心day和time\n",dataFrame[['day','time']][(dataFrame.tip>7)|(dataFrame.total_bill>50)]

# 三.统计描述
# 对于数值数据，结果的索引将包括计数，平均值，标准差，最小值，
# 最大值以及较低的百分位数和50。默认情况下，较低的百分位数为25，
# 较高的百分位数为75.50百分位数与中位数相同

# 中位数是第50百分位数。
# 第25百分位数又称第一个四分位数（First Quartile），用Q1表示；第50百分位数又称第二个四分位数（Second Quartile），
# 用Q2表示；第75百分位数又称第三个四分位数（Third Quartile）,用Q3表示。若求得第p百分位数为小数，可完整为整数。

print "描述性统计\n",dataFrame.describe()

# 四.数据处理
# (一)数据转置
print "矩阵转置\n",dataFrame.T

# (二)数据排序
# 按tip列升序排序
print "按tip列升序排序\n",dataFrame.sort_values(by='tip')

# (四)数据分组
#按day这一列进行分组
group = dataFrame.groupby('day')

#打印每一组的第一行数据
print "按day这一列进行分组,第一组\n",group.first()

#打印每一组的最后一行数据
print "按day这一列进行分组，最后一组\n",group.last()

#(五)计数统计
#统计性别
count = dataFrame['sex'].value_counts()
print"统计性别\n",(count)