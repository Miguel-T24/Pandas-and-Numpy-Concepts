# 43. write a pandas proigram to get a list of a specified column og dataframe

import pandas as pd
import numpy as np

values = np.random.randint(0,10,(3,3))
columns = ['col1','col2','col3']

df = pd.DataFrame(values, columns=columns)
print(df)

print(df['col2'].tolist())