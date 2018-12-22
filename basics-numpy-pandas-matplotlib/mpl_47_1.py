# 折线图/散点图：plot
import matplotlib.pylab as pyl
import numpy as np

x = [1,2,3,4,5]
y = [5,7,8,0,4]
x2 = [1,3,5,7,9]
y2 = [3,5,6,8,1]
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

pyl.plot(x,y,'-.-.Dr')
pyl.plot(x2,y2,'-Hy')
pyl.title("show")
pyl.xlabel("NUMBER")
pyl.ylabel("done")
pyl.xlim(0,10)
pyl.ylim(0,10)
pyl.show()


# 直方图：hist









