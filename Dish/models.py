from django.db import models

# Create your models here.


class HealthKnowledge(models.Model):
    """健康科普知识"""
    text_id = models.IntegerField(verbose_name="文章ID")
    title = models.CharField(verbose_name='知识标题', max_length=100)
    health_text = models.TextField(verbose_name='知识科普内容')

    def __str__(self):
        return self.title

class Dishinfo(models.Model):
    """菜品信息表"""
    dish_name = models.CharField(max_length=20, verbose_name='菜品名称')
    dish_heat = models.FloatField(verbose_name='热量')  # 热量
    dish_carbohydrate = models.FloatField(verbose_name='碳水化合物含量', null=True)  # 碳水化合物含量
    dish_protein = models.FloatField(verbose_name='蛋白质含量', null=True)  # 蛋白质含量
    dish_fat = models.FloatField(verbose_name='脂肪含量', null=True)  # 脂肪含量
    dish_cholesterol = models.FloatField(verbose_name='胆固醇含量', null=True)  # 胆固醇含量
    dish_mineral = models.FloatField(verbose_name='矿物质含量', null=True)  # 矿物质含量
    dish_carotene = models.FloatField(verbose_name='胡萝卜素含量', null=True)  # 胡萝卜素含量
    dish_vitamin_A = models.FloatField(verbose_name='维生素A含量', null=True)  # 维生素A含量
    dish_vitamin_C = models.FloatField(verbose_name='维生素C含量', null=True)  # 维生素C含量
    dish_vitamin_E = models.FloatField(verbose_name='维生素E含量', null=True)  # 维生素E含量
    dish_vitamin_B1 = models.FloatField(verbose_name='维生素B1含量', null=True)  # 维生素B1含量
    dish_vitamin_B2 = models.FloatField(verbose_name='维生素B2含量', null=True, unique=False)  # 维生素B2含量
    dish_dietary = models.FloatField(verbose_name='膳食纤维', null=True, unique=False)  # 膳食纤维
    # img_url = models.CharField(max_length=100, verbose_name='菜品图片', null=True)  # 菜品图片

    def __str__(self):
        return self.dish_name

    class Meta:
        verbose_name = '菜品基本信息'
        verbose_name_plural = verbose_name


class Carousel(models.Model):
    """轮播图"""
    number = models.IntegerField(verbose_name='编号', help_text='编号决定图片播放的顺序，图片不要多于5张')
    img_url = models.CharField(verbose_name='图片地址', max_length=200)

    class Meta:
        verbose_name = '图片轮播'
        verbose_name_plural = verbose_name
