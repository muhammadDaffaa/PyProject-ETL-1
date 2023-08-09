# print(pd.__version__)

import pandas as pd

sheet_id = "2PACX-1vSqZELlKiz569OLqngJ-BKmqsDuwlFcgqsrLTlsiSujHI7EQV-ZGRWhCSSnio-0FbfJ85vItV_beppF"
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/e/{sheet_id}/pub?gid=1623601030&single=true&output=csv")

df_json = df.to_json('json_file.json', orient)

# print(df.iloc[-1])
print(df.iloc[-1])
