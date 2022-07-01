from django.contrib import admin
from .models import *
# Register your models here.


class KnowledgeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'text_id', 'title', 'health_text']
    list_filter = ['text_id', 'title']  # 过滤字段
    search_fields = ['text_id', 'title']  # 搜索字段
    list_per_page = 10


class DishinfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'dish_name', 'dish_heat', 'dish_carbohydrate', 'dish_protein', 'dish_fat', 'dish_cholesterol',
                    'dish_mineral', 'dish_carotene', 'dish_vitamin_A', 'dish_vitamin_C', 'dish_vitamin_E',
                    'dish_vitamin_B1', 'dish_vitamin_B2', 'dish_dietary']
    list_filter = ['dish_name']  # 过滤字段
    search_fields = ['dish_name']  # 搜索字段
    list_per_page = 10


class CarouselAdmin(admin.ModelAdmin):
    list_display = ['pk', 'number', 'img_url']
    list_filter = ['number']  # 过滤字段
    search_fields = ['number']  # 搜索字段
    list_per_page = 10


'''注册表单'''
admin.site.register(HealthKnowledge, KnowledgeAdmin)
admin.site.register(Dishinfo, DishinfoAdmin)
admin.site.register(Carousel, CarouselAdmin)
