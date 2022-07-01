
def time_tmp(run_time):
    minute = run_time.split(".")[0]
    second = run_time.split(".")[1]
    if second[0] == 0:
        second = int(second[1])
        print(second)
        minute = int(minute) + (second / 60)
        return minute
    second = int(second)
    print(second)
    minute = int(minute) + (second / 60)
    return minute