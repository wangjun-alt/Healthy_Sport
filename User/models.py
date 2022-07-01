from django.db import models

# Create your models here.


class Userinfo(models.Model):
    """用户的基本个人信息"""
    open_id = models.CharField(max_length=100, verbose_name='用户唯一标识符', primary_key=True, unique=True)
    username = models.CharField(max_length=100, verbose_name='微信用户名称')
    biography = models.CharField(max_length=200, verbose_name='个人简介', default='这个人很懒，还没有任何介绍。')
    gender = models.BooleanField(default=True, verbose_name='性别')
    age = models.IntegerField(verbose_name='年龄', null=True)
    brontime = models.DateField(verbose_name='出生日期', null=True)
    height = models.FloatField(verbose_name='身高', null=True)
    weight = models.FloatField(verbose_name='体重', null=True)
    BMI = models.FloatField(verbose_name='BMI', null=True)
    bodyfat_rate = models.FloatField(verbose_name='体脂率', null=True)
    last_time = models.DateField(verbose_name='用户最后一次登录时间', null=True)
    metabolism = models.FloatField(verbose_name='每日基础代谢卡路里', default=0)

    def user_gender(self):
        if self.gender:
            return '男'
        else:
            return '女'
    user_gender.short_description = "性别"

    def __str__(self):
        return self.open_id

    class Meta:
        verbose_name = '个人信息表'
        verbose_name_plural = verbose_name


class Feedback(models.Model):
    """反馈建议表"""
    user = models.ForeignKey(to=Userinfo, to_field="open_id", on_delete=models.CASCADE, verbose_name='用户唯一标识符')
    feed_text = models.TextField(verbose_name="反馈与建议", help_text="在这里填写反馈与建议")

    class Meta:
        verbose_name = '反馈与建议信息'
        verbose_name_plural = verbose_name


class UserWeights(models.Model):
    """用户的体重笔记"""
    user = models.ForeignKey(to=Userinfo, to_field="open_id", on_delete=models.CASCADE, verbose_name='用户唯一标识符')
    weight_one = models.FloatField(verbose_name='用户体重记录一', null=True)
    one_time = models.DateField(verbose_name='用户体重记录一的时间', null=True)
    weight_two = models.FloatField(verbose_name='用户体重记录二', null=True)
    two_time = models.DateField(verbose_name='用户体重记录二的时间', null=True)
    weight_three = models.FloatField(verbose_name='用户体重记录三', null=True)
    three_time = models.DateField(verbose_name='用户体重记录三的时间', null=True)
    weight_four = models.FloatField(verbose_name='用户体重记录四', null=True)
    four_time = models.DateField(verbose_name='用户体重记录四的时间', null=True)
    weight_five = models.FloatField(verbose_name='用户体重记录五', null=True)
    five_time = models.DateField(verbose_name='用户体重记录五的时间', null=True)

    class Meta:
        verbose_name = '用户体重笔记表'
        verbose_name_plural = verbose_name


class UserSearchHistory(models.Model):
    """用户的搜索历史"""
    user = models.ForeignKey(to=Userinfo, to_field="open_id", on_delete=models.CASCADE, verbose_name='用户唯一标识符')
    search_one = models.CharField(max_length=50, verbose_name='用户搜索历史一', null=True)
    search_two = models.CharField(max_length=50, verbose_name='用户搜索历史二', null=True)
    search_three = models.CharField(max_length=50, verbose_name='用户搜索历史三', null=True)

    class Meta:
        verbose_name = '用户搜索记录表'
        verbose_name_plural = verbose_name


class UserSportNotes(models.Model):
    """用户的卡路里日记"""
    user = models.ForeignKey(to=Userinfo, to_field="open_id", on_delete=models.CASCADE, verbose_name='用户唯一标识符')
    sport_consumed = models.FloatField(verbose_name='用户当天累计消耗卡路里', default=0)
    sport_time = models.FloatField(verbose_name='用户当天累计运动时间', default=0)
    sport_target = models.FloatField(verbose_name='用户运动目标', default=0)
    sport_consume = models.FloatField(verbose_name='每日待消耗热量', default=0)
    sport_residualheat = models.FloatField(verbose_name='当天摄入的卡路里', default=0)

    class Meta:
        verbose_name = '用户卡路里日记表'
        verbose_name_plural = verbose_name
