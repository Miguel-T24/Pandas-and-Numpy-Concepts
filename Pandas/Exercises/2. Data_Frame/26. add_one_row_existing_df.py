# 26. Write a pandas program to add one row in an existing dtaafame

import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.arange(15).reshape(5,3), columns=['col1','col2','col3'])
print(df)

df.loc[5] = list(range(10,13))
print(df)

df2 = {'col1':13,"col2":14,'col3':15}
df = df.append(df2, ignore_index=True)
print(df)