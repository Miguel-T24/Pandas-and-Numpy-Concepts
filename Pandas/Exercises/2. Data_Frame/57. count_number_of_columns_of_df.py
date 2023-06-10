# 57. Write a pandsas program to count number of columns of a dataframe

import pandas as pd
import numpy as np

values = np.random.randint(0,10,(5,3))
col = ['col1','col2','col3']

df = pd.DataFrame(values, columns=col)
print(df)

print(len(df.columns))