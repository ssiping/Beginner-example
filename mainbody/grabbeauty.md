#### 编写代码

1、首先引入我们所需要的模块

```python
import requests
import os
```

2、开始代码编写

2.1 特别说明

```python
###
想要实现百度图片下载多页，经过分析，我发现在我们提交的参数里，pn代表的是从第几张图片开始加载，顺着这个思路我们可以给上面的代码套一个大循环，即第一次下载从第1张开始，下载三十张，第二次从第31张开始下载。
###
```

2.2 浏览器伪装

```python
#进行UA伪装
header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
```

2.3 url地址

```python
#url地址
url = 'https://image.baidu.com/search/acjson?'
```

2.4  抓取参数

```python
#参数表
param = {
        'tn': 'resultjson_com',
        'logid': '8846269338939606587',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'queryWord': '性感美女',
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '-1',
        'z':'' ,
        'ic':'' ,
        'hd': '',
        'latest': '',
        'copyright': '',
        'word': '性感美女',
        's':'' ,
        'se':'' ,
        'tab': '',
        'width': '',
        'height': '',
        'face': '0',
        'istype': '2',
        'qc': '',
        'nc': '1',
        'fr': '',
        'expermode': '',
        'force': '',
        'cg': 'girl',
        'pn': pn,#从第几张图片开始
        'rn': '30',
        'gsm': '1e',
    }
```

2.5 自动生成文件夹，抓取的图片放在里面

```python
#生成文件夹
os.makedirs('download/images',exist_ok=True)
```

2.6 编码转换

```python
#将编码形式转换为utf-8 
page_text = requests.get(url=url,headers=header,params=param)
page_text.encoding = 'utf-8'
```

2.7 将图片地址进行存储

```python
page_text = page_text.json()
#将返回数据转换为json格式
info_list = page_text['data']
#先取出所有链接所在的字典，并将其存储在一个列表当中
del info_list[-1]
#由于利用此方式取出的字典最后一个为空，所以删除列表中最后一个元素
```

2.8 下载图片进行存储

```python
img_path_list = []
#定义一个存储图片地址的列表
for i in info_list:
    img_path_list.append(i['thumbURL'])
    #将图片地址全部存储在列表中
for img_path in img_path_list:
    img_data = requests.get(url=img_path,headers=header).content
    img_path = 'download/images/' + str(n) + '.jpg'
    with open(img_path,'wb') as fp:
        fp.write(img_data)
    n = n + 1
    #再将所有的图片地址取出，进行下载
    #n将作为图片的名字
```

3、完整代码

```python
import requests
import os
page = input('请输入要爬取多少页：')
os.makedirs('download/images',exist_ok=True)
page = int(page) + 1
header = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
n = 0
pn = 1
#pn是从第几张图片获取 百度图片下滑时默认一次性显示30张
for m in range(1,page):
    url = 'https://image.baidu.com/search/acjson?'
    param = {
        'tn': 'resultjson_com',
        'logid': '8846269338939606587',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'queryWord': '性感美女',
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '-1',
        'z':'' ,
        'ic':'' ,
        'hd': '',
        'latest': '',
        'copyright': '',
        'word': '性感美女',
        's':'' ,
        'se':'' ,
        'tab': '',
        'width': '',
        'height': '',
        'face': '0',
        'istype': '2',
        'qc': '',
        'nc': '1',
        'fr': '',
        'expermode': '',
        'force': '',
        'cg': 'girl',
        'pn': pn,#从第几张图片开始
        'rn': '30',
        'gsm': '1e',
    }
    page_text = requests.get(url=url,headers=header,params=param)
    page_text.encoding = 'utf-8'
    page_text = page_text.json()
    info_list = page_text['data']
    del info_list[-1]
    img_path_list = []
    for i in info_list:
        img_path_list.append(i['thumbURL'])
    for img_path in img_path_list:
        img_data = requests.get(url=img_path,headers=header).content
        img_path = 'download/images/' + str(n) + '.jpg'
        with open(img_path,'wb') as fp:
            fp.write(img_data)
        n = n + 1
    pn += 29
```

