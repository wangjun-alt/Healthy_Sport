import json
import os
import datetime
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from Healthy_Sport.settings import BASE_DIR
from User.models import *
from Sport.models import *
from module.userinfo.init import userinit, userrecover
from module.utils.jwt_auth import create_token
from module.userinfo.calculateinfo import *
# Create your views here.


class LoginView(APIView):
    authentication_classes = []

    def post(self, request):
        """
            拿用户openid，微信小程序登录
            :return: response [fail or succees]
            response = {"code":200 "status": "fail", "errMsg": "", "data": ""}
        """
        response = {"code": 200, "status": "fail", "errMsg": "", "data": ""}
        body = json.loads(request.body)
        nickname = body.get("nickname")
        code = body.get("code")
        reqUrl = "https://api.weixin.qq.com/sns/jscode2session?appid=wx3f5e22ca87e81851&secret" \
                 "=088f6189c32f941f4061bf670cf5232e&js_code=" + code + "&grant_type=authorization_code "
        identityInfo = requests.get(reqUrl).json()  # 向微信接口申请openId
        openid = identityInfo['openid'] if 'openid' in identityInfo else None
        if not openid:
            response["code"] = 400
            response["errMsg"] = "微信调用失败"
            return Response(data=response)
        try:
            user = Userinfo.objects.get(open_id=openid)
        except Userinfo.DoesNotExist:
            user = None
        if user == None:  # 用户是新用户，直接创建该文件目录
            user = Userinfo.objects.create(open_id=openid)
            user.username = nickname
            user.save()
            file_path = os.path.join(BASE_DIR, 'media', '%s' % openid)
            token = create_token({'username': user.open_id})
            os.mkdir(file_path)
            init = userinit(openid)
            if init is True:
                response["status"] = "succeed"
            response["data"] = {
                "user": '新用户',
                "token": token
            }
            local_time = datetime.date.today()
            user.last_time = local_time
            user.save()
            return Response(data=response)
        elif user.age is None:
            token = create_token({'username': user.open_id})
            response["status"] = "success"
            response["data"] = {
                "user": '新用户',
                "token": token,
            }
            local_time = datetime.date.today()
            user.last_time = local_time
            user.save()
            return Response(data=response)
        user.username = nickname
        print(user.username)
        user.age = get_userage(user.brontime)
        user.save()
        local_time = datetime.date.today()
        time = local_time - user.last_time
        if time.days > 0:
            userrecover(openid)
        token = create_token({'username': user.open_id})
        response["status"] = "success"
        response["data"] = {
            "user": '老用户',
            "token": token
        }
        return Response(data=response)


class SaveView(APIView):
    def post(self, request):
        """
            新用户保存用户相关信息
            :return: response [fail or succees]
            response = {"code":200 "status": "fail", "errMsg": "", "data": ""}
        """
        response = {"code": 200, "status": "fail", "errMsg": "", "data": ""}
        result = request.user
        openid = result.get('username')
        user = Userinfo.objects.get(open_id=openid)
        body = json.loads(request.body)
        gender = body.get('gender')
        if gender == "1":
            user.gender = True
        else:user.gender = False
        brontime = body.get('borntime')
        print(brontime)
        print(type(brontime))
        user.brontime = str_date(brontime)
        height = body.get('height')
        weight = body.get('weight')
        print(weight)
        print(height)
        user.weight = float(weight)
        user.height = float(height)
        user.age = get_userage(user.brontime)
        user_weight = UserWeights.objects.get(user=user)
        user_weight.weight_one = user.weight
        local_time = datetime.date.today()
        user_weight.one_time = local_time
        user.BMI = get_bmi(user.weight, user.height)
        user.bodyfat_rate = get_bodyfatrate(user.gender, user.BMI, user.age)
        user.metabolism = get_metabolism(user.gender, user.weight, user.height, user.age)
        user.save()
        user_weight.save()
        response["status"] = "success"
        response["data"] = "保存成功"
        return Response(data=response)


class WightView(APIView):
    def get(self, request):
        """
            获取用户体重日记信息
            :return: response [fail or succees]
            response = {"code":200 "status": "fail", "errMsg": "", "data": ""}
        """
        response = {"code": 200, "status": "fail", "errMsg": "", "data": ""}
        result = request.user
        openid = result.get('username')
        val = UserWeights.objects.get(user=openid)
        if val.weight_five:
            response["data"] = [{'weight':val.weight_one, 'time':val.one_time},
                                {'weight':val.weight_two, 'time':val.two_time},
                                {'weight':val.weight_three, 'time':val.three_time},
                                {'weight':val.weight_four, 'time':val.four_time},
                                {'weight':val.weight_five, 'time':val.five_time}
                                ]
        elif val.weight_four:
            response["data"] = [{'weight': val.weight_one, 'time': val.one_time},
                                {'weight': val.weight_two, 'time': val.two_time},
                                {'weight': val.weight_three, 'time': val.three_time},
                                {'weight': val.weight_four, 'time': val.four_time}
                                ]
        elif val.weight_three:
            response["data"] = [{'weight': val.weight_one, 'time': val.one_time},
                                {'weight': val.weight_two, 'time': val.two_time},
                                {'weight': val.weight_three, 'time': val.three_time}
                                ]
        elif val.weight_two:
            response["data"] = [{'weight': val.weight_one, 'time': val.one_time},
                                {'weight': val.weight_two, 'time': val.two_time}
                                ]
        elif val.weight_one:
            response["data"] = [{'weight': val.weight_one, 'time': val.one_time}
                                    ]
        response["status"] = "success"
        return Response(data=response)


class SportView(APIView):
    def get(self, request):
        """
            运动计划的信息获取
            :return: response [fail or succees]
            response = {"code":200 "status": "fail", "errMsg": "", "data": ""}
        """
        response = {"code": 200, "status": "fail", "errMsg": "", "data": ""}
        result = request.user
        openid = result.get('username')
        user = Userinfo.objects.get(open_id=openid)
        sport = UserSportNotes.objects.get(user=openid)
        if user.gender:
            sport.sport_consume = int(user.weight) + 500
        else:
            sport.sport_consume = int(user.weight) + 400
        # run = SportRun.objects.get(user=openid)
        # swim = SportSwim.objects.get(user=openid)
        # cycling = SportCycling.objects.get(user=openid)
        # football = SportFootball.objects.get(user=openid)
        # if run.sport_mark:
        #     sport.sport_consumed = sport.sport_consumed + run.run_calorie
        #     sport.sport_time = sport.sport_time + run.run_time
        # if swim.sport_mark:
        #     sport.sport_consumed = sport.sport_consumed + swim.swim_calorie
        #     sport.sport_time = sport.sport_time + swim.swim_time
        # if cycling.sport_mark:
        #     sport.sport_consumed = sport.sport_consumed + cycling.cycling_calorie
        #     sport.sport_time = sport.sport_time + cycling.cycling_time
        # if football.sport_mark:
        #     sport.sport_consumed = sport.sport_consumed + football.football_calorie
        #     sport.sport_time = sport.sport_time + football.football_time
        sport.save()
        response["status"] = "success"
        response["data"] = {
            "sport_consume": sport.sport_consume,
            "sport_time": sport.sport_time,
            "sport_consumed": sport.sport_consumed,
            "sport_residualheat": sport.sport_residualheat
        }
        return Response(data=response)


class FeedView(APIView):
    def post(self,request):
        """
            保存用户的反馈与建议
            :return: response [fail or succees]
            response = {"code":200 "status": "fail", "errMsg": "", "data": ""}
        """
        response = {"code": 200, "status": "fail", "errMsg": "", "data": ""}
        result = request.user
        openid = result.get('username')
        body = json.loads(request.body)
        feedtext = body.get('feedtext')
        user = Userinfo.objects.get(open_id=openid)
        feed = Feedback.objects.create(user=user, feed_text=feedtext)
        response["status"] = "success"
        response["data"] = "反馈成功"
        return Response(data=response)


class InfoView(APIView):
    def get(self, request):
        """
            获取用户信息
            :return: response [fail or succees]
            response = {"code":200 "status": "fail", "errMsg": "", "data": ""}
        """
        response = {"code": 200, "status": "fail", "errMsg": "", "data": ""}
        result = request.user
        openid = result.get('username')
        user = Userinfo.objects.get(open_id=openid)
        response["status"] = "success"
        response["data"] = {
            "nickname": user.username,
            "biography": user.biography,
            "gender": user.gender,
            "height": user.height,
            "weight": user.weight,
            "BMI": user.BMI,
            "bodyfat_rate": user.bodyfat_rate,
            "metabolism": user.metabolism
        }
        return Response(data=response)



    def put(self, request):
        """
            修改用户信息
            :return: response [fail or succees]
            response = {"code":200 "status": "fail", "errMsg": "", "data": ""}
        """
        response = {"code": 200, "status": "fail", "errMsg": "", "data": ""}
        result = request.user
        openid = result.get('username')
        body = json.loads(request.body)
        user = Userinfo.objects.get(open_id=openid)
        user.biography = body.get('biography')
        user.height = float(body.get('height'))
        user.weight = float(body.get('weight'))
        user.BMI = get_bmi(user.weight, user.height)
        user.bodyfat_rate = get_bodyfatrate(user.gender, user.BMI, user.age)
        user.metabolism = get_metabolism(user.gender, user.weight, user.height, user.age)
        user.save()
        weights = UserWeights.objects.get(user=openid)
        local_time = datetime.date.today()
        if weights.weight_five:
            weights.weight_one = weights.weight_two
            weights.one_time = weights.two_time
            weights.weight_two = weights.weight_three
            weights.two_time = weights.three_time
            weights.weight_three = weights.weight_four
            weights.three_time = weights.four_time
            weights.weight_four = weights.weight_five
            weights.four_time = weights.five_time
            weights.weight_five = user.weight
            weights.five_time = local_time
            weights.save()
            response["status"] = "success"
            response["data"] = "修改成功"
            return Response(data=response)
        if weights.weight_four:
            weights.weight_five = user.weight
            weights.five_time = local_time
            weights.save()
            response["status"] = "success"
            response["data"] = "修改成功"
            return Response(data=response)
        if weights.weight_three:
            weights.weight_four = user.weight
            weights.four_time = local_time
            weights.save()
            response["status"] = "success"
            response["data"] = "修改成功"
            return Response(data=response)
        if weights.weight_two:
            weights.weight_three = user.weight
            weights.three_time = local_time
            weights.save()
            response["status"] = "success"
            response["data"] = "修改成功"
            return Response(data=response)
        if weights.weight_one:
            weights.weight_two = user.weight
            weights.two_time = local_time
            weights.save()
            response["status"] = "success"
            response["data"] = "修改成功"
            return Response(data=response)



class SportItemsView(APIView):
    def get(self, request):
        """
            运动项目信息获取
            :return: response [fail or succees]
            response = {"code":200 "status": "fail", "errMsg": "", "data": ""}
        """
        response = {"code": 200, "status": "fail", "errMsg": "", "data": ""}
        result = request.user
        openid = result.get('username')
        run = SportRun.objects.get(user=openid)
        swim = SportSwim.objects.get(user=openid)
        cycling = SportCycling.objects.get(user=openid)
        football = SportFootball.objects.get(user=openid)
        li = []
        if run.sport_mark:
            li.append("跑步")
        if swim.sport_mark:
            li.append("游泳")
        if cycling.sport_mark:
            li.append("骑单车")
        if football.sport_mark:
            li.append("踢足球")
        response["status"] = "success"
        if not li:
            response["data"] = "今天还没有运动！"
            return Response(data=response)
        response["data"] = li
        return Response(data=response)