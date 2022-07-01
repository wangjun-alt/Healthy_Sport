from django.contrib import admin
from django.urls import path, include
from Sport import views

urlpatterns = [
    path('run/', views.RunView.as_view()),  # 跑步消耗计算以及统计
    path('swim/', views.SwimView.as_view()),  # 游泳消耗计算以及统计
    path('cycle/', views.CyclingView.as_view()),  # 骑自行车消耗计算以及统计
    path('football/', views.FootballView.as_view())  # 足球消耗计算以及统计
]