# 31. Write a pandas program to select a row of series/dataframe by given integer index

import pandas as pd
import numpy as np

data = np.random.randint(low = 0, high = 10, size = (5,3))
col = ['col1','col2','col3']
df = pd.DataFrame(data=data, columns = col)
print(df)
print("Getting Index 2")
print(df.iloc[2,:])
print(df.loc[[2]])