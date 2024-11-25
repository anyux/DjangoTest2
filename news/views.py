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

def static_test(request):
    return render(request,'news/static_test.html')