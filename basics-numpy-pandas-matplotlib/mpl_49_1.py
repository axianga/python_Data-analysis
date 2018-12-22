# numpy:基础，数据处理
# pandas：数据探索，数据分析，导入数据
# matplotlib：作图可视化

import numpy as np
import pandas as pda
import matplotlib.pylab as pyl

data = pda.read_csv('1.csv')
# data.values[第几行][第几列]
# data.T 转置，行变列，列变行
print(data.values[0])     
data2 = data.T
y1 = data2.values[3]   #第三 列的所有元素
x1 = data2.values[2]   #第二列的所有元素
#pyl.plot(x1,y1)
#pyl.show()
x2 = data2.values[0]
pyl.plot(x2,x1)
pyl.show()