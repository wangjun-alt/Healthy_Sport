from django.contrib import admin
from django.urls import path, include
from User import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),  # 微信用户登录
    path('info/save/', views.SaveView.as_view()),   # 微信用户信息post保存
    path('feedback/', views.FeedView.as_view()),    # 用户反馈与建议信息保存
    path('weight/', views.WightView.as_view()),     # 用户的体重日记
    path('userinfo/', views.InfoView.as_view()),  # 用户信息的获取以及修改（get、update）
    path('sport/', views.SportView.as_view()),      # 用户的卡路里日记
    path('items/', views.SportItemsView.as_view())   # 获取用户运动的项目
]
