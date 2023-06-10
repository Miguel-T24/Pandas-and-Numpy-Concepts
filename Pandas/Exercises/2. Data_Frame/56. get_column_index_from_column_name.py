# 56. Write a pandasd program to get a coluumn index from column name of a given dataframe

import pandas as pd
import numpy as np

values = np.random.randint(0,10,(5,3))
col = ['col1','col2','col3']

df = pd.DataFrame(values, columns=col)
print(df)


print(df.columns.tolist().index('col2'))
