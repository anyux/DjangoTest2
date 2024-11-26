import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from booksmanage.models import Books


# Create your views here.

class LoginView(View):
    """登录验证"""

    def get(self, request):
        return render(request, 'login.html')


    def post(self, request):
        """
        用户登录
        Args:
            request:

        Returns:

        """

        """
                # form表单提交数据
        if len(request.POST) > 0:
            username = request.POST['username']
            password = request.POST['password']
            content_type = request.content_type
            print(content_type)
            print(request)
            print(username, password)
        elif len(request.body) > 0:
            print(request)
            username = json.loads(request.body)['username']
            password = json.loads(request.body)['password']
            content_type = request.content_type
            print(content_type)
            print(username, password)
        return JsonResponse({"status": True,"username":username,"password":password,"content_type":content_type})
        """
        #通过三元表达式处理,可以兼容form表单和json数据
        params = request.POST if len(request.POST) else json.loads(request.body)

        username = params.get('username')
        password = params.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({"status": 200, "msg": "ok"})
        else:
            return JsonResponse({"status": 403, "msg": "username or password error"})

class LogoutView(View):

    def get(self, request):
        logout(request)
        return JsonResponse({"status": 200, "msg": "logout success"})

class BookView(View):
    """
    图书管理的接口
    """

    def get(self, request):
        """
        获取图书列表
        Args:
            request:

        Returns:

        """
        # 给book图书列表,添加用户登录才能查看的权限限制
        if not request.user.is_authenticated:
            res = {
                "code":2002,
                "message":"Authentication failed, you do not have access rights"
            }
            return JsonResponse(res)
        books = Books.objects.all()
        #获取所有图书信息
        data = []
        for book in books:
            dic = {
                "id":book.id,
                "name":book.name,
                "status":book.status,
            }
            data.append(dic)
        #列表推导式获取数据
        # data = [{
        #     "id":book.id,
        #     "name":book.name,
        #     "status":book.status,
        # } for book in data]
        res = {
            "code":1000,
            "message":"success",
            "data":data
        }
        return JsonResponse(res)

    def post(self, request):
        """
        添加图书
        Args:
            request:

        Returns:

        """
        # 状态认证
        if not request.user.is_authenticated:
            res = {
                "code":2002,
                "message":"Authentication failed, you do not have access rights"
            }
            return JsonResponse(res)
        #获取参数
        params = request.POST if len(request.POST) else json.loads(request.body)

        id = params.get('id')
        name = params.get('name')

        #检查参数
        #检查数据是否为空
        if not (id and name):
            return JsonResponse({"code":2002,"message":"id or name error"})
        #检查数据类型
        if not isinstance(id,str):
            return JsonResponse({"code":2003,"message":"id error"})
        #检查数据类型
        if not isinstance(name,str):
            return JsonResponse({"code":2003,"message":"name error"})
        # 检查id是存在
        if Books.objects.filter(id=id).exists():
            return JsonResponse({"code":2003,"message":f"books id:{id} is exists"})

        #添加图书
        try:
            Books.objects.create(id=id,name=name)
        except Exception as e:
            # 如果添加失败
            return JsonResponse({"code":2003,"message":f"books id:{id} add error:{e}"})
        else:
            return JsonResponse({"code":1000,"message":"success"})



    def delete(self, request):
        """
        删除图书
        Args:
            request:

        Returns:

        """
        # 状态认证
        if not request.user.is_authenticated:
            res = {
                "code":2002,
                "message":"Authentication failed, you do not have access rights"
            }
            return JsonResponse(res)
        #获取参数
        id = request.GET.get('id',None)
        #检查参数
        #检查数据是否为空
        if not id:
            return JsonResponse({"code":2002,"message":"id  error"})
        #检查数据类型
        if not isinstance(id,str):
            return JsonResponse({"code":2003,"message":"id error"})
        
        #删除图书
        try:
            books=Books.objects.get(id=id)
        except Exception as e:
            # 如果删除失败
            return JsonResponse({"code":2003,"message":f"books id:{id} info error:{e}"})
        else:
            books.delete()
            return JsonResponse({"code":1000,"message":f"books id:{id} delete success"})