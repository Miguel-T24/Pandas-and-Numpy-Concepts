# 44. Write a pandas program to crate e a dtafaame form anumpy array and specify the index column and column header

import pandas as pd
import numpy as np

values = np.random.randint(0,10,(10,3))
columns = ['col1','col2','col3']
index = list(map(lambda x:"Index"+str(x),range(1,11)))

df = pd.DataFrame(values,columns=columns,index=index)

print(df)