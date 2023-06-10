# 62. Write a pandas program to rmeove first n rows of a given dataframe

import pandas as pd
import numpy as np

values = np.random.randint(0,10,(6,3))
col = ['col1','col2','col3']
df = pd.DataFrame(values, columns=col)
print(df)

df1 = df.drop(index=list(range(0,3)))
print(df1)

print(df.iloc[3:])