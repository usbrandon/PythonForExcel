import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First', 'Last', 'Street', 'City', 'State', 'Area Code', 'Income']

df.drop(columns='Street', inplace=True)
df = df.set_index('Area Code')

#print(df.loc[8074])
#print(df.loc[8074:, 'First'])

df.First = df.First.str.split().str[0]
#print(df)

df = df.replace(np.nan, 'N/A', regex=True)
print(df)
#to_excel = df.to_excel('modified.xlsx')