#Python code demonstrating creating a DataFrame from a dict
import pandas as pd

#initialise data for student grades
data = { 'Name': ['Cheeray', 'Casey'],
         'Score':[89,90]}

# Creates pandas DataFrame
df = pd.DataFrame(data)
df['grade'] = df['Score'].apply(lambda x: 4.0 if 90 <= x <= 100 else '')

print(df)