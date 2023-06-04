# 26. Write a pandas program to compute diffreenc eof difference between consecutive numbers of a given series

import pandas as pd

s = pd.Series(range(1,16,2))
print(s)

r = s.diff().tolist()
print(r)