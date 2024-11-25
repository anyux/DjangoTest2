## csrf

### 1.csrf 攻击
csrf全拼为Cross Site Request Forgery,译为 跨站请求伪造.CSRF指攻击者盗用了你的身份,以你的名义发送恶意请求
csrf能够做的事情包括:以你的名意发送邮件,消息,盗取账号,购买商品,虚拟倾向转账.导致个人隐私泄露及财产安全

### 2.django防止csrf的方式
1. 默认打开csrf中间件
2. 表单post提交数据时加上{% csrf_token %}标签

防御原理:
1. 渲染模板文件时在页面生成一个名字叫做csrfmiddlewaretoken的隐藏域
2. 服务器交给浏览器保存一个名字为csrftoken的cookie信息
3. 提交表单时,两个值都会发送给服务器,服务器进行比对,如果一样,则csrf验证通过,否则失效
当启用中间件并加入标签csrf_token后,会向客户端提交浏览器写入一条cookie信息,这条信息的值与隐藏域input元素的value属性是一致的,
提交到服务器后会先由csrf中间件进行验证,比如对比失败则返回403页面,而不会进行后续的处理

csrf_token.html
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>csrf_token</title>
</head>
<body>
<form method="post">
    {% csrf_token %}
    <input type="text" name="">
    <input type="password">
    <button type="submit">提交</button>
</form>
</body>
</html>
```

news/views.py
```html
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    print(request.method)
    return JsonResponse({"code":"hello"})

def csrf_token(request):
    if request.method == "POST":
        return JsonResponse({"code":"hello"})
    else:
        return render(request,'csrf_token.html')
```

news/urls.py
````python
from django.urls import path, re_path

from news import views

urlpatterns = [

       re_path(r'^index/$', views.index, name='index'),
       re_path(r'^csrf_token/$', views.csrf_token, name='index'),
]
````