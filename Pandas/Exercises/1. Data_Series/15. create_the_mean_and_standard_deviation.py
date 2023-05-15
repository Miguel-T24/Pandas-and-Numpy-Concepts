# 15. Write a pandas program to create the mean and standard deviation of the data of a given Series

import pandas as pd

s = pd.Series([1,2,3,4,5,6,7,8,9,5,3])
print("Original: \n{}".format(s))

print("Mean: {}".format(s.mean()))
print("Standard Deviation: {}".format(s.std()))
