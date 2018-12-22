# 折线图/散点图：plot
import matplotlib.pylab as pyl
import numpy as np

# 直方图hist

'''    
data = np.random.normal(10.0,2.0,1000)
pyl.hist(data)
pyl.show()
'''
'''      # randint(1,10+1,1000) 不含11区间：1-10,1000个数
data2 = np.random.randint(1,10+1,1000)
print(data2)
pyl.hist(data2)
pyl.show()
'''
'''       
data3 = np.random.random_integers(1,10,1000)
pyl.hist(data3)
pyl.show()
'''     # histtype : {‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’}, optional(选择展示的类型,默认为bar)
data4 = np.random.randint(1,10+1,1000)
pyl.hist(data4,histtype = 'stepfilled')
pyl.xlabel("Quantily")
pyl.show()

'''
# 直方图属性设置 
# np.arange(x1,x2,w)：x区域，不含x2，宽度w
data4 = np.random.randint(1,10+1,1000)
sty = np.arange(0,11,1)
pyl.hist(data4,sty)
pyl.show()
'''

# 显示图 个数 subplot(x,y,n) x:行，y：列，n：第几个
'''   # 输出两行两列
pyl.subplot(2,2,1)
pyl.subplot(2,2,2) 
pyl.subplot(2,2,3)
pyl.subplot(2,2,4)
pyl.show()
'''
'''  # 输出第一行两列，第二行一列图形
pyl.subplot(2,2,1)
pyl.subplot(2,2,2)
pyl.subplot(2,1,2)
pyl.show()

'''
'''

'''



'''
x = [1,2,3,4,5]
y = [5,7,8,0,4]
x2 = [1,3,5,7,9]
y2 = [3,5,6,8,1]
'''
#pyl.plot(x,y)  # (x,y,形式) 形式默认蓝色折线图,
#pyl.show()

#pyl.plot(x,y,'o')  # o:形式为散点图
#pyl.show()

#pyl.plot(x,y,'y')    
#pyl.show()

#pyl.plot(x,y,'yo')
#pyl.show()

'''
在同张图上显示多个图形
pyl.plot(x1,y2,'')
pyl.plot(x2,y2,'')
o : 散点图
颜色  
    c--cyan--青色
    r--red--红色
    m--magente--品红
    g--green--绿色
    b--blue--蓝色
    y--yellow--黄色
    k--black--黑色
    w--while--白色

线条样式
    - 直线
    --虚线
    -.-.形式
    ：细小虚线

点的样式(坐标点)
    s -- 方形
    h -- 六角形
    H -- 六角形
    * -- 星形
    + -- 加号
    x -- x型
    d -- 菱形
    D -- 菱形
    p -- 五角形

title,xlabel,ylabel,标题，x轴，y轴,显示英文正常。显示中文错误
xlim(),ylim()： x、y轴范围  
''' 

#pyl.plot(x,y,':r')
#pyl.show()
'''
pyl.plot(x,y,'-.-.Dr')
pyl.plot(x2,y2,'-Hy')
pyl.title("show")
pyl.xlabel("NUMBER")
pyl.ylabel("done")
pyl.xlim(0,10)
pyl.ylim(0,10)
pyl.show()
'''

'''
# 随机数生成
data = np.random.random_integers(1,10,10) #(最小值，最大值，个数) 
print(data)
data = np.random.randint(1,10,10) #(最小值，最大值，个数) 
print(data)

data2 = np.random.normal(5.0,2.0,10) #(均数μ，方差开平方σ，个数)
print(data2)

normal = np.random.normal(1,0,10)   # 标准正态分布
print(normal)
'''









