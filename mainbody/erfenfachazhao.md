##### 二分法猜一个数

方法一、数列

```python
list=[]
minbetween=int(input("请输入数值范围，最小值是："))
maxbetween=int(input("请输入数值范围，最大值是："))
while True:
    for i in range(minbetween,maxbetween+1):
        list.append(i)
    guessnumber=(list[0]+list[-1])//2
    print("我猜数字可能是：",guessnumber)
    decide=input("我猜得对不对(大了d、小了x、正确z）")
    if decide=="z":
        print("猜对了！")
        break
    elif decide=="d":
        maxbetween=guessnumber
        list=[]
    elif decide=="x":
        minbetween=guessnumber
        list=[]
```

方法二、直接计算

```python
minbetween=int(input("请输入数值范围，最小值是："))
maxbetween=int(input("请输入数值范围，最大值是："))
while True:
    guessnumber=(minbetween+maxbetween)//2
    print("我猜数字可能是：",guessnumber)
    decide=input("我猜得对不对(大了d、小了x、正确z）")
    if decide=="z":
        print("猜对了！")
        break
    elif decide=="d":
        maxbetween=guessnumber
    elif decide=="x":
        minbetween=guessnumber
```

