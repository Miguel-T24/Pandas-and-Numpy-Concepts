# 2. Write a pandas program to convert a panda module series to python list and it's type

import pandas as pd

serie = pd.Series([1,2,3,4,5])
print(serie)

lista = list(serie)

print()
print(lista)
print(type(lista))

# other way
# serie.tolist()