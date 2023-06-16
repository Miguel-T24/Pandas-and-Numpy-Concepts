# 1. Write a pandas program to convert all the string values to upper, lower cases in a given pandas series. Also find the length of the string values

import pandas as pd
import numpy as np
s = pd.Series(['X', 'Y', 'Z', 'Aaba', 'Baca', np.nan, 'CABA', None, 'bird', 'horse', 'dog'])
print(s)
print("Original series:")

print(s.str.upper())
print(s.str.lower())
print(s.str.len().astype(int))