# 29. Write a pandas program to delete dataframe rows based on given column

import pandas as pd

data = [
    [1,4,7],
    [4,5,8],
    [3,6,9],
    [4,7,0],
    [5,8,1]
]

columns = ['col1','col2','col3']

df = pd.DataFrame(data = data , columns=columns)
print(df)

print(df[df['col2'] !=5])