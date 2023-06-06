# 27. Write a panda sprogram to write a datafame to csv file using tab separator

# 27. write_df_to_csv_using_tab
import pandas as pd
import numpy as np
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)
print(df)

print('Dataframe from new file csv file:')
df.to_csv("27. write_df_to_csv_using_tab.csv", sep='\t',index=False)

new_df = pd.read_csv("./27. write_df_to_csv_using_tab.csv")
print(new_df)