##### 迭代器转换为生成器函数

编写一个可以无限迭代斐波那契数列的Python迭代器类，并将其转换为生成器函数，
然后通过for循环迭代这个生成器函数，并输出迭代及结果。迭代值不能超过1000

```python
class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        result = self.b
        self.a,self.b = self.b, self.a + self.b
        if result > 1000: raise StopIteration
        return result
def fibonacciGenerator():
    for f in Fibonacci():
        yield f
for s4r in fibonacciGenerator():
    print(s4r, end = ' ')
```

