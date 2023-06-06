# 23. Write a pandas program to renme columns of given DataFrame

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(9).reshape(3,3), index=range(3), columns=["col1",'col2','col3'])
print(df)

df.columns = ["column1",'column2','column3']
# df = df.rename(columns={'col1': 'Column1', 'col2': 'Column2', 'col3': 'Column3'})
print(df)