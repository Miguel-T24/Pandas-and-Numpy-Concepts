# 59. Write a pandas program to get first n records of a datafame

import pandas as pd
import numpy as np

values = np.random.randint(0,10,(5,3))
col = ['col1','col2','col3']

df = pd.DataFrame(values, columns=col)
print(df)

print(df.head(3))