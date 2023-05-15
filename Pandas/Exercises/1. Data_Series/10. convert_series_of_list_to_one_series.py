# 10. Write a pandas program to convert Series of list to one Series

import pandas as pd
from itertools import chain

series_of_lists = pd.Series([["red","green","white"], ["red","black"],["yellow"]])
print("series of lists:\n{}".format(series_of_lists))

# Way 1: importing chain from itertools
series_one = list(chain(*list(series_of_lists)))
series_one = pd.Series(series_one)
print(series_one)

# Way 2: Using pandas functions
series_one2 = series_of_lists.apply(pd.Series).stack().reset_index(drop=True) 
print(series_one2)