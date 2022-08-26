from django.urls import path
from . import views

urlpatterns = [

    path('', views.mypage, name = "home"),
    path('about/', views.about, name = "about"),
    path('main/', views.main, name = "main")

]