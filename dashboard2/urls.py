"""config URL Configuration

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
from django.urls import path, include

from dashboard2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard1', views.dashboard1, name='dashboard1'),
    path('dashboard2', views.dashboard2, name='dashboard2'),
    path('dashboard3', views.dashboard3, name='dashboard3'),
    path('health01', views.health01, name='health01'),
    path('health02', views.health02, name='health02'),
    path('health03', views.health03, name='health03'),
    path('health04', views.health04, name='health04'),
    path('health05', views.health05, name='health05'),
    path('health06', views.health06, name='health06'),
    path('health07', views.health07, name='health07'),
    path('health08', views.health08, name='health08'),
    path('health09', views.health09, name='health09'),
    path('health10', views.health10, name='health10'),
    path('health11', views.health11, name='health11'),

    path('region01', views.region01, name='region01'),
    path('region02', views.region02, name='region02'),
    path('region03', views.region03, name='region03'),
    path('region04', views.region04, name='region04'),
    path('region05', views.region05, name='region05'),
    path('region06', views.region06, name='region06'),
    path('region07', views.region07, name='region07'),
    path('region08', views.region08, name='region08'),
    path('region09', views.region09, name='region09'),
    path('region10', views.region10, name='region10'),
    path('region11', views.region11, name='region11'),
    path('region12', views.region12, name='region12'),
    path('region13', views.region13, name='region13'),
    path('region14', views.region14, name='region14'),
    path('region15', views.region15, name='region15'),
    path('region16', views.region16, name='region16'),
    path('year2009', views.year2009, name='year2009'),
    path('year2010', views.year2010, name='year2010'),
    path('year2011', views.year2011, name='year2011'),
    path('year2012', views.year2012, name='year2012'),
    path('year2013', views.year2013, name='year2013'),
    path('year2014', views.year2014, name='year2014'),
    path('year2015', views.year2015, name='year2015'),
    path('year2016', views.year2016, name='year2016'),
    path('year2017', views.year2017, name='year2017'),
    path('year2018', views.year2018, name='year2018'),

    path('mlr99', views.mlr99, name='mlr99'),
    path('mlr01', views.mlr01, name='mlr01'),
    path('mlr02', views.mlr02, name='mlr02'),
    path('mlr03', views.mlr03, name='mlr03'),
    path('mlr04', views.mlr04, name='mlr04'),
    path('mlr05', views.mlr05, name='mlr05'),

]
