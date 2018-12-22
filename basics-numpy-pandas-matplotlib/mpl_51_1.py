# 数据清洗，整理数据图形展示
import pymysql
import numpy as np
import pandas as pda
import matplotlib.pylab as pyl

conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "root", db = "mt" )
sql = "select * from hotel"
data = pda.read_sql(sql, conn)
print(data.columns)           # data 的列名列表
print(data.columns[3])        # 第3+1 行的列名
print(data.describe())        # data的属性
print(len(data))              # data的长度，行数
print(data['avgScore'])       # 输出data["avgScore"]的列所有元素
print(data.values[0])         # 输出第一行的值
# 数据清洗，将控制赋值给中位数
for i in range(len(data)):
    if data["avgScore"][i] == None:
        data["avgScore"][i] = 4.65
print(data["avgScore"])

'''   # 此段逻辑较差
# 数据清洗，将data["avgPrice"] 为0的数值赋值为空，再赋值为中位数
data["avgScore"][(data["avgScore"] == 0)] = None
count_change = 0
for i in data.columns:
    for j in data.columns:
        if (data["i"].isnull())[j] :
            data[i][j] = "4.65"
            count+=1
print(count_change)

'''
# 展示数据，折线图与散点图对比
'''
pyl.subplot(2,1,1)
data2 = data.T
avgScore = data2.values[3]
comment = data2.values[6]
pyl.plot(avgScore,comment,'-.-.*r')
#pyl.show()
pyl.subplot(2,1,2)
pyl.plot(avgScore,comment,'or')
pyl.show()
'''
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
x = da2[3]
y = da2[6]
pyl.subplot(2,1,1)
data2 = data.T
avgScore = data2.values[3]
comment = data2.values[6]
pyl.plot(x,y,'-.-.*r')
#pyl.show()
pyl.subplot(2,1,2)
pyl.plot(x,y,'or')
pyl.show()




