# 35. Write a pandas program to crate a timeseries to display all the sundays if given year

import pandas as pd

result = pd.Series(pd.date_range('2020-01-01', periods=52, freq='W-SUN'))
print("All Sundays of 2020:")

print(result)