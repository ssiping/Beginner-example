在python中连接Mysql数据库

1、引用模块

```python
import pymysql
```

2、定义Mysql连接函数，连接school数据库，用户名root,密码314625

```python
def mysqlConnect(sql):
    db=pymysql.connect(host="localhost",user="root",password="314625",database="school")
    cursor=db.cursor()
    cursor.execute(sql)
    db.commit()
    data=cursor.fetchall()
    db.close()
    return data
```

3、查询数据表stu并显示

```python
sql='select * from stu'
res=mysqlConnect(sql)
for i in res:
    print(i)
print()
```

4、删除数据表stu中id为103的记录并显示

```python
sql0='delete from stu where id=103'
mysqlConnect(sql0)
sql='select * from stu'
res=mysqlConnect(sql)
for i in res:
    print(i)
print()
```

5、向数据表stu中插入id为103的记录并显示

```python
sql0="INSERT INTO stu VALUES(103,'SMITH','M',01,22,'2013-03-15')"
try:
    mysqlConnect(sql0)
    #(102,'HOWARD','M',01,24,'2015-07-31'),
    #(103,'SMITH','M',01,22,'2013-03-15'),'
    sql='select * from stu'
    res=mysqlConnect(sql)
    for i in res:
        print(i)
except:
    # 如果发生错误则回滚
    db=pymysql.connect(host="localhost",user="root",password="314625",database="school")
    db.rollback()
    db.close()
print()
```

6、将数据表stu中id为103的记录，其年龄更新为40

```python
sql0="update stu set age=40 where id=103"
try:
    mysqlConnect(sql0)
    #(102,'HOWARD','M',01,24,'2015-07-31'),
    #(103,'SMITH','M',01,22,'2013-03-15'),'
    sql='select * from stu'
    res=mysqlConnect(sql)
    for i in res:
        print(i)
except:
    # 如果发生错误则回滚
    db=pymysql.connect(host="localhost",user="root",password="314625",database="school")
    db.rollback()
    db.close()
```

7、完整代码

```python
import pymysql
def mysqlConnect(sql):
    db=pymysql.connect(host="localhost",user="root",password="314625",database="school")
    cursor=db.cursor()
    cursor.execute(sql)
    db.commit()
    data=cursor.fetchall()
    db.close()
    return data
sql='select * from stu'
res=mysqlConnect(sql)
for i in res:
    print(i)
print()
sql0='delete from stu where id=103'
mysqlConnect(sql0)
sql='select * from stu'
res=mysqlConnect(sql)
for i in res:
    print(i)
print()
sql0="INSERT INTO stu VALUES(103,'SMITH','M',01,22,'2013-03-15')"
try:
    mysqlConnect(sql0)
    #(102,'HOWARD','M',01,24,'2015-07-31'),
    #(103,'SMITH','M',01,22,'2013-03-15'),'
    sql='select * from stu'
    res=mysqlConnect(sql)
    for i in res:
        print(i)
except:
    # 如果发生错误则回滚
    db=pymysql.connect(host="localhost",user="root",password="314625",database="school")
    db.rollback()
    db.close()
print()
sql0="update stu set age=40 where id=103"
try:
    mysqlConnect(sql0)
    #(102,'HOWARD','M',01,24,'2015-07-31'),
    #(103,'SMITH','M',01,22,'2013-03-15'),'
    sql='select * from stu'
    res=mysqlConnect(sql)
    for i in res:
        print(i)
except:
    # 如果发生错误则回滚
    db=pymysql.connect(host="localhost",user="root",password="314625",database="school")
    db.rollback()
    db.close()
```

