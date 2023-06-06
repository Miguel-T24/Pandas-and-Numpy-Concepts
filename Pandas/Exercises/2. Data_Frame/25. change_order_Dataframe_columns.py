# 25. Write a pandas program to change the order of a datafram column

import pandas as pd
import numpy as np
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)

print(df)
print(df[['col3','col2','col1']])
print(df)