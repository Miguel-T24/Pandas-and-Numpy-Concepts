# 9. Write a pandas program to convert a given series to an array

import pandas as pd
import numpy as np

serie = pd.Series([100,200,"python",300.12,400])
print("Serie:\n{}".format(serie))

# Convert to List
lista = list(serie)
print("Array:\n{}".format(lista))
print(type(lista))

# Convert to Array
num_array = np.array(serie)
print("Array:\n{}".format(num_array))
print(type(num_array))

