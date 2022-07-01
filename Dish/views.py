# -- coding: utf-8 --**
import os
from django.shortcuts import render
from Dish.models import *
import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from Healthy_Sport.settings import BASE_DIR
from User.models import *
from Sport.models import *

# Create your views here.
from module.dish.dishfound import dishfound


class SearchView(APIView):
    def post(self, request):
        """
            菜品信息的查询
            :return: response [fail or succees]
            response = {"code":200 "status": "fail", "errMsg": "", "data": ""}
        """
        response = {"code": 200, "status": "fail", "errMsg": "", "data": ""}
        print(request.body)
        body = json.loads(request.body)
        print(body)
        dish_name = body.get("dishname")
        print(dish_name)
        try:
            dishinfo = Dishinfo.objects.get(dish_name=dish_name)
        except Dishinfo.DoesNotExist:
            dishinfo = None
        if dishinfo is None:
            response["status"] = "success"
            response["data"] = {
            "dish_name": dish_name,
            "dish_heat": "敬请期待",
            "dish_fat": "敬请期待",
            "dish_protein": "敬请期待",
            "dish_dietary": "敬请期待",
            "dish_cholesterol": "敬请期待",
            "dish_carbohydrate": "敬请期待",
            "dish_mineral": "敬请期待",
            "dish_vitamin_A": "敬请期待"
        }
            return Response(data=response)
        response["status"] = "success"
        response["data"] = {
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
        return Response(data=response)


class KnowledgeView(APIView):
    def get(self, request):
        """
            菜品信息的查询
            :return: response [fail or succees]
            response = {"code":200 "status": "fail", "errMsg": "", "data": ""}
        """
        response = {"code": 200, "status": "fail", "errMsg": "", "data": ""}
        try:
            healthtexts = HealthKnowledge.objects.all()
        except HealthKnowledge.DoesNotExist:
            healthtexts = None
        if healthtexts is None:
            response["status"] = "success"
            response["data"] = "目前还没有健康科普哦，敬请期待！"
        li = []
        for healthtext in healthtexts:
            li.append(healthtext)
        response["status"] = "success"
        response["data"] = li
        return Response(data=response)


class DishfoundView(APIView):
    def post(self, request):
        """
            菜品识别并计算卡路里
            :return: response [fail or succees]
            response = {"code":200 "status": "fail", "errMsg": "", "data": ""}
        """
        response = {"code": 200, "status": "fail", "errMsg": "", "data": ""}
        result = request.user
        openid = result.get('username')
        dish_weight = request.headers.get('dishweight')
        file_obj = request.FILES.get('file', None)
        file_path = os.path.join(BASE_DIR, 'media', '%s' % openid, file_obj.name)
        print(dish_weight)
        data = dishfound(file_path, file_obj, dish_weight, openid, response)
        response["status"] = "success"
        response["data"] = data
        return Response(data=response)
