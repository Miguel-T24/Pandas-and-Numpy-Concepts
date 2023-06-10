# u64. Write a pandas program to add a prefix or suffix to all columns of a given datafme


import pandas as pd
import numpy as np

values = np.random.randint(0,10,(5,3))
col = ['col1','col2','col3']

df = pd.DataFrame(values, columns=col)
print(df)

# Add prefix
df.columns = list(map(lambda x:'A_'+x, df.columns))
print(df)

# reset columns
df.columns = ['col1','col2','col3']
print(df.columns.tolist())

# Add suffix
df.columns = list(map(lambda x:x+'_1',df.columns))
print(df)

# Other way
# print(df.add_prefix("A_"))
# print(df.add_suffix("_1"))

