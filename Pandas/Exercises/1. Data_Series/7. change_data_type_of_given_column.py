# 7. Write a pandas program to change the data type og given a column or Series

import pandas as pd


serie = pd.Series([100,200,"python",300.12,400])

print("original Serie: ")
print(serie)

print("\ndtype changed:")
serie = pd.to_numeric(serie, errors = 'coerce')
print(serie)
print(serie.dtype)