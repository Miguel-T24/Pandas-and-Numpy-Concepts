# 53. Write a pandas program to insert a given column at a specific column index in a dataframe

import pandas as pd
import numpy as np

values = np.random.randint(0,10,(5,2))
col = ['col1','col2']

df = pd.DataFrame(values, columns=col)
print(df)

s3 = pd.Series(list(range(1,6)))
print(s3)
s4 = pd.Series(list(range(1,6)))
print(s4)

df['col3'] = s3

print(df)

df.insert(loc=0,column='col0',value=[1,2,3,4,5])
print(df)
