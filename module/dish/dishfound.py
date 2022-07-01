from aip import AipImageClassify
from Dish.models import *
from User.models import *


def dishfound(file_path, file_obj, dish_weight, openid, response):
    """ 你的 APPID AK SK """
    APP_ID = '24772730'
    API_KEY = 'SAx4BEE5KNjy5C70coBGjttw'
    SECRET_KEY = 'TjMHiD58XlxfxlKX512FYqf8eDsibnmG'
    client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
    with open(file_path, 'wb') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)
    with open(file_path, 'rb') as fp:
        image = fp.read()

    """ 调用菜品识别 """
    # result = (client.dishDetect(image))

    """ 如果有可选参数 """
    options = {}
    options["top_num"] = 10
    options["filter_threshold"] = "0.7"
    options["baike_num"] = 1
    """ 带参数调用菜品识别 """
    result = client.dishDetect(image, options)
    result = result.get("result")
    result = result[0]
    print(result)
    logo = result.get('has_calorie')
    data = {}
    print(dish_weight)
    dish_weight = float(dish_weight) / 100
    if logo is True:
        calorie = result.get('calorie')  # 每一百克所包含的食物卡路里
        dish_name = result.get('name')
        print(dish_name)
        try:
            dishinfo = Dishinfo.objects.filter(dish_name=dish_name).first()
        except Dishinfo.DoesNotExist:
            dishinfo = None
        if dishinfo:
            if dishinfo.dish_mineral:
                dishinfo.dish_heat = calorie
                dish_heated = int(dishinfo.dish_heat) * int(dish_weight)
                user = UserSportNotes.objects.get(user=openid)
                user.sport_consume = user.sport_consume + dish_heated
                user.save()
                data = {
                    "dish_heated": dish_heated,
                    "dish_name": dishinfo.dish_name,
                    "dish_heat": dishinfo.dish_heat,
                    "dish_fat": dishinfo.dish_fat,
                    "dish_protein": dishinfo.dish_protein,
                    "dish_dietary": dishinfo.dish_dietary,
                    "dish_cholesterol": dishinfo.dish_cholesterol,
                    "dish_carbohydrate": dishinfo.dish_carbohydrate,
                    "dish_mineral": dishinfo.dish_mineral,
                    "dish_vitamin_A": dishinfo.dish_vitamin_A
                }
            else:
                dish_heated = int(dishinfo.dish_heat) * int(dish_weight)
                user = UserSportNotes.objects.get(user=openid)
                user.sport_consume = user.sport_consume + dish_heated
                user.save()
                data = {
                    "dish_heated": dish_heated,
                    "dish_name": dishinfo.dish_name,
                    "dish_heat": dishinfo.dish_heat,
                    "dish_fat": "敬请期待",
                    "dish_protein": "敬请期待",
                    "dish_dietary": "敬请期待",
                    "dish_cholesterol": "敬请期待",
                    "dish_carbohydrate":"敬请期待",
                    "dish_mineral": "敬请期待",
                    "dish_vitamin_A": "敬请期待"
                }
        else:
            dish = Dishinfo.objects.create(
                dish_name=dish_name,
                dish_heat=calorie,
            )
            dish_heated = int(dish.dish_heat) * int(dish_weight)
            user = UserSportNotes.objects.get(user=openid)
            user.sport_consume = user.sport_consume + dish_heated
            user.save()
            data = {
                "dish_heated": dish_heated,
                "dish_name": dish.dish_name,
                "dish_heat": dish.dish_heat,
                "dish_fat": "敬请期待",
                "dish_protein": "敬请期待",
                "dish_dietary": "敬请期待",
                "dish_cholesterol": "敬请期待",
                "dish_carbohydrate": "敬请期待",
                "dish_mineral": "敬请期待",
                "dish_vitamin_A": "敬请期待"
            }

    return data
