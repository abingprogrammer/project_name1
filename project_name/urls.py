"""project_name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path  #Django 2.0 及以上：url的写法
from django.conf.urls import url #new Django 1.8.x － Django 1.11.x url的写法
from app_name import views as app_views  # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', app_views.index,),
    path('home/', app_views.home),
   # path('qrcode/<data>', app_views.generate_qrcode),

    url('^qrcode/(.+)$',app_views.generate_qrcode),
    path('hello/', app_views.hello),
]
