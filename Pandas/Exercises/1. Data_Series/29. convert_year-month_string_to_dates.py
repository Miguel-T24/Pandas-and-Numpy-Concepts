# 29. Write a pandas program to conbvert year-month string to dates adding a specified day of thhe month

import pandas as pd

l = ['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019']
s = pd.Series(l)
print(s)

s = s.map(lambda x:x+"-11")
s = pd.to_datetime(s)
print(s)