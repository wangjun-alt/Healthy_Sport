from django.db import models

# Create your models here.


class SportRun(models.Model):
    """跑步表"""
    user = models.ForeignKey(to='User.Userinfo', to_field="open_id", on_delete=models.CASCADE, verbose_name='用户唯一标识符')
    run_time = models.FloatField(verbose_name='运动时长', default=0)
    run_distance = models.FloatField(verbose_name='运动累计距离', default=0)
    run_calorie = models.FloatField(verbose_name='运动累计消耗', default=0)
    sport_mark = models.BooleanField(verbose_name='运动标记', default=False)

    def __str__(self):
        user = str(self.user)
        return user

    class Meta:
        verbose_name = '跑步信息表'
        verbose_name_plural = verbose_name


class SportSwim(models.Model):
    """游泳表"""
    user = models.ForeignKey(to='User.Userinfo', to_field="open_id", on_delete=models.CASCADE, verbose_name='用户唯一标识符')
    swim_time = models.FloatField(verbose_name='运动时长', default=0)
    swim_calorie = models.FloatField(verbose_name='运动累计消耗', default=0)
    sport_mark = models.BooleanField(verbose_name='运动标记', default=False)


    def __str__(self):
        return self.user

    class Meta:
        verbose_name = '游泳信息表'
        verbose_name_plural = verbose_name


class SportCycling(models.Model):
    """骑单车表"""
    user = models.ForeignKey(to='User.Userinfo', to_field="open_id", on_delete=models.CASCADE, verbose_name='用户唯一标识符')
    cycling_time = models.FloatField(verbose_name='运动时长', default=0)
    cycling_calorie = models.FloatField(verbose_name='运动累计消耗', default=0)
    sport_mark = models.BooleanField(verbose_name='运动标记', default=False)


    def __str__(self):
        return self.user

    class Meta:
        verbose_name = '骑单车信息表'
        verbose_name_plural = verbose_name


class SportFootball(models.Model):
    """足球表"""
    user = models.ForeignKey(to='User.Userinfo', to_field="open_id", on_delete=models.CASCADE, verbose_name='用户唯一标识符')
    football_time = models.FloatField(verbose_name='运动时长', default=0)
    football_calorie = models.FloatField(verbose_name='运动累计消耗', default=0)
    sport_mark = models.BooleanField(verbose_name='运动标记', default=False)


    def __str__(self):
        return self.user

    class Meta:
        verbose_name = '骑单车信息表'
        verbose_name_plural = verbose_name


class SportImg(models.Model):
    """运动图片表"""
    sportname = models.CharField(max_length=50, verbose_name="运动名称", unique=True)
    img_url = models.CharField(verbose_name='图片地址', max_length=200)

    def __str__(self):
        return self.sportname

    class Meta:
        verbose_name = '运动图片表'
        verbose_name_plural = verbose_name
