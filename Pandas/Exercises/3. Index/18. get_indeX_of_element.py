# 18. Write a pandas program to get the index of an element of a given series

import pandas as pd
ds = pd.Series([1,3,5,7,9,11,13,15], index=[0,1,2,3,4,5,7,8])
print("Original Series:")
print(ds)
print("\nIndex of 11 in the said series:")
x = ds[ds == 11].index[0]
print(x)