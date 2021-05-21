"""simbirsoft_test URL Configuration

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

urlpatterns = [
    path('', views.start),
    path('data/', views.data),
    path('q1/', views.q1,name='p1'),
    path('q2', views.q2,name='p2'),
    path('q3/', views.q3,name='p3'),
    path('q4/', views.q4,name='p4'),
    path('q5/', views.q5,name='p5'),
    path('result/', views.result,name='res'),

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
