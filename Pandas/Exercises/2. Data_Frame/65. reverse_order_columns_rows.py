# 65. Write a pandas program to revrse order (rows, columns) of a given Dataframe

import pandas as pd
import numpy as np

values = np.random.randint(0,10,(5,3))
col = ['col1','col2','col3']

df = pd.DataFrame(values, columns=col)
print(df)

print(df[df.columns[::-1]])
print(df.iloc[::-1])