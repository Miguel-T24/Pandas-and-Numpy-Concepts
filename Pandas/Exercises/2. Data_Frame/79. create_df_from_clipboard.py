# 79. Write a pandas program to crate a datafrme fro the clipboard (data from an excel spreadsheet or a google sheet).

import pandas as pd
df = pd.read_clipboard()
print("Data from clipboard to DataFrame:")
print(df)