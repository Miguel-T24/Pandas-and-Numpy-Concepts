# 41. Write a panda sprogram to conbvert dataframe column type from string datetime

import pandas as pd
import numpy as np
s = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000'])
print("String Date:")
print(s)

print(s.dtype)
s=pd.to_datetime(s)
print(s)
print(s.dtype)