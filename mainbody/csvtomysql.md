##### 将CSV文件中的数据读出后写入Mysql数据库

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

3、读取CSV文件中的数据

```python
df = pd.read_csv(r"D:\6 - 随书数据集\order.csv",encoding='unicode_escape',header=None)
```

4、将读取的数据写入MysqlS数据库

```python
try:
    for i in range(0,3500):
        h=int(i+1)
        a=int(df[0][i])
        b=int(df[1][i])
        c=str(df[2][i])
        d=float(df[3][i])
        e=float(df[4][i])
        f=str(df[5][i])
        g=str(df[6][i])
        print(h,a,b,c,d,e,f,g)
        sql0="INSERT INTO ordertest VALUES({},{},{},'{}',{},{},'{}','{}')".format(h,a,b,c,d,e,f,g)
        print(sql0)
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
#模块的导入
import pandas as pd
import pymysql
def mysqlConnect(sql):
    db=pymysql.connect(host="localhost",user="root",password="314625",database="school")
    cursor=db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()
df = pd.read_csv(r"D:\6 - 随书数据集\order.csv",encoding='unicode_escape',header=None)
try:
    for i in range(0,3500):
        h=int(i+1)
        a=int(df[0][i])
        b=int(df[1][i])
        c=str(df[2][i])
        d=float(df[3][i])
        e=float(df[4][i])
        f=str(df[5][i])
        g=str(df[6][i])
        print(h,a,b,c,d,e,f,g)
        sql0="INSERT INTO ordertest VALUES({},{},{},'{}',{},{},'{}','{}')".format(h,a,b,c,d,e,f,g)
        print(sql0)
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

