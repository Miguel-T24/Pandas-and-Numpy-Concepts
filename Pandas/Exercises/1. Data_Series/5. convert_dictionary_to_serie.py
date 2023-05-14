# 5. Write a pandas program to convert a dictionary to a pandas series

import pandas as pd

dic = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

serie = pd.Series(dic)

print(serie)