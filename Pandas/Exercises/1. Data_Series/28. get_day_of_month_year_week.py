# 28. Write a pandas program to get the day of month, day of yeyar, week number and day of week from given series of date strings

import pandas as pd

l = ['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20']
s = pd.Series(l)
print(s)
# s = s.map(lambda x:parse(x))
s = pd.to_datetime(s)

print(s)
print("Day of Month:\n{}".format(s.dt.day.tolist()))
print("Day of year:\n{}".format(s.dt.dayofyear.tolist()))
print("Week number:\n{}".format(s.dt.weekofyear.tolist()))
print("Day of Week:\n{}".format(s.dt.day_name().tolist()))