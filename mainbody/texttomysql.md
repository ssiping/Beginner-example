[回主页](https://github.com/ssiping/Beginner-example)
#### text文件数据导入
```python
#模块的导入
import pandas as pd
df = pd.read_table(r"texttest.txt")
print(df)
```
|    | 年龄| 性别 |
|:--:| :--:| :--: |
|0| 54|  男  |
|1| 16 |  女  |
|2| 47|  女  |
|3| 41|  男|
|4| 51  |女|
|5| 26|男|
#### shape方法获取数据表的行和列
```python
#模块的导入
import pandas as pd
df = pd.read_table(r"texttest.txt")
print(df)
print(df.shape)
```
#### info()方法查看数据表的数据类型
```python
#模块的导入
import pandas as pd
df = pd.read_table(r"texttest.txt")
print(df)
print(df.info())
```
#### describe()方法获取数值类型字段的分布值
```python
#模块的导入
import pandas as pd
df = pd.read_table(r"texttest.txt")
print(df)
print(df.describe())
```
[回主页](https://github.com/ssiping/Beginner-example)