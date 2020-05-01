"""backEnd URL Configuration

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
from rest_framework_jwt.views import obtain_jwt_token

from core import views

urlpatterns = [
    path('categories', views.CategoryList.as_view()),
    path('events', views.EventList.as_view()),
    path('categories/<int:pk>', views.CategoryDetail.as_view()),
    path('events/<int:pk>', views.EventDetail.as_view()),
    path('login', obtain_jwt_token),
    path('categories', views.CategoryList.as_view()),


]


