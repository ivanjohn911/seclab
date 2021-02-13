from django.conf.urls import url
from virus import views
from django.urls import path

urlpatterns = [
    url(r'info', views.info,name='info'),
    url(r'sendmail/', views.sendmail,name='sendmail'),
    url(r'mail', views.showsendmail,name='mail'),
    url(r'search',views.showsearch,name='search'),
    url(r'showqueryasset',views.showqueryasset,name='showqueryasset'),
    url(r'showasset',views.assetinfo,name='showasset'),
    url(r'showaddasset',views.showaddasset,name='showaddasset')
]