# 21. Write a pandas program to find the positions of numebrs that are multiples of 5 of a given series


import pandas as pd
import numpy as np

l = [1,9,8,6,9,7,1,5,1]
s = pd.Series(l)
print(s)

result = np.where(s%5==0)
print(result)