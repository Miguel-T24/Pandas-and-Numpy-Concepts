# 72. Write a pandas program to combine many giuven series to crate a dataframe

import pandas as pd

s1 = pd.Series(['php','python','java','c#','c++'])
s2 = pd.Series(range(1,6))

print("s1:\n{}".format(s1))
print("s2:\n{}".format(s2))

df = pd.DataFrame(data = s1,columns=['col1'])
print(df)
df['col2'] = s2
print(df)

print("\n\n")
ds1 = pd.DataFrame(s1,columns=['col1'])
print(ds1)
ds2 = pd.DataFrame(s2,columns=['col2'])
print(ds2)

df1 = pd.concat([ds1,ds2],axis = 1)
print("\n\n\n{}".format(df1))