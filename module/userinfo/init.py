from User.models import *
from Sport.models import *


def userinit(openid):
    user = Userinfo.objects.get(open_id=openid)
    if user:
        user_sport = UserSportNotes.objects.create(user=user)
        user_feed = Feedback.objects.create(user=user)
        user_weights = UserWeights.objects.create(user=user)
        user_search = UserSearchHistory.objects.create(user=user)
        sport_run = SportRun.objects.create(user=user)
        sport_swim = SportSwim.objects.create(user=user)
        sport_cycling = SportCycling.objects.create(user=user)
        sport_football = SportFootball.objects.create(user=user)
        return True
    return False


def userrecover(openid):
    user_sport = UserSportNotes.objects.get(user=openid)
    user_sport.sport_consumed = 0
    user_sport.sport_consume = 500
    user_sport.sport_time = 0
    user_sport.sport_residualheat = 0
    user_sport.save()
    sport_run = SportRun.objects.get(user=openid)
    if sport_run.sport_mark is True:
        sport_run.run_time = 0
        sport_run.run_calorie = 0
        sport_run.run_distance = 0
        sport_run.sport_mark = False
    sport_swim = SportSwim.objects.get(user=openid)
    if sport_swim.sport_mark is True:
        sport_swim.swim_time = 0
        sport_swim.swim_calorie = 0
        sport_swim.sport_mark = False
    sport_cycle = SportCycling.objects.get(user=openid)
    if sport_cycle.sport_mark is True:
        sport_cycle.cycling_time = 0
        sport_cycle.cycling_calorie = 0
        sport_cycle.sport_mark = False
    sport_football = SportFootball.objects.get(user=openid)
    if sport_football.sport_mark is True:
        sport_football.football_calorie = 0
        sport_football.football_time = 0
        sport_football.sport_mark = False
    return True