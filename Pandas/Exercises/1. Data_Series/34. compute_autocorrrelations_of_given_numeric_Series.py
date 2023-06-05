# 34. Write pandas program to compute the autorrelations fo a given numeric series

import pandas as pd
import numpy as np

num_series = pd.Series(np.arange(15)+np.random.normal(1,10,15))
print("Original series:")
print(num_series)

autoc = [num_series.autocorr(i).round(2) for i in range(11)]
print("\nAutocorrelations of the said series")
print(autoc)