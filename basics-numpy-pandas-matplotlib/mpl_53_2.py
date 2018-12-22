# # 数据清洗，整理数据图形展示
# np.arange(avgScore_min,avgScore_max,avgScore_dst) hist 的长度，前两个是区间，左开右闭，第三个的宽度。
import pymysql
import numpy as np
import pandas as pda
import matplotlib.pylab as pyl

conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "root", db = "mt" )
sql = "select * from hotel"
data = pda.read_sql(sql, conn)
print(data.columns)           # data 的列名列表
print(data.describe())        # data的属性
print(len(data))              # data的长度，行数

# .T  转置的方法，步骤多，可以直接用data["列名"]
line = len(data.values)      # 行数
print('***',line)
col = len(data.values[0])    # 列数
print('***',col)
da = data.values             # data的行属性
for i in range(line):
    for j in range(col):
        if(da[i][3] > 5.0):
            print(da[i][3])
            da[i][3] = 4.65
da2 = da.T
x = da2[3]      # avgScore
y = da2[6]      # comment
pyl.subplot(2,1,1)
data2 = data.T
avgScore = data2.values[3]
comment = data2.values[6]
pyl.plot(x,y,'-.-.*r')
#pyl.show()
pyl.subplot(2,1,2)
pyl.plot(x,y,'or')
pyl.show()
print('***__***')
# 分布分析
# 极差 = 最大值-最小值
# 极距 = 极差/组数
avgScore_max = da2[3].max()
avgScore_min = da2[3].min()
comment_max = da2[6].max()
comment_min = da2[6].min()

avgScore_rg = avgScore_max - avgScore_min
comment_rg = comment_max - comment_min

avgScore_dst = avgScore_rg/10
comment_dst = comment_rg/10

avgScore_sty = np.arange(avgScore_min,avgScore_max,avgScore_dst)
comment_sty = np.arange(comment_min,comment_max,comment_dst)

pyl.subplot(2,1,1)
pyl.hist(da2[3],avgScore_sty)
#pyl.show()
pyl.subplot(2,1,2)
pyl.hist(da2[6],comment_sty)
pyl.show()
print("finished")


