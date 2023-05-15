# 19. Write a pandas program to claculate the frecuency count of each unique value of a given series

import pandas as pd
import numpy as np

num_series = pd.Series(np.take(list('0123456789'), np.random.randint(10, size=40)))
print("Num Series\n{}".format(num_series))

result = num_series.value_counts()
print("\nResult:\n{}".format(result))
