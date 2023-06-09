# 51. Write a pandas program to convert the datatype of given colun (floats to ints).

import pandas as pd
import numpy as np

values = np.random.uniform(0,10,(5,3))

df = pd.DataFrame(values, columns=['col1','col2','col3'])
print(df)
print(df.dtypes)

df = df.astype({'col1':'int64','col2':int,'col3':int})
print(df)
print(df.dtypes)