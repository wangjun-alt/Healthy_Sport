import datetime


# 字符串转换为日期
def str_date(born_time):
    born_time = datetime.date(*map(int, born_time.split('-')))
    return born_time


# 计算用户年龄
def get_userage(brontime):
    local_time = datetime.date.today()
    time = local_time - brontime
    if time.days <= 0:
        return False
    if local_time.year - brontime.year > 0 and local_time.month - brontime.month > 0 \
            and local_time.day - brontime.day > 0:
        age = local_time.year - brontime.year
        return age
    elif local_time.year - brontime.year > 0 and local_time.month - brontime.month < 0:
        age = local_time.year - brontime.year - 1
        return age
    elif local_time.year - brontime.year > 0 and local_time.month - brontime.month > 0 \
            and local_time.day - brontime.day < 0:
        age = local_time.year - brontime.year - 1
        return age


# 计算BMI
def get_bmi(weight, height):
    BMI = float(weight) / (float(height) * float(height))
    return BMI


# 计算体脂率
def get_bodyfatrate(gender, BMI, age):
    if gender:
        bodyfat_rate = ((1.2 * BMI) + (0.23 * age) - 5.4 - (10.8 * 1)) / 100
        return bodyfat_rate
    bodyfat_rate = ((1.2 * BMI) + (0.23 * age) - 5.4 - (10.8 * 0)) / 100
    return bodyfat_rate


# 计算用户每日的基础代谢
def get_metabolism(gender, weight, height, age):
    if gender:
        metabolism = 66 + (13.7 * weight) + (5.0 * height) - (6.8 * age)
        return metabolism
    metabolism = 665 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    return metabolism


# 计算跑步的运动消耗
def get_run(weight, run_time, run_distance):
    run_Calorie = weight * run_time * (30 / (run_time / (float(run_distance) / 400)))
    return run_Calorie


# 计算游泳的运动消耗
def get_swim(gender, swim_time):
    if gender:
        swim_calorie = swim_time / 60 * 843
    else:
        swim_calorie = swim_time / 60 * 600
    return swim_calorie


# 计算骑单车的运动消耗
def get_cycling(cycling_time):
    cycling_calorie = cycling_time / 60 * 480
    return cycling_calorie


# 计算踢足球的运动消耗
def get_football(football_time):
    football_calorie = football_time / 60 * 450
    return football_calorie