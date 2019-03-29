"""blinkled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include

from led import views

urlpatterns = [ url(r'^$', views.blinker),
]

"""
urlpatterns = [

url(r'^$', views.redon, name='redon'),
url(r'^$', views.redoff, name='redoff'),
url(r'^$', views.greenon, name='greenon'),
url(r'^$', views.greenoff, name='greenoff'),
url(r'^$', views.blueon, name='blueon'),
url(r'^$', views.blueoff, name='blueoff'),
]
"""

"""
path('redon/', views.redon),
path('redoff/', views.redoff),
path('greenon/', views.greenon),
path('greenoff/', views.greenoff),
path('blueon/', views.blueon),
path('blueoff/', views.blueoff),
"""
