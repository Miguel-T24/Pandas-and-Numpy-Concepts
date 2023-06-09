# 47. Write a pandas program to get the specified row value of a given dataframe

import pandas as pd
import numpy as np

values=np.random.randint(0,50,(5,3))
columns = ['col1','col2','col3']

df = pd.DataFrame(values,columns=columns)

print(df)

print(df.iloc[0])
