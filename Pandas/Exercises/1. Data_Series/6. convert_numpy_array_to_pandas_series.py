# 6. Write a pandas program to convert a numpy array to a pandas series

import numpy as np
import pandas as pd

num_array = np.array([10,20,30,40,50])
print("Numpy Array")
print(num_array)

pan_series = pd.Series(num_array)
print("Pandas Series:")
print(pan_series)