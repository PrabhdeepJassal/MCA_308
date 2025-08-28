import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.DataFrame(np.random.randint(1, 201, size=(100, 30)))

df = df.mask(df.applymap(lambda x: 10 <= x <= 60))

rowcnt = df.isna().sum(axis=1)
colcnt = df.isna().sum(axis=0)

print("NA rows:", rowcnt)
print("NA columns:", colcnt)

df = df.apply(lambda col: col.fillna(col.mean()), axis=0)
plt.figure(figsize=(12, 8))
sns.heatmap(df)
plt.title("Heatmap of Dataset")
plt.show()

corr = df.corr()

colslow = (corr.apply(lambda x: (x <= 0.7).sum()) > 0).sum()
print("no. of cols correlation <= 0.7", colslow)
def normalize(col):
    return (col - col.min()) / (col.max() - col.min()) * 10
df_normalized = df.apply(normalize, axis=0)


df_binary = df_normalized.applymap(lambda x: 0 if x <= 5 else 1)

plt.figure(figsize=(10, 6))
sns.histplot(df_normalized[0], kde=True, bins=20) 
plt.title("Distribution of Column 0 (Normalized)")
plt.show()

plt.figure(figsize=(10, 6))
sns.kdeplot(df_normalized[1], fill=True)
plt.title("KDE of Column 1 (Normalized)")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df_normalized.iloc[:, :5]) 
plt.title("Boxplot of First 5 Columns")
plt.show()