# 11. write a pandas program to sort a given series

import pandas as pd

serie = pd.Series(['100','200','python','300.12','400'])
print("Original : \n{}".format(serie))

serie = pd.Series(serie).sort_values()
print("Sorted: \n{}".format(serie))

