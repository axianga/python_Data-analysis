import pandas as pda

# 导入csv文件，首行：列名
a = pda.read_csv("*.csv")
a.describe()
a.sort_values(by="name") # 按某列的大小排序

# 导入excel
b = pda.read_excel("*.xls")

# 导入mysql数据库
import pymysql
conn = pymysql.connect(host = "",user = "",passwd = "",db = "")
sql = "select * from mytable"
c = pda.read_sql(sql,conn)

# 读取html网页表格数据: .html：读取本地网页数据  url:读取网络网页
d = pda.read_html("*.html")
e = pda.read_html("url")

# 导入文本的数据 .txt
f = pda.read_table("*.txt")








