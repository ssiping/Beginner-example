Mysql操作

1、操作MySQL数据库

```mysql
-- 查看数据库
SHOW DATABASES;
-- 创建数据库test_db
CREATE DATABASE test_db;
-- 查看名称中包含“test_db”的数据库
SHOW DATABASES LIKE 'test_db';
-- 创建字符集为GB2312的数据库test_db_char
CREATE DATABASE test_db_char
DEFAULT CHARACTER SET gb2312
DEFAULT COLLATE gb2312_chinese_ci;
-- 查看数据库的声明定义
SHOW CREATE DATABASE test_db_char;
-- 修改数据库的字符集和校对规则
ALTER DATABASE test_db
DEFAULT CHARACTER SET gb2312
DEFAULT COLLATE gb2312_chinese_ci;
-- 删除数据库
DROP DATABASE test_db_del;
-- 使用数据库
USE test_db;
```

2、操作表

```mysql
-- 在test_db数据库中创建tb_emp1数据表
USE test_db;
CREATE TABLE tb_emp6
(
id INT(11),
name VARCHAR(25),
deptId INT(11),
salary FLOAT
);
-- 查看数据库中的表
SHOW TABLES;
-- 查看数据表的表结构
DESCRIBE tb_emp1;
-- 在表的第一列添加字段
ALTER TABLE tb_emp1
ADD COLUMN col1 INT FIRST;
-- 在name列后添加字段
ALTER TABLE tb_emp1
ADD COLUMN col2 INT AFTER name;
-- 修改字段数据类型
ALTER TABLE tb_emp1
MODIFY name VARCHAR(30);
-- 删除字段
ALTER TABLE tb_emp1
DROP col2;
-- 修改字段名称
ALTER TABLE tb_emp1
CHANGE col1 col3 CHAR(30);
-- 修改表名
ALTER TABLE tb_emp1
RENAME TO tb_emp2;
-- 删除表
DROP TABLE tb_emp3;
```

3、约束

```mysql
-- 在创建表时设置主键约束
CREATE TABLE tb_emp4
(
id INT(11),
name VARCHAR(22),
location VARCHAR(50), 
PRIMARY KEY(id)
);
-- 在创建表时设置复合主键
CREATE TABLE tb_emp5
(
name VARCHAR(25),
deptId INT(11),
salary FLOAT,
PRIMARY KEY(name,deptId)
);
-- 在修改数据表时添加主键约束
ALTER TABLE tb_emp2
ADD PRIMARY KEY(id);
-- 在创建表时创建外键约束
CREATE TABLE tb_emp6
(
id INT(11) PRIMARY KEY,
name VARCHAR(25),
deptId INT(11),
salary FLOAT,
CONSTRAINT fk_emp_dept1
FOREIGN KEY(deptId) 
REFERENCES tb_dept1(id)
);
-- 在修改表时添加外键约束
ALTER TABLE tb_emp2
ADD CONSTRAINT fk_tb_dept1
FOREIGN KEY(deptId)
REFERENCES tb_dept1(id);
-- 删除外键约束
ALTER TABLE tb_emp2
DROP FOREIGN fk_tb_dept1;
-- 在创建表时设置唯一索引
CREATE TABLE tb_emp2
(
id INT PRIMARY KEY,
name VARCHAR(40) UNIQUE,
location VARCHAR(50)
);
-- 在修改表时添加唯一索引
ALTER TABLE tb_dept1
ADD CONSTRAINT unique_name UNIQUE(name);
-- 删除唯一索引
ALTER TABLE tb_dept1
DROP INDEX unique_name;
--在创建表时设置检查约束
CREATE TABLE tb_emp7
(
id INT(11) PRIMARY KEY,
name VARCHAR(25),
deptId INT(11),
salary FLOAT,
CHECK(salary>0 AND salary<10000)
);
-- 在修改表时添加检查约束
ALTER TABLE tb_emp7
ADD CONSTRAINT check_id
CHECK(id>0);
-- 在创建表时设置默认值约束
CREATE TABLE tb_dept3
(
id INT(11) PRIMARY KEY,
name VARCHAR(22),
location VARCHAR(50) DEFAULT 'Beijing'
);
-- 在修改表时添加默认值约束
ALTER TABLE tb_dept3
CHANGE COLUMN location
location VARCHAR(50) DEFAULT 'Shanghai';
CHECK(id>0);
-- 删除默认值约束
ALTER TABLE tb_dept3
CHANGE COLUMN location
location VARCHAR(50) DEFAULT NULL;
-- 在创建表时设置非空约束
CREATE TABLE tb_dept4
(
id INT PRIMARY KEY,
name VARCHAR(20) NOT NULL,
location VARCHAR(50)
);
-- 在修改表时添加非空约束
ALTER TABLE tb_dept4
CHANGE COLUMN location
location VARCHAR(50) NOT NULL;
-- 删除非空约束
ALTER TABLE tb_dept4
CHANGE COLUMN location
location VARCHAR(50) NULL;
```

4、函数

```mysql
-- 绝对值函数
SELECT ABS(5),ABS(-2.4),ABS(-24),ABS(0);
-- 求余函数
SELECT MOD(63,8),MOD(120,10),MOD(15.5,3);
-- 平方根函数
SELECT SQRT(25),SQRT(120),SQRT(-9);
-- 符号函数
SELECT SIGN(-6),SIGN(0),SIGN(34);
-- 向上取整函数
SELECT CEIL(-2.5),CEILING(2.5);
-- 正弦函数
SELECT SIN(1),SIN(0.5*PI());
-- 反正弦函数
SELECT ASIN(0.8414709848078965),ASIN(2);
-- 余弦函数
SELECT COS(1),COS(0),COS(PI());
-- 反余弦函数
SELECT ACOS(2),ACOS(1),ACOS(-1);
-- 正切函数
SELECT TAN(1),TAN(0);
-- 反正切函数
SELECT ATAN(1.5574077246549023),ATAN(0);
-- 余切函数
SELECT COT(1);
-- 字符串长度函数
SELECT LENGTH('name'),LENGTH('数据库');
-- 字母大写转换函数
SELECT UPPER('green'),UPPER('Green');
-- 字母小写转换函数
SELECT LOWER('BLUE'),LOWER('Blue');
-- 左起取字符串函数
SELECT LEFT('MySQL',2);
-- 右起取字符串函数
SELECT RIGHT('MySQL',3);
-- 连接字符串函数
SELECT CONCAT('MySQL','5.7'),CONCAT('MySQL',NULL);
-- 删除空格函数
SELECT '[   mobile   ]',CONCAT('[',TRIM('   mobile   '),']');
-- 替换字符串函数
SELECT INSERT('Football',2,4,'Play') AS col1,
INSERT('Football',-1,4,'Play') AS col2,
INSERT('Football',3,20,'Play') AS col3;
-- 获取子串函数
SELECT SUBSTRING('computer',3) AS col1,
SUBSTRING('computer',3,4) AS col2,
SUBSTRING('computer',-3) AS col3,
SUBSTRING('computer',-5,3) AS col4;
-- 字符串逆序函数
SELECT REVERSE('hello');
-- 替换函数
SELECT REPLACE('aaa.mysql.com','a','w');
-- 当前日期和时间函数
SELECT NOW(),SYSDATE();
-- 当前日期函数
SELECT CURDATE(),CURRENT_DATE(),CURRENT_DATE()+0;
-- 当前时间函数
SELECT CURTIME(),CURRENT_TIME(),CURRENT_TIME()+0;
-- 周索引函数
SELECT DAYOFWEEK('2017-12-15');
-- 工作日索引函数
SELECT WEEKDAY('2017-12-15');
-- 月索引函数
SELECT DAYOFMONTH('2017-12-15');
-- 年索引函数
SELECT DAYOFYEAR('2017-12-15');
-- 月份名称函数
SELECT MONTHNAME('2017-12-15');
-- 间隔天数函数
SELECT DATEDIFF('2017-11-30','2017-11-29') AS COL1,
DATEDIFF('2017-11-30','2017-12-15') AS col2;
-- 日期加操作函数
SELECT ADDDATE('2017-11-30 23:59:59', INTERVAL 1 SECOND) AS col1,
ADDDATE('2017-11-30 23:59:59' ,INTERVAL '1:1' MINUTE_SECOND) AS col2;
-- 日期时间格式化输出函数
SELECT DATE_FORMAT('2017-11-15 21:45:00','%W %M %D %Y') AS col1,
DATE_FORMAT('2017-11-15 21:45:00','%h:i% %p %M %D %Y') AS col2;
-- 最大值函数
SELECT MAX(student_score)
AS max_score
FROM tb_students_score;
-- 最小值函数
SELECT MIN(student_score)
AS min_score
FROM tb_students_score;
-- 计数函数
SELECT COUNT(student_name)
AS students_number
FROM tb_students_score;
-- 求和函数
SELECT SUM(student_score)
AS score_sum
FROM tb_students_score;
平均值函数
SELECT AVG(student_score)
AS score_avg
FROM tb_students_score;
```

5、使用基本的查询语句

```mysql
-- 使用星号查询表中的全部内容
SELECT * FROM tb_students_info;
-- 使用字段名查询表中全部字段
SELECT id,name,dept_id,age,sex,height,login_date
FROM tb_students_info;
-- 查询表中指定的字段
SELECT name FROM tb_students_info;
-- 去除结果中的重复行
SELECT  DISTINCT age
FROM tb_students_info;
SELECT   age
FROM tb_students_info;
-- 给表设置别名
SELECT stu.name,stu.height
FROM tb_students_info AS stu;
-- 给列设置别名
SELECT name AS student_name,
age AS student_age
FROM tb_students_info;
-- 指定查询结果的行数
SELECT * FROM tb_students_info LIMIT 4;
-- 根据位置偏移量指定查询行数
SELECT * FROM tb_students_info LIMIT 3,5;
-- 对查询结果进行排序
SELECT * FROM tb_students_info ORDER BY height;
-- 对查询结果的多列进行排序
SELECT name,height
FROM tb_students_info
ORDER BY height,name;
-- 单一条件的查询语句
SELECT name,height
FROM tb_students_info
WHERE height=170;
-- 多条件的查询语句
SELECT * FROM tb_students_info
WHERE age>21 AND height>=175;
SELECT * FROM tb_students_info
WHERE age<22;
-- 使用百分号通配符进行模糊查询
SELECT name FROM tb_students_info
WHERE name LIKE 'T%';
-- 使用下划线通配符进行模糊查询
SELECT name FROM tb_students_info
WHERE name LIKE '____y';
-- 使用比较运算符设置日期条件
SELECT * FROM tb_students_info
WHERE login_date<'2016-01-01';
-- 使用BETWEEN AND运算符设置日期条件
SELECT * FROM tb_students_info
WHERE login_date
BETWEEN '2015-10-01'
AND '2016-05-01';
```

6、查询进阶

```mysql
-- 内连接查询
SELECT id,name,age,dept_name
FROM tb_students_info INNER JOIN tb_departments
WHERE tb_students_info.dept_id=tb_departments.dept_id;
-- 左外连接查询
SELECT name,dept_name
FROM tb_students_info s
LEFT OUTER JOIN tb_departments d
ON s.dept_id = d.dept_id;
-- 右外连接查询
SELECT name,dept_name
FROM tb_students_info s
RIGHT OUTER JOIN tb_departments d
ON s.dept_id = d.dept_id;
-- 自连接查询
SELECT s1.id, s1.name
FROM tb_students_info s1,tb_students_info s2
WHERE s1.dept_id=s2.dept_id
AND s2.id = 1;
-- IN子查询
SELECT name FROM tb_students_info
WHERE dept_id IN
(SELECT dept_id
FROM tb_departments
WHERE dept_type= 'A' );
-- 内层子查询
SELECT dept_id
FROM tb_departments
WHERE dept_type='A';
-- 外层子查询
SELECT name FROM tb_students_info
WHERE dept_id IN(1,2);
-- NOT IN子查询
SELECT name FROM tb_students_info
WHERE dept_id NOT IN
(SELECT dept_id
FROM tb_departments
WHERE dept_type='A');
-- 带等号运算符的子查询
SELECT name FROM tb_students_info
WHERE dept_id = 
(SELECT dept_id
FROM tb_departments
WHERE dept_name='Computer');
-- 带不等号运算符的子查询
SELECT name FROM tb_students_info
WHERE dept_id <>
(SELECT dept_id
FROM tb_departments
WHERE dept_name='Computer');
-- EXISTS子查询
SELECT * FROM tb_students_info
WHERE EXISTS
(SELECT dept_name
FROM tb_departments
WHERE dept_id=1);
-- 分组查询与计数函数的应用
SELECT dept_id,COUNT(*) AS total
FROM tb_students_info
GROUP BY dept_id;
-- 分组查询
SELECT dept_id,GROUP_CONCAT(name) AS names
FROM tb_students_info
GROUP BY dept_id;
-- 使用HAVING关键字设置条件
SELECT dept_id,GROUP_CONCAT(name) AS names
FROM tb_students_info
GROUP BY dept_id
HAVING COUNT(name)>1;
-- 查询以特定字符开头的记录
SELECT * FROM tb_departments
WHERE dept_name REGEXP '^C';
-- 查询以特定字符串开头的记录
SELECT * FROM tb_departments
WHERE dept_name REGEXP '^Ch';
-- 查询以特定字符结尾的记录
SELECT * FROM tb_departments
WHERE dept_name REGEXP 'y$';
-- 查询以特定字符串结尾的记录
SELECT * FROM tb_departments
WHERE dept_name REGEXP 'my$';
-- 用符号“.”匹配任意一个字符
SELECT * FROM tb_departments
WHERE dept_name REGEXP 'o.y';
-- 用符号“*”匹配多个字符
SELECT * FROM tb_departments
WHERE dept_name REGEXP '^Ch*';
-- 用符号“+”匹配多个字符
SELECT * FROM tb_departments
WHERE dept_name REGEXP '^Ch+';
-- 匹配指定单个字符串
SELECT * FROM tb_departments
WHERE dept_name REGEXP 'in';
-- 匹配指定多个字符串
SELECT * FROM tb_departments
WHERE dept_name REGEXP 'in|on';
-- 匹配任意一个字母
SELECT * FROM tb_departments
WHERE dept_name REGEXP '[io]';
-- 匹配任意一个数字
SELECT * FROM tb_departments
WHERE dept_call REGEXP '[123]';
-- 匹配指定字符以外的字符
SELECT * FROM tb_departments
WHERE dept_name REGEXP '[^a-t]';
```

7、操作表中的数据

```mysql
-- 创建数据表tb_courses
CREATE TABLE tb_courses
(
course_id INT NOT NULL AUTO_INCREMENT,
course_name CHAR(40) NOT NULL,
course_grade FLOAT NOT NULL,
course_info CHAR(100) NULL,
PRIMARY KEY(course_id)
);
-- 指定所有字段插入一条数据
INSERT INTO tb_courses
(course_id,course_name,course_grade,course_info)
VALUES(1,'Network',3,'Computer Network');
INSERT INTO tb_courses
VAUES(3,'Java',4,'Java EE');
-- 不按照定义列的顺序插入一条数据
INSERT INTO tb_courses
(course_name,course_info,course_id,course_grade)
VALUES('Database','MySQL',2,3);
-- 没有列名称列表插入一条数据
INSERT INTO tb_courses
VALUES(3,'Java',4,'Java EE');
-- 向表中指定字段添加值
INSERT INTO tb_courses
(course_name,course_grade,course_info)
VALUES('System',3,'Operation System');
-- 复制表数据
CREATE TABLE tb_courses_new
(
course_id INT NOT NULL AUTO_INCREMENT,
course_name CHAR(40) NOT NULL,
course_grade FLOAT NOT NULL,
course_info CHAR(100) NULL,
PRIMARY KEY(course_id)
);
INSERT INTO tb_courses_new
(course_id,course_name,course_grade,course_info)
SELECT course_id,course_name,course_grade,course_info
FROM tb_courses;
-- 修改表中的数据
UPDATE tb_courses_new
SET course_grade=4;
UPDATE tb_courses_new
SET course_grade=4;
-- 根据条件修改表中的数据
UPDATE tb_courses_new
SET course_name='DB',course_grade=3.5
WHERE course_id=2;
-- 删除表中的全部数据
DELETE FROM tb_courses_new;
-- 根据条件删除表中的数据
DELETE FROM tb_courses
WHERE course_id=4;
DELETE FROM tb_courses_new
WHERE course_id=4;
DELETE FROM tb_emp6
WHERE id=2;
```

8、视图

```mysql
-- 创建基于单表的视图
CREATE VIEW view_students_info
AS SELECT * FROM tb_students_info;
-- 根据字段名创建基于单表的视图
CREATE VIEW v_students_info
(s_id,s_name,d_id,s_age,s_sex,s_height,s_date)
AS SELECT id,name,dept_id,age,sex,height,login_date
FROM tb_students_info;
-- 创建基于多表的视图
CREATE VIEW view_stu_dept(d_id,s_name,dept_name)
AS SELECT s.id,s.name,d.dept_name
FROM tb_students_info s,tb_departments d
WHERE s.dept_id=d.dept_id;
-- 查看视图的定义
DESCRIBE v_students_info;
DESC v_students_info;
-- 修改视图的定义
ALTER VIEW view_students_info
AS SELECT id,name,age
FROM tb_students_info;
-- 修改视图的内容
UPDATE view_students_info
SET age=205 WHERE id=1;
-- 删除视图
DROP VIEW IF EXISTS v_students_info;
```

9、自定义函数和存储过程

```mysql
-- 创建自定义函数
set global log_bin_trust_function_creators=TRUE
CREATE FUNCTION StuNameById()
RETURNS VARCHAR(45)
RETURN
(SELECT name FROM tb_students_info
WHERE id=1);
-- 使用自定义函数
SELECT StuNameById();
-- 删除自定义函数
DROP FUNCTION StuNameById;
-- 创建不带参数的存储过程
DELIMITER //
CREATE PROCEDURE ShowStuScore()
BEGIN
SELECT * FROM tb_students_score;
END //
DELIMITER //
CREATE PROCEDURE ShowStuScore()
BEGIN
SELECT * FROM tb_students_info;
END //
-- 调用不带参数的存储过程
DELIMITER;
CALL ShowStuScore();
call ShowStuScore();
-- 创建带参数的存储过程
DELIMITER //
CREATE PROCEDURE GetScoreByStu
(IN name VARCHAR(30))
BEGIN
SELECT student_score FROM tb_students_score
WHERE student_name=name;
END //
DELIMITER //
CREATE PROCEDURE GetScoreByStu
(IN name VARCHAR(30))
BEGIN
SELECT age FROM tb_students_info
WHERE tb_students_info.name=name;
END //
-- 调用带参数的存储过程
CALL GetScoreByStu('Green');
-- 删除存储过程
DELIMITER ;
DROP PROCEDURE GetScor0eByStu;
```

10、触发器

```mysql
-- 创建BEFORE类型触发器
CREATE TRIGGER SumOfSalary
BEFORE INSERT ON tb_emp8
FOR EACH ROW
SET @sum=@sum+NEW.salary;
-- 触发BEFORE类型触发器
SET @sum=0;
INSERT INTO tb_emp8
VALUES(3,'A',1,1000),(4,'B',1,500),(5,'A',1,1000),(6,'B',1,500);
-- 创建AFTER类型触发器
CREATE TRIGGER double_salary
AFTER INSERT ON tb_emp6
FOR EACH ROW
INSERT INTO tb_emp7
VALUES (NEW.id,NEW.name,deptId,2*NEW.salary);
-- 触发AFTER类型触发器
INSERT INTO tb_emp6
VALUES (1,'A',1,1000),(2,'B',1,500);
INSERT INTO tb_emp6
VALUES (5,'A',1,2000),(6,'B',1,3000);
-- 删除触发器
DROP TRIGGER double_salary;
```

11、索引

```mysql
-- 创建一般索引
CREATE TABLE tb_stu_info
(
id INT NOT NULL,
name CHAR(45) DEFAULT NULL,
dept_id INT DEFAULT NULL,
age INT DEFAULT NULL,
height INT DEFAULT NULL,
INDEX(height)
);
-- 创建唯一索引
CREATE TABLE tb_stu_info2
(
id INT NOT NULL,
name CHAR(45) DEFAULT NULL,
dept_id INT DEFAULT NULL,
age INT DEFAULT NULL,
height INT DEFAULT NULL,
UNIQUE INDEX(height)
);
-- 查看索引
SHOW INDEX FROM tb_stu_info2;
-- 删除索引
DROP INDEX height
ON tb_stu_info;
```

12、用户与权限

```mysql
-- 创建用户
CREATE USER 'jack'@'localhost'
IDENTIFIED BY 'tiger';
DROP USER 'jack'@'localhost';
-- 登录数据库
mysql -h localhost -u james -p
mysql -h localhost -u root -p
mysql -h localhost -u sunshiping -p
mysql -h localhost -u testuser -p
-- 修改用户账号
RENAME USER james@'localhost'
TO jack@'localhost';
mysql -h localhost -u jack -p
-- 删除用户
DROP USER 'testuser'@'localhost';
-- 授予用户权限
CREATE USER 'testuser'@'localhost' IDENTIFIED BY '123456';
grant all privileges on test_db.* to 'testuser'@'localhost';
flush privileges;
-- 授权后查询用户权限
SELECT Host,User,Select_priv,Insert_priv,Grant_priv
FROM mysql.user
WHERE User='testuser';
-- 撤销用户权限
REVOKE INSERT ON *.*
FROM 'testuser'@'localhost';
```

13、事务与数据库的备份恢复

```mysql
-- 数据库备份
SELECT * FROM school.tb_students_info
INTO OUTFILE 'D:/down/file.txt'
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '?';
-- 复制表数据
CREATE TABLE tb_students_copy
LIKE tb_students_info;
-- 数据库恢复
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/file.txt'
D:/down/file.txt
INTO TABLE test_db.tb_students_copy
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '?';
```

14、实例代码

```mysql
-- 创建数据表stu
CREATE TABLE stu
(
id INT NOT NULL PRIMARY KEY,
name VARCHAR(25) NOT NULL,
sex VARCHAR(2) NOT NULL,
class_id INT,
age INT,
login_date DATE
);
-- 创建数据表class
CREATE TABLE class
(
id INT NOT NULL PRIMARY KEY,
name VARCHAR(25) NOT NULL,
grade VARCHAR(10) NOT NULL,
t_name VARCHAR(25) NOT NULL
);
CREATE TABLE tb_emp8
(
id INT NOT NULL PRIMARY KEY,
name VARCHAR(22) NOT NULL,
deptId INT NOT NULL,
salary int NOT NULL
);
-- 向数据表stu中插入记录
INSERT INTO stu VALUES
(101,'JAMES','M',01,20,'2014-07-31'),
(102,'HOWARD','M',01,24,'2015-07-31'),
(103,'SMITH','M',01,22,'2013-03-15'),
(201,'ALLEN','F',02,21,'2017-05-01'),
(202,'JONES','F',02,23,'2015-07-31'),
(301,'KING','F',03,22,'2013-01-01'),
(302,'ADAMS','M',03,20,'2014-06-01');
-- 向数据表class中插入记录
INSERT INTO class VALUES
(01,'MATH','One','JONH'),
(02,'HISTORY','Two','SIMON'),
(03,'PHYSICS','Three','JACKSON');
-- 查询每个班级年龄最大的学生
SELECT a.class_id,b.name,max(a.age)
FROM stu a,class b
WHERE a.class_id=b.id
GROUP BY a.class_id;
-- 查询学生JAMES所在班级名称和班主任姓名
SELECT a.name,b.name,b.t_name
FROM stu a,class b
WHERE a.class_id=b.id
AND a.name='JAMES';
-- 使用连接查询，查询所有学生的班级信息
SELECT a.id,a.name,b.name
FROM stu a,class b
WHERE a.class_id=b.id;
-- 在stu表中，计算每个班级各有多少名学生
SELECT b.name,COUNT(*)
FROM stu a,class b
WHERE a.class_id=b.id
GROUP BY b.name;
-- 在stu表中，计算不同班级学生的平均年龄
SELECT b.name,AVG(age)
FROM stu a,class b
WHERE a.class_id=b.id
GROUP BY b.name; 
-- 指定所有字段名称插入记录
INSERT INTO stu
(id,name,sex,class_id,age,login_date)
 VALUES(101,'JAMES','M',01,20,'2014-07-31');
-- 不指定字段名称插入记录
INSERT INTO stu VALUES
(104,'HOWARD','M',01,24,'2015-07-31');
-- 同时插入多条记录
INSERT INTO stu VALUES
(105,'SMITH','M',01,22,'2013-03-15'),
(203,'ALLEN','F',02,21,'2017-05-01'),
(204,'JONES','F',02,23,'2015-07-31'),
(303,'KING','F',03,22,'2013-01-01'),
(304,'ADAMS','M',03,20,'2014-06-01');
-- 将学生JAMES的年龄增加1
UPDATE stu SET age=age+1
WHERE name='JAMES';
-- 将学生HOWARD的年龄增加1
UPDATE stu SET sex='F',login_date='2016-08-31'
WHERE name='HOWARD';
-- 删除班级号为01的记录
DELETE FROM stu
WHERE class_id=01;
-- 创建年龄超过22岁的学生的视图
CREATE VIEW stu_older(id,name,sex,age,login_date)
AS SELECT id,name,sex,age,login_date
FROM stu
WHERE age > 22;
-- 创建01班级的学生的视图
CREATE VIEW stu_class_one
(id,name,sex,age,login_date,class_name)
AS SELECT a.id,a.name,a.sex,a.age,a.login_date,b.name
FROM stu a,class b
WHERE class_id=01 AND a.class_id=b.id;
-- 更新学生HOWARD的年龄
UPDATE stu_class_one
SET age=age-1
WHERE name='HOWARD';
-- 查看创建的视图
SELECT * FROM information_schema.views\G
-- 删除创建的视图
DROP VIEW stu_orlder;
DROP VIEW stu_older;
-- 【存储过程】（p299）
-- 创建存储过程
DELIMITER //
CREATE PROCEDURE getStuInfo
(IN id int(11))
BEGIN
SELECT id,a.name,b.name
FROM stu a,class b
WHERE a.class_id=b.id
AND a.id=id;
END //
-- 调用存储过程
DELIMITER ;
CALL getStuInfo(103);
-- 【触发器】（p338）
-- 创建数据表stu_login
CREATE TABLE stu_login
(
id INT NOT NULL PRIMARY KEY,
name VARCHAR(25) NOT NULL,
login_date DATE 
);
-- 创建数据表stu_years
CREATE TABLE stu_years
(
id INT NOT NULL PRIMARY KEY,
name VARCHAR(25) NOT NULL,
years INT 
);
-- 创建触发器get_years
CREATE TRIGGER get_years
AFTER INSERT ON stu_login
FOR EACH ROW
INSERT INTO stu_years
VALUES(NEW.id,NEW.name,
YEAR(CURDATE())-YEAR(NEW.login_date));
-- 向stu_login
INSERT INTO stu_login VALUES
(101,'JAMES','2014-07-31'),
(102,'HOWARD','2015-07-31'),
(103,'SMITH','2013-03-15');
-- 【索引】（p273）
-- 创建学生索引表
CREATE TABLE stu_index
(
id INT NOT NULL PRIMARY KEY,
name VARCHAR(25) NOT NULL,
sex VARCHAR(2) NOT NULL,
age INT NOT NULL,
login_date DATE NOT NULL,
UNIQUE INDEX uni_idx(id),
INDEX multi_idx(name(25),sex(2))
);
-- 创建班级索引表
CREATE TABLE class_index
(
id INT NOT NULL PRIMARY KEY,
name VARCHAR(25) NOT NULL,
grade VARCHAR(10) NOT NULL,
t_name VARCHAR(25) NOT NULL
);
-- 添加唯一索引
ALTER TABLE class_index
ADD UNIQUE INDEX uni_c_idx(id DESC);
-- 添加普通索引
ALTER TABLE class_index
ADD INDEX com_grade_idx(grade);
-- 添加组合索引
CREATE INDEX multi_col_idx
ON class_index(name,grade);
-- 删除索引
ALTER TABLE class_index
DROP INDEX com_tname_idx;
DROP INDEX multi_col_idx ON class_index;
-- 【用户与权限】（p368）
-- 创建新用户
GRANT SELECT,UPDATE(id,name,grade,t_name)
ON class
TO 'adminNew'@'localhost' IDENTIFIED BY '123'
WITH MAX_CONNECTIONS_PER_HOUR 30;
-- 查询账户信息
SELECT host,user,select_priv,update_priv
FROM mysql.user
WHERE user='adminNew';
-- 查询表权限信息
SELECT host,db,user,table_name,table_priv,column_priv
FROM mysql.tables_priv
WHERE user='adminNew';
-- 查询列权限信息
SELECT host,db,user,table_name,column_priv,column_priv
FROM mysql.columns_priv
WHERE user='adminNew';
-- 查看账户的权限信息
SHOW GRANTS FOR 'adminNew'@'localhost';
-- 收回账户权限
REVOKE SELECT,UPDATE
ON school.class
FROM 'adminNew'@'localhost';
-- 删除用户
DROP USER 'adminNew'@'localhost';
-- 【备份和还原】（p399）
-- 使用mysqldump备份
C:\Users\USER>mysqldump -u root -p school students > D:\mysql_backup\students_bk.sql
-- 使用mysqldump还原
SOURCE D:/mysql_backup/students_bk.sql;
-- 数据库备份
SELECT * FROM school.stu
INTO OUTFILE 'D:/Uploads/students_out.txt'
FIELDS
TERMINATED BY ','
ENCLOSED BY '\"'
LINES
STARTING BY '<'
TERMINATED BY '>\r\n';
-- 数据库还原
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/students_out.txt'
INTO TABLE school.students
FIELDS
TERMINATED BY ','
ENCLOSED BY '\"'
LINES
STARTING BY '<'
TERMINATED BY '>\r\n';
CREATE TABLE tb_students_info
(
id INT NOT NULL PRIMARY KEY,
name VARCHAR(25) NOT NULL,
dept_id INT NOT NULL,
age INT,
sex VARCHAR(2) NOT NULL,
height INT,
login_date DATE
);
INSERT INTO tb_students_info VALUES
(1,'Dany',01,25,'F','160','2015-09-10'),
(2,'Green',03,23,'F','158','2016-10-22'),
(3,'Henry',02,23,'M','185','2015-05-31'),
(4,'Jane',01,22,'F','162','2016-12-20'),
(5,'Jim',01,24,'M','175','2016-01-15'),
(6,'John',02,21,'M','172','2015-11-11'),
(7,'Lily',06,22,'F','165','2016-02-26'),
(8,'Susan',04,23,'F','170','2015-10-01'),
(9,'Thomas',03,22,'M','178','2016-06-07'),
(10,'Tom',04,23,'M','165','2016-08-05');
CREATE TABLE tb_departments
(
dept_id INT NOT NULL PRIMARY KEY,
dept_name VARCHAR(25) NOT NULL,
dept_call INT,
dept_type VARCHAR(25) NULL
);
INSERT INTO tb_departments VALUES
(1,'computer','11111','A'),
(2,'math','22222','A'),
(3,'chinese','33333','B'),
(4,'economy','44444','B'),
(5,'history','55555','B');
select * from tb_departments;
select * from tb_students_info;
```

