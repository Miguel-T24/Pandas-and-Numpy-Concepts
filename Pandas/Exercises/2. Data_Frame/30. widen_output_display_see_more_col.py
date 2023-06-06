# 30. Write a apndas program to widen output display to see more columns.

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

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
print("Original DataFrame")
print(df)