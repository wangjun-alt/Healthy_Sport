import json
import os
import datetime
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from Healthy_Sport.settings import BASE_DIR
from User.models import *
from Sport.models import *
from module.time.time_tmp import time_tmp
from module.userinfo.calculateinfo import *
# Create your views here.

class RunView(APIView):
    def post(self, request):
        """
            跑步的运动计算统计
            :return: response [fail or succees]
            response = {"code":200 "status": "fail", "errMsg": "", "data": ""}
        """
        response = {"code": 200, "status": "fail", "errMsg": "", "data": ""}
        result = request.user
        openid = result.get('username')
        body = json.loads(request.body)
        run_time = body.get('runtime')
        print(run_time)
        run_time = time_tmp(run_time)
        print(run_time)
        run_distance = body.get('distance')
        run = SportRun.objects.get(user=openid)
        user = Userinfo.objects.get(open_id=openid)
        run_calorie = get_run(user.weight, run_time, run_distance)
        run.run_calorie = run.run_calorie + run_calorie
        run.run_time = run.run_time + run_time
        run.sport_mark = True
        run.save()
        run = SportRun.objects.get(user=openid)
        sport = UserSportNotes.objects.get(user=openid)
        sport.sport_consumed = sport.sport_consumed + run.run_calorie
        sport.sport_time = sport.sport_time + run.run_time
        response["status"] = "success"
        response["data"] = {
            "runtime": run_time,
            "calorie": run_calorie
        }
        return Response(data=response)



class SwimView(APIView):
    def post(self, request):
        """
            游泳的运动计算统计
            :return: response [fail or succees]
            response = {"code":200 "status": "fail", "errMsg": "", "data": ""}
        """
        response = {"code": 200, "status": "fail", "errMsg": "", "data": ""}
        result = request.user
        openid = result.get('username')
        body = json.loads(request.body)
        swim_time = body.get('swimtime')
        swim = SportSwim.objects.get(user=openid)
        user = Userinfo.objects.get(open_id=openid)
        swim_calorie = get_swim(user.gender, swim_time)
        swim.swim_calorie = swim.swim_calorie + swim_calorie
        swim.swim_time = swim.swim_time + swim_time
        swim.sport_mark = True
        swim.save()
        response["status"] = "success"
        response["data"] = {
            "swimtime": swim_time,
            "calorie": swim_calorie
        }
        return Response(data=response)


class CyclingView(APIView):
    def post(self, request):
        """
            骑单车的运动计算统计
            :return: response [fail or succees]
            response = {"code":200 "status": "fail", "errMsg": "", "data": ""}
        """
        response = {"code": 200, "status": "fail", "errMsg": "", "data": ""}
        result = request.user
        openid = result.get('username')
        body = json.loads(request.body)
        cycling_time = body.get('cyclingtime')
        cycling = SportCycling.objects.get(user=openid)
        user = Userinfo.objects.get(open_id=openid)
        cycling_calorie = get_cycling(cycling_time)
        cycling.cycling_calorie = cycling.cycling_calorie + cycling_calorie
        cycling.cycling_time = cycling.swim_time + cycling_time
        cycling.sport_mark = True
        cycling.save()
        response["status"] = "success"
        response["data"] = {
            "cyclingtime": cycling_time,
            "calorie": cycling_calorie
        }
        return Response(data=response)


class FootballView(APIView):
    def post(self, request):
        """
            游泳的运动计算统计
            :return: response [fail or succees]
            response = {"code":200 "status": "fail", "errMsg": "", "data": ""}
        """
        response = {"code": 200, "status": "fail", "errMsg": "", "data": ""}
        result = request.user
        openid = result.get('username')
        body = json.loads(request.body)
        football_time = body.get('footballtime')
        football = SportFootball.objects.get(user=openid)
        user = Userinfo.objects.get(open_id=openid)
        football_calorie = get_football(football_time)
        football.football_calorie = football.football_calorie + football_calorie
        football.football_time = football.football_time + football_time
        football.sport_mark = True
        football.save()
        response["status"] = "success"
        response["data"] = {
            "footballtime": football_time,
            "calorie": football_calorie
        }
        return Response(data=response)