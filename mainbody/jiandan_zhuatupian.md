##### 煎蛋网抓取妹子

1、输入模块

```python
# -*- coding:utf-8 -*-
#  author: yukun
import requests
import lxml
import os
import time
from bs4 import BeautifulSoup
```

2、获得HTML源码

```python
def get_html(url):
    # 指定一个浏览器头
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
    # 代理，免费的代理只能维持一会可能就没用了，自行更换
    proxies = {'http': '174.41.84.203'}
    try:
        # Requests库的get请求
        resp = requests.get(url, headers=headers)
    except:
        # 如果请求被阻，就使用代理
        resp = requests.get(url, headers=headers, proxies=proxies)
     return resp
```

3、创建文件夹

```python
def mkdir(path):
    # os.path.exists(name)判断是否存在路径
    # os.path.join(path, name)连接目录与文件名
    isExists = os.path.exists(os.path.join("D:\jiandan", path))
    # 如果不存在
    if not isExists:
        print('makedir', path)
        # 创建文件夹
        os.makedirs(os.path.join("D:\jiandan", path))
        # 切换到创建的文件夹
        os.chdir(os.path.join("D:\jiandan", path))
        return True
    # 如果存在了就返回False
    else:
        print(path, 'already exists')
        return False
```

4、获得图片地址并下载

```python
def get_imgs():
    # 调用函数获得所有页面
    i=1
    for url in all_page():
        
        path = str('D:\jiandan/')+str(i)
        # 创建文件夹的函数
        mkdir(path)
        # 调用请求函数获得HTML源码
        html = get_html(url).text
        # 使用lxml解析器，也可以使用html.parser
        soup = BeautifulSoup(html, 'lxml')
        # css选择器
        allimgs = soup.select('div.text>p>img')
        # 调用download函数下载保存
        download(allimgs)
        i=i+1
    # 执行完毕打出ok
    print('ok')
```

5、获得所有页面的图片地址

```python
def all_page():
    urllist = []
    base_url = 'http://jandan.net/girl'
    # BeautifulSoup解析页面得到最高页码数
    urllist.append(base_url)  
    soup = BeautifulSoup(get_html(base_url).text, 'lxml')
    # 获得最高页码数
    allpage = soup.find('span', class_="current-comment-page").get_text()[1:-1]
    page = soup.find('a', class_="previous-comment-page").attrs['href'][2:]
    page="http://"+page
    urllist.append(page)
    for i in range(2, int(allpage)-1):
        soup = BeautifulSoup(get_html(page).text,'lxml')
        page = soup.find('a', class_="previous-comment-page").attrs['href'][2:]
        page="http://"+page
        urllist.append(page)
        i+=1
    return urllist
    # for循环迭代出所有页面，得到url
    # for page in range(1, int(allpage)+1):
        # allurl = base_url + 'page-' + str(page)
        # urllist.append(allurl)
    # return urllist
```

6、保存图片函数

```python
def download(list):
    for img in list:
        urls = img['src']
        # 判断url是否完整
        if urls[0:5] == 'http:':
            img_url = urls
        else:
            img_url = 'http:' + urls
        filename = img_url.split('/')[-1]
        # 保存图片
        with open(filename, 'wb') as f:
            # 直接过滤掉保存失败的图片，不终止程序
            try:
                f.write(get_html(img_url).content)
                print('Sucessful image:',filename)
            except:
                print('Failed:',filename)
```

7、主程序入口并计时

```python
 if __name__ == '__main__':
    # 计时
    t1 = time.time()
    # 调用函数
    get_imgs()
    print(time.time() - t1)
```

8、完整代码

```python
# -*- coding:utf-8 -*-
#  author: yukun
import requests
import lxml
import os
import time
from bs4 import BeautifulSoup
i=1
# 发出请求获得HTML源码
def get_html(url):
    # 指定一个浏览器头
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
    # 代理，免费的代理只能维持一会可能就没用了，自行更换
    proxies = {'http': '174.41.84.203'}
    try:
        # Requests库的get请求
        resp = requests.get(url, headers=headers)
    except:
        # 如果请求被阻，就使用代理
        resp = requests.get(url, headers=headers, proxies=proxies)
     return resp
 # 创建文件夹的函数，保存到D盘
def mkdir(path):
    # os.path.exists(name)判断是否存在路径
    # os.path.join(path, name)连接目录与文件名
    isExists = os.path.exists(os.path.join("D:\jiandan", path))
    # 如果不存在
    if not isExists:
        print('makedir', path)
        # 创建文件夹
        os.makedirs(os.path.join("D:\jiandan", path))
        # 切换到创建的文件夹
        os.chdir(os.path.join("D:\jiandan", path))
        return True
    # 如果存在了就返回False
    else:
        print(path, 'already exists')
        return False
 # 获得图片地址调用download函数进行下载
def get_imgs():
    # 调用函数获得所有页面
    i=1
    for url in all_page():
        
        path = str('D:\jiandan/')+str(i)
        # 创建文件夹的函数
        mkdir(path)
        # 调用请求函数获得HTML源码
        html = get_html(url).text
        # 使用lxml解析器，也可以使用html.parser
        soup = BeautifulSoup(html, 'lxml')
        # css选择器
        allimgs = soup.select('div.text>p>img')
        # 调用download函数下载保存
        download(allimgs)
        i=i+1
    # 执行完毕打出ok
    print('ok')
 # 获得所有页面
def all_page():
    urllist = []
    base_url = 'http://jandan.net/girl'
    # BeautifulSoup解析页面得到最高页码数
    urllist.append(base_url)  
    soup = BeautifulSoup(get_html(base_url).text, 'lxml')
    # 获得最高页码数
    allpage = soup.find('span', class_="current-comment-page").get_text()[1:-1]
    page = soup.find('a', class_="previous-comment-page").attrs['href'][2:]
    page="http://"+page
    urllist.append(page)
    for i in range(2, int(allpage)-1):
        soup = BeautifulSoup(get_html(page).text,'lxml')
        page = soup.find('a', class_="previous-comment-page").attrs['href'][2:]
        page="http://"+page
        urllist.append(page)
        i+=1
    return urllist
    # for循环迭代出所有页面，得到url
    # for page in range(1, int(allpage)+1):
        # allurl = base_url + 'page-' + str(page)
        # urllist.append(allurl)
    # return urllist
 # 保存图片函数，传入的参数是一页所有图片url集合
def download(list):
    for img in list:
        urls = img['src']
        # 判断url是否完整
        if urls[0:5] == 'http:':
            img_url = urls
        else:
            img_url = 'http:' + urls
        filename = img_url.split('/')[-1]
        # 保存图片
        with open(filename, 'wb') as f:
            # 直接过滤掉保存失败的图片，不终止程序
            try:
                f.write(get_html(img_url).content)
                print('Sucessful image:',filename)
            except:
                print('Failed:',filename)
 if __name__ == '__main__':
    # 计时
    t1 = time.time()
    # 调用函数
    get_imgs()
    print(time.time() - t1)
```

