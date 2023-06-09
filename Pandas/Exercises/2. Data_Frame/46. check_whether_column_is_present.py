# 46. Write a pandass program to check whether a given column is present ina  dataframe or not

import pandas as pd
import numpy as np

values = np.random.randint(0,50,(5,3))
columns = ['col1','col2','col3']

df = pd.DataFrame(values,columns=columns)
print(df)

def exist(col,cols):
    return "Column Exist" if col in cols else "Column not Exist"

print(exist('col1',df.columns))
print(exist('col4',df.columns))