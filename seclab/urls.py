"""seclab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from virus import views,urls
from django.views.generic import RedirectView
from django.conf.urls import url,include

urlpatterns = [
    #admin后台
    path('admin/', admin.site.urls),
    #调试base
    path('base/',views.showbase,name='base'),
    #功能
    #病毒处理记录
    path('info/', views.info, name='info'),
    path('addinfo/', views.addinfo, name='addinfo'),
    path('delinfo/<int:info_id>', views.deleteinfo, name='delinfo'),
    path('sendmail/', views.sendmail, name='sendmail'),
    path('searchinfo/',views.searchinfo, name='searchinfo'),
    #物资请购
    path('addasset/',views.addasset,name='addasset'),
    path('delassetinfo/<int:assetinfo_id>', views.delassetinfo, name='delassetinfo'),
    path('searchassetinfo/',views.searchassetinfo, name='searchassetinfo'),
    #path('/mail/',views.showsendmail,name='mail'),
    #start页面相关
    path('', RedirectView.as_view(url='start/')),
    path('start/', views.IndexView.as_view(), name='start'),
    url(r'^start/', include("virus.urls")),
    #login页面相关
    path('login/',views.login,name='login'),
    path('userlogin/',views.userlogin,name='userlogin'),
]