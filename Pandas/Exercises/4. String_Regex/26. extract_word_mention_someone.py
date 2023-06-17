# 26. Write a pandas program to exrtact word mention someone in twwwts using @ from the specified column of given datarframe.

import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
df = pd.DataFrame({
    'tweets': ['@Obama says goodbye','Retweets for @cash','A political endorsement in @Indonesia', '1 dog = many #retweets', 'Just a simple #egg']
    })
print("Original DataFrame:")
print(df)

df['mention'] = df['tweets'].str.extract('(@\w+)',expand=True)
print(df)