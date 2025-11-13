import pandas as pd
import os
import seaborn as sns
data = {
    'Tid': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Refund': ['Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'No'],
    'Marital Status': ['Single', 'Married', 'Single', 'Married', 'Divorced', 'Married', 'Divorced', 'Single', 'Married', 'Single'],
    'Taxable Income': ['125K', '100K', '70K', '120K', '95K', '60K', '220K', '85K', '75K', '90K'],
    'Cheat': ['No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)

slctedrows = df.iloc[[0, 4, 7, 8]]
#question 1
print("\n1.Rows at index 0, 4, 7, 8")
print(slctedrows)

file_name = 'dataset.csv'
df.to_csv(file_name, index=False)

#question 2
print(f"\n2.Reading and Displaying a CSV File")
print(f"The DataFrame has been saved to a file named")

df_from_csv = pd.read_csv(file_name)
print(df_from_csv)


#question 4
print("\n4.Demonstrating Attribute Types")
nominal_data = ['Sales', 'HR', 'Engineering', 'HR', 'Sales']
binary_data = ['Pass', 'Fail', 'Pass', 'Pass', 'Fail']

ordinal_data = ['Low', 'Medium', 'High', 'Medium', 'Low']
level_order = ['Low', 'Medium', 'High']
ordinal_cat_type = pd.CategoricalDtype(categories=level_order, ordered=True)

discrete_numeric_data = [5, 2, 10, 8, 5]
continuous_numeric_data = [170.5, 165.1, 182.3, 175.0, 170.5]

attribute_df = pd.DataFrame({
    'Department (Nominal)': nominal_data,
    'Result (Binary)': binary_data,
    'Performance (Ordinal)': pd.Series(ordinal_data, dtype=ordinal_cat_type),
    'Projects (Discrete Numeric)': discrete_numeric_data,
    'Height (Continuous Numeric)': continuous_numeric_data
})

print(attribute_df)
print(attribute_df.info())


#  question 5

print("\n5.Navigating the DataFrame")

rows_3_to_7 = df.iloc[3:8]
print("\n1.selecting rows from index 3 to 7-")
print(rows_3_to_7)

rows_4_to_8_cols_2_to_4 = df.iloc[4:9, 2:5]
print("\n2.selecting rows 4-8 and columns 2-4-")
print(rows_4_to_8_cols_2_to_4)

all_rows_cols_1_to_3 = df.iloc[:, 1:4]
print("\n3.selecting all rows for columns 1-3-")
print(all_rows_cols_1_to_3)


# question 6
iris_filename = '/Users/prabhdeepsingh/Data\ Visualization/Iris.csv'
iris_df = pd.read_csv(iris_filename)

print("\n2. Displaying the first 5 rows of the Iris dataset:")
print(iris_df.head())

