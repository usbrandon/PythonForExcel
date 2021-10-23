import pandas as pd
from openpyxl.workbook import Workbook

df = pd.read_csv('Names.csv', header=None)
df.columns = ['First', 'Last', 'Street', 'City', 'State', 'Area Code', 'Income']

#print(df.loc[(df['City'] == 'Riverside') & (df['First']=='John')])

df['Tax %'] = df['Income'].apply(lambda x: .15 if 10000 < x < 40000 else .20 if 40000 < x < 80000 else .25)

df['Taxes Owed'] = df['Income'] * df['Tax %']
print(df)

to_drop = ['First', 'Street', 'Area Code']
df.drop(columns = to_drop, inplace=True)
print(df)

df['Test Col'] = False
df.loc[df['Income'] > 60000, 'Test Col'] = True
print(df)
print(df.groupby(['Test Col']).mean().sort_values('Income'))