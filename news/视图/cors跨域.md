## cors 跨域问题
针对于前后端分离的项目,前端和后端是分开部署的,因此服务端要支持cors(跨域资源共享)策略,需要在响应头中加上`Access-Control-Allow-Origin: *`

| 位置   | 域名             |
|------|----------------|
| 前端服务 | 127.0.0.1:8080 |
| 后端服务 | 127.0.0.1:8000 |

前端与后端分别是不同的端口,这就涉及到跨域访问数据的问题,因此浏览器同源策略,默认是不支持两个不同的域名间相互访问
需要后端添加跨域访问支持

### 1.后端 django配置

1. django-cors-headers
```bash
pip install django-cors-headers
```
2. 添加应用
settings.py
```python
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    # 'news',
    # 'books',
    'booksmanage'
]
```
配置跨域中间件
settings.py
```python
MIDDLEWARE = [
    #跨域中间件
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
配置开放白名单
settings.py
```python
#CORS
#对外开放白名单
CORS_ORIGIN_ALLOW_ALL = True
#允许跨域操作session会放
CORS_ALLOW_CREDENTIALS = True
#指定可以访问的跨域ip或域名
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8080',
    "http://192.168.8.101:8080",
)
```
- 浏览器会在第一次发送options请求询问后端是否允许跨域
- 后端在响应结果中告知浏览器允许跨域,允许的情况下浏览器再发送跨域请求

### 2.前端: axios配置
```javascript
// 允许axios跨域携带cookie
axios.defaults.withCredentials = true
```