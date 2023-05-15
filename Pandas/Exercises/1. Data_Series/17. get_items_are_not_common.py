# 17. Write a pandas program to get the items which are not common of two given series

import pandas as pd
import numpy as np

sr1 = pd.Series([1,2,3,4,5])
sr2 = pd.Series([2,4,6,8,10])

print("Series 1:\n{}".format(sr1))
print("Series 2:\n{}".format(sr2))

sr11 = pd.Series(np.union1d(sr1, sr2))
sr22 = pd.Series(np.intersect1d(sr1, sr2))
result = sr11[~sr11.isin(sr22)]

print("Resultado: \n{}".format(result))
