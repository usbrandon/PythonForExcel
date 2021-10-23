import pandas as pd
from openpyxl.workbook import Workbook

df_csv = pd.read_csv('Names.csv', header=None)
df_csv.columns = ['First', 'Last', 'Street', 'City', 'State', 'Area Code', 'Income']

print(df_csv.iloc[2,1])