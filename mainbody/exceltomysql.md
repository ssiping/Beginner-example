##### 将excel表格中的数据读出后写入Mysql数据库

1、模块的导入

```python
import pandas as pd
import pymysql
```

2、数据库连接函数

```python
def mysqlConnect(sql):
    db=pymysql.connect(host="localhost",user="root",password="314625",database="school")
    cursor=db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()
```

3、读取表格中的数据

```python
df = pd.read_excel(r"D:\6 - 随书数据集\loan.xlsx",header = None)
```

4、将数据逐个读出后逐条写入Mysql数据库

```python
try:
    for i in range(0,150009):
        a=int(df[0][i])
        b=float(df[1][i])
        c=float(df[2][i])
        d=float(df[3][i])
        e=str(df[4][i])
        if e=="nan":
            e=0
        f=str(df[5][i])
        if f=="nan":
            f=0
        print(a,b,c,d,e,f)
        sql0="INSERT INTO loan VALUES({},'{}','{}','{}','{}','{}')".format(a,b,c,d,e,f)
        mysqlConnect(sql0)
        df.drop([i],axis=0,inplace=True)
```

5、发生错误则回滚

```python
except:
    # 如果发生错误则回滚
    print("你已经写入数据")
    db=pymysql.connect(host="localhost",user="root",password="314625",database="school")
    db.rollback()
    db.close()
    pass
```

6、完整代码

```python
import pandas as pd
import pymysql
def mysqlConnect(sql):
    db=pymysql.connect(host="localhost",user="root",password="314625",database="school")
    cursor=db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()
df = pd.read_excel(r"D:\6 - 随书数据集\loan.xlsx",header = None)
try:
    for i in range(0,150009):
        a=int(df[0][i])
        b=float(df[1][i])
        c=float(df[2][i])
        d=float(df[3][i])
        e=str(df[4][i])
        if e=="nan":
            e=0
        f=str(df[5][i])
        if f=="nan":
            f=0
        print(a,b,c,d,e,f)
        sql0="INSERT INTO loan VALUES({},'{}','{}','{}','{}','{}')".format(a,b,c,d,e,f)
        mysqlConnect(sql0)
        df.drop([i],axis=0,inplace=True)
except:
    # 如果发生错误则回滚
    print("你已经写入数据")
    db=pymysql.connect(host="localhost",user="root",password="314625",database="school")
    db.rollback()
    db.close()
    pass
```

