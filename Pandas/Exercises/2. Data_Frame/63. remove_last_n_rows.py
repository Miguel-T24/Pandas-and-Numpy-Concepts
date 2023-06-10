# 63. write a pandas program to remove last n rows of a given datafanme


import pandas as pd
import numpy as np

values = np.random.randint(0,10,(6,3))
col = ['col1','col2','col3']

df = pd.DataFrame(values, columns=col)
print(df)

print(df.iloc[:3])