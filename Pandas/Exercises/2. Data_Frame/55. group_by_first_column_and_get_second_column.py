# 55. Write a pandas program to group by the first column and get second column as list in rows

import pandas as pd

values = [
    ['C1',1],
    ['C1',2],
    ['C2',3],
    ['C2',3],
    ['C2',4],
    ['C3',6],
    ['C2',5]
]

columns = ['col1','col2']

df= pd.DataFrame(values,columns=columns)
print(df)

print(df.groupby('col1')['col2'].apply(list))