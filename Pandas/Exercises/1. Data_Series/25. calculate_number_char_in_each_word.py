# 25. Write a python program to calculate the number of characters in each word in a given series

import pandas as pd

s = pd.Series(["php","python","java","c#"])
print(s)
s1 = s.map(lambda x:len(x))
print(s1)
