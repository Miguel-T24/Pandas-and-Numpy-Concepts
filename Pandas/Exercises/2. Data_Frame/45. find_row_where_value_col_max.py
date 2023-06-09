# 45. write a pandas proigram to find the row where the value of a given column is maximum

import pandas as pd
import numpy as np

values = np.random.randint(0,50,(5,3))
columns = ['col1','col2','col3']

df = pd.DataFrame(values,columns=columns)
print(df)

print("Row where col1 has maximum value:")
print(df['col1'].argmax())
print("Row where col2 has maximum value:")
print(df['col2'].argmax())
print("Row where col3 has maximum value:")
print(df['col3'].argmax())