# numpy 的基本操作
# 排序:sort() 最大值：max() 最小值：min() 分维度：reshape（） 数组下标切断:ar1[:]
import numpy as np

# 排序 sort(),不能赋值，直接调用，改变自身
ar1 = np.array(['c','1','5','3'])
print(ar1, end = '\n----\n')
ar1.sort()        
print(ar1,end = '\n----\n')
print(np.sort(ar1),end = '\n----\n')

# 最大值和最小值 max()\min()
ar1 = np.array(range(12))
print(ar1)
ar2 = ar1.reshape((3,4))
print(ar2)
ar1_max = ar1.max()
ar2_max = ar2.max()
print(ar1_max,ar2_max,end = "\n----\n")

ar1_max2 = np.max(ar1)
ar2_max2 = np.max(ar2)
print(ar1_max2,ar1_max2,end = '\n----\n')

# 切片，数组
ar1 = np.array(range(1,13))
print(ar1,'\n',ar1[0:11],'\n',ar1[:5],'\n',ar1[5:])