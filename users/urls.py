#-*- coding = utf-8 -*-
#@Time : 2023/1/7 13:03
#@Author : 马卓然
#@File : urls.py.py
#@Software : PyCharm

'''为应用程序users定义URL模式'''

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # 包含默认的身份验证URL
    path('', include('django.contrib.auth.urls')),
    # 注册页面
    path('register/', views.register, name='register'),
]