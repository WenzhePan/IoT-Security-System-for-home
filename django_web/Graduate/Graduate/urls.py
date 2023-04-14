"""Graduate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import mqtt
from django.conf.urls import url
#from . import views
from GetData.views import get_id,index,ajax_humi,ajax_temp,ajax_echo,ajax_depth,ajax_smoke,ajax_fire,ajax_date,ctrl,close
from login import views
from echarts.views import date,door,get_door
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    url(r'^index/', index),
    url(r'^get_door/', get_door),
    # path('get_id/',get_id,name='add'),
    url(r'^get_id$',get_id,name='get_id'),
    url(r'^ajax_humi$',ajax_humi),
    url(r'^ajax_temp$',ajax_temp),
    url(r'^ajax_echo$',ajax_echo),
    url(r'^ajax_depth$',ajax_depth),
    url(r'^ajax_smoke$',ajax_smoke),
    url(r'^ajax_date$',ajax_date),
    url(r'^ajax_fire$',ajax_fire),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^Jump_R/', views.Jump_R),
    url(r'^logout/', views.logout),
    url(r'^L/',views.L),
    url(r'^date$',date),
    url(r'^door$',door),
    url(r'^ctrl/',ctrl),
    url(r'^close/',close),
]
