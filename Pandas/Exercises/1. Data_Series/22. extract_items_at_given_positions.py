# 22. Write a pandas program to extract items at given positions of a given series

import pandas as pd

s = pd.Series(list('2390238923902390239023'))
print(s)

positions = [0,2,6,11,21]
r = s.take(positions)
print(""+r)