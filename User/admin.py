from django.contrib import admin
from.models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['open_id', 'biography', 'username', 'user_gender', 'age', 'brontime',
                    'height', 'weight', 'BMI', 'bodyfat_rate', 'last_time', 'metabolism']
    list_filter = ['open_id']  # 过滤字段
    search_fields = ['open_id']  # 搜索字段
    list_per_page = 10


class FeedAdmin(admin.ModelAdmin):
    list_display = ['user', 'feed_text']
    list_filter = ['user']  # 过滤字段
    search_fields = ['user']  # 搜索字段
    list_per_page = 10


class UserSportAdmin(admin.ModelAdmin):
    list_display = ['user', 'sport_consume', 'sport_time', 'sport_target', 'sport_consume',
                    'sport_residualheat']
    list_filter = ['user']  # 过滤字段
    search_fields = ['user']  # 搜索字段
    list_per_page = 10


class UserWeightsAdmin(admin.ModelAdmin):
    list_display = ['user', 'weight_one', 'weight_two', 'weight_three', 'weight_four', 'weight_five']
    list_filter = ['user']  # 过滤字段
    search_fields = ['user']  # 搜索字段
    list_per_page = 10


class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'search_one', 'search_two', 'search_three']
    list_filter = ['user']  # 过滤字段
    search_fields = ['user']  # 搜索字段
    list_per_page = 10


'''注册表单'''
admin.site.register(Userinfo, UserAdmin)
admin.site.register(Feedback, FeedAdmin)
admin.site.register(UserSportNotes, UserSportAdmin)
admin.site.register(UserWeights, UserWeightsAdmin)
admin.site.register(UserSearchHistory, SearchHistoryAdmin)