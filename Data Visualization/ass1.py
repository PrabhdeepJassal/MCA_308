import pandas as pd
import os
data = {
    'Tid': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Refund': ['Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'No'],
    'Marital Status': ['Single', 'Married', 'Single', 'Married', 'Divorced', 'Married', 'Divorced', 'Single', 'Married', 'Single'],
    'Taxable Income': ['125K', '100K', '70K', '120K', '95K', '60K', '220K', '85K', '75K', '90K'],
    'Cheat': ['No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)

slctedrows = df.iloc[[0, 4, 7, 8]]

print("\n1.Rows at index 0, 4, 7, 8")
print(slctedrows)

file_name = 'dataset.csv'
df.to_csv(file_name, index=False)

print(f"\n2.Reading and Displaying a CSV File")
print(f"The DataFrame has been saved to a file named")

df_from_csv = pd.read_csv(file_name)
print(df_from_csv)