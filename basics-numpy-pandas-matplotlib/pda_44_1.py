import pandas as pda

# Series：数据列表 
#index 索引,默认索引是0，1，2，3---
a = pda.Series([1,2,8,3])
print(a)
b = pda.Series([1,2,8,3],index = ['a','b','c','d'])
print(b)

# DataFrame() 数据框，
# index：行名，columns：列名
c = pda.DataFrame([[3,4,5,6],[1,3,5,7],[9,8,7,6]])
print(c)
d = pda.DataFrame([[3,4,5,6],[1,3,5,7],[9,8,7,6]],index = ['apple','banana','cat'],columns = ['a','b','b','d'])
print(d)

# DataFrame()  通过字典创建数字框
# one:列的值
# 头部行数：head(行数)，默认五行
# 尾部行数：tail(行数)，默认五行
e = pda.DataFrame({
        "one":4,
        "two":[5,5,5],
        "three":list(str(789))
    })
print(e)
eh = e.head(2)
print(eh)
et = e.tail(2)
print(et)

# descrobe() 参数信息,count：单列数量,mean:平均数，std：标准差，min：最小值，max：最大值
# 25%，50%，75%，分位数。
f = pda.DataFrame({
        "one":[1,2,3,4],
        "two":[2,4,6,8],
        "three":[1,3,5,7]
    })
print(f)
print(f.describe())