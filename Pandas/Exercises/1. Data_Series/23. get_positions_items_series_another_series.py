# 23. Write a pandas program to get the positions of items of a given series in another given series

import pandas as pd

s1 = pd.Series(list(range(1,11)))
print(s1)

s2 = pd.Series(list(range(1,11,2)))
print(s2)


result = [pd.Index(s1).get_loc(i) for i in s2]
print(result)