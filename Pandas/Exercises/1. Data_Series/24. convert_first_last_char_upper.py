# 24. Write a pandas program to convert the first and last char of each word to upper case in aeach word of a given series.

import pandas as pd

s = pd.Series(["php","python","java","c#"])
print(s)
r = s.map(lambda x:x[0].upper()+x[1:-1]+x[-1].upper())
print(r)