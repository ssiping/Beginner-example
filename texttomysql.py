#模块的导入
import pandas as pd
df = pd.read_table(r"D:\texttest.txt")
print(df)
print(df.shape)
print(df.info())
print(df.describe())
