# 39. Wriote a pandas program to combining two series into a datarame

import pandas as pd

s1 = [1,2,3,4,5]
s2 = [6,7,8,9,10]

s1 = pd.Series(s1)
s2 = pd.Series(s2)

print(s1)
print(s2)

df = pd.concat([s1,s2],axis=1)
print(df)
