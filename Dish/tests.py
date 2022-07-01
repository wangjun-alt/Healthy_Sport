from django.test import TestCase
# Create your tests here.

import datetime
born_time = '2001-06-01'


def str_date(born_time):
    born_time = datetime.date(*map(int, born_time.split('-')))
    return born_time


time = str_date(born_time)
print(time)
local_time = datetime.date.today()
print(local_time)
print(type(time))
result = local_time.year - time.year - 1








