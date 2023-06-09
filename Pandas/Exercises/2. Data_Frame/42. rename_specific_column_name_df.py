# 42. Write a pandas program to rename specific column name in a given dataframe

import pandas as pd
import numpy as np

values = np.random.randint(0,10,(3,3))
columns = ['col1','col2','col3']

df = pd.DataFrame(values, columns=columns)
print(df)

df = df.rename(columns = {"col2":'column2'})
print(df)