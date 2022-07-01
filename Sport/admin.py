from django.contrib import admin
from .models import *


# Register your models here.


class SportRunAdmin(admin.ModelAdmin):
    list_display = ['user', 'run_time', 'run_distance', 'run_calorie', 'sport_mark']
    list_filter = ['user']  # 过滤字段
    search_fields = ['user']  # 搜索字段
    list_per_page = 10


class SportSwimAdmin(admin.ModelAdmin):
    list_display = ['user', 'swim_time', 'swim_calorie']
    list_filter = ['user']  # 过滤字段
    search_fields = ['user']  # 搜索字段
    list_per_page = 10


class SportCyclingAdmin(admin.ModelAdmin):
    list_display = ['user', 'cycling_time', 'cycling_calorie', 'sport_mark']
    list_filter = ['user']  # 过滤字段
    search_fields = ['user']  # 搜索字段
    list_per_page = 10


class SportFootballAdmin(admin.ModelAdmin):
    list_display = ['user', 'football_time', 'football_calorie', 'sport_mark']
    list_filter = ['user']  # 过滤字段
    search_fields = ['user']  # 搜索字段
    list_per_page = 10


class SportImgAdmin(admin.ModelAdmin):
    list_display = ['pk', 'sportname', 'img_url']
    list_filter = ['sportname']  # 过滤字段
    search_fields = ['sportname']  # 搜索字段
    list_per_page = 10


'''注册表单'''
admin.site.register(SportImg, SportImgAdmin)
admin.site.register(SportFootball, SportFootballAdmin)
admin.site.register(SportRun, SportRunAdmin)
admin.site.register(SportCycling, SportCyclingAdmin)
admin.site.register(SportSwim, SportSwimAdmin)
