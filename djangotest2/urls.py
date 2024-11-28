"""
URL configuration for djangotest2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from booksmanage import views as booksmanage_views

urlpatterns = [
       path('admin/', admin.site.urls),
       path('news/', include('news.urls')),
       re_path(r'^user/login/?$', booksmanage_views.LoginView.as_view(), name='login'),
       re_path(r'^user/logout/?$', booksmanage_views.LogoutView.as_view(), name='logout'),
       re_path(r'^books/?$', booksmanage_views.BookView.as_view(), name='book'),
       re_path(r'^books/handler/?$', booksmanage_views.RecordView.as_view(), name='book'),
]
