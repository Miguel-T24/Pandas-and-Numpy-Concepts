# 24. Write a pandas program to select rows from a given dataframe based in values in some column

import pandas as pd
import numpy as np

d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)
print(df)

print(df[df['col1'] == 4])