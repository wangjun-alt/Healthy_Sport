from django.contrib import admin
from Dish import views
from django.urls import path, include

urlpatterns = [
    path('search/', views.SearchView.as_view()),   # 菜品信息搜索
    # path('banner/image/', views.BannerView.as_view()),  # 获取主页轮播图
    path('konwledge/', views.KnowledgeView.as_view()),  # 科普知识获取
    path('found/', views.DishfoundView.as_view()),  # 菜品识别以及相关计算
]