# Write a Pandas program to create a time-series with two index labels and random values. Also print the type of the index.

import pandas as pd
import numpy as np
import datetime
from datetime import datetime, date
dates = [datetime(2011, 9, 1), datetime(2011, 9, 2)]
print("Time-series with two index labels:")
time_series = pd.Series(np.random.randn(2), dates)
print(time_series)
print("\nType of the index:")
print(type(time_series.index))