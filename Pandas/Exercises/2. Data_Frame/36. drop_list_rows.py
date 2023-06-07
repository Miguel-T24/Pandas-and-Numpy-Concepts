# 36. Write a pandas program to drop a list of rows from specified Dataframe

import pandas as pd
import numpy as np

data = np.random.randint(0, 10,(5,3))
col = ['col1','col2','col3']

df = pd.DataFrame(data=data,columns=col)

print(df)

df = df.drop(index=[2,4])
print(df)