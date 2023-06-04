# 3. Write a pandas program to add, substract, multiple and divide two pandas series

import pandas as pd

serie1 = pd.Series([2,4,6,8,10])
serie2 = pd.Series([1,3,5,7,9])

print("Series")
print(serie1)
print(serie2)

print("\nAdd")
print(serie1 + serie2)

print("\nSubstract:")
print(serie1 - serie2)

print("\nMultiply:")
print(serie1 * serie2)

print("\nDivide")
print(serie1/serie2)