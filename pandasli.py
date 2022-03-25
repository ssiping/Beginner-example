#模块的导入
import pandas as pd
import numpy as np
import matplotlib as plt
S1 = pd.Series(["a","b","c","d"])
print(S1)
print(S1.index)
S2 = pd.Series([1,2,3,4],index = ["a","b","c","d"])
print(S2)
print(S2.index)
S3 = pd.Series({"a":1,"b":2,"c":3,"d":4})
print(S3)
print(S3.index)
print("****************")
df31 = pd.DataFrame([["a","A"],["b","B"],["c","C"],["d","D"]],columns = ["小写","大写"])
print(df31)
print("****************")
df32 = pd.DataFrame([["a","A"],["b","B"],["c","C"],["d","D"]],index = ["一","二","三","四"])
print(df32)
print("****************")
df33 = pd.DataFrame([["a","A"],["b","B"],["c","C"],["d","D"]],columns = ["小写","大写"],index = ["一","二","三","四"])
print(df33)
print("****************")
data = {"小写":["a","b","c","d"],"大写":["A","B","C","D"]}
df41 = pd.DataFrame(data)
print(df41)
print("****************")
data = {"小写":["a","b","c","d"],"大写":["A","B","C","D"]}
df42 = pd.DataFrame(data,index = ["一","二","三","四"])
print(df42)
print(df42.columns)
print(df42.index)
print("****************")
df = pd.read_excel(r"D:\6 - 随书数据集\test.xlsx",sheet_name = "Sheet1",header = None)#index_col = 0,
print(df)
for i in df:
    print(i)
print("****************")
df = pd.read_excel(r"D:\6 - 随书数据集\test.xlsx")
print(df)
print(type(df))
df = pd.read_excel(r"D:\6 - 随书数据集\test.xlsx",usecols =[0,2],header = None)
print(df)
#print(df.iat["0","编号"])
print(df[0][0])



