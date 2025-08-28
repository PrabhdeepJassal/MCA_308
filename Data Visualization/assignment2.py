import pandas as pd

# Q.1 Create dataset
data = {
    "Tid": [1,2,3,4,5,6,7,8,9,10],
    "Refund": ["Yes","No","No","Yes","No","No","Yes","No","No","No"],
    "Marital Status": ["Single","Married","Single","Married","Divorced",
                       "Married","Divorced","Single","Married","Single"],
    "Taxable Income": ["125K","100K","70K","120K","95K","60K","220K","85K","75K","90K"],
    "Cheat": ["No","No","No","No","Yes","No","No","Yes","No","Yes"]
}

df = pd.DataFrame(data)
print("Original DataFrame")
print(df)

rows = df.loc[[0, 4, 7, 8]]
print("\nLocated Rows (0, 4, 7, 8)")
print(rows)

df.to_csv("data.csv", index=False)   
csv_df = pd.read_csv("data.csv")    
print("\nData Read from CSV ")
print(csv_df)
