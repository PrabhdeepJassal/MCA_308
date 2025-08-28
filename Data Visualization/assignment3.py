import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("AW_BikeBuyer.csv")

print("Original Dataset")
print(df.head())
print("\nColumns:", df.columns)

selected = [
    "BirthDate", "MaritalStatus", "Education", "Occupation",
    "YearlyIncome", "NumberCarsOwned", "CommuteDistance",
    "AvgMonthSpend", "BikeBuyer"
]

df_sel = df[selected].copy()

print("\nSelected Attributes DataFrame")
print(df_sel.head())

df_sel["BirthDate"] = pd.to_datetime(df_sel["BirthDate"])
df_sel["Age"] = (pd.Timestamp.today() - df_sel["BirthDate"]).dt.days // 365


df_sel.drop(columns=["BirthDate"], inplace=True)

print("\nData Types for Preprocessing")
for col in df_sel.columns:
    print(col, "→", df_sel[col].dtype)

income_buy = df_sel.loc[df_sel["BikeBuyer"]==1, "YearlyIncome"]
income_nobuy = df_sel.loc[df_sel["BikeBuyer"]==0, "YearlyIncome"]

print("\nMean income (buyers):", income_buy.mean())
print("Mean income (non-buyers):", income_nobuy.mean())

t_stat, p_val = stats.ttest_ind(income_buy, income_nobuy, equal_var=False)
print(f"T-test: t = {t_stat:.3f}, p = {p_val:.3f}")

commute_ct = df_sel.groupby("CommuteDistance")["BikeBuyer"].agg(['sum','count'])
commute_ct['pct_buyers'] = commute_ct['sum'] / commute_ct['count'] * 100
print("\nPurchase % by Commute Distance")
print(commute_ct)

plt.figure(figsize=(8,5))
df_sel[df_sel["BikeBuyer"]==1]["Age"].hist(alpha=0.5, label="Buyer")
df_sel[df_sel["BikeBuyer"]==0]["Age"].hist(alpha=0.5, label="Non-Buyer")
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Age Distribution by Buyer Status")
plt.legend()
plt.show()

age_buy = df_sel.loc[df_sel["BikeBuyer"]==1, "Age"]
age_nobuy = df_sel.loc[df_sel["BikeBuyer"]==0, "Age"]
ks_stat, ks_p = stats.ks_2samp(age_buy, age_nobuy)
print(f"\nKS-test Age Dist: statistic = {ks_stat:.3f}, p = {ks_p:.3f}")

ct = pd.crosstab(df_sel["MaritalStatus"], df_sel["BikeBuyer"], margins=True)
ct['pct_buyers'] = ct[1] / ct['All'] * 100 
print("\nBuyer % by Marital Status")
print(ct)

# Chi-square test
chi2, p, dof, ex = stats.chi2_contingency(ct.iloc[:-1, :-1])
print(f"\nChi-square: χ² = {chi2:.3f}, p = {p:.3f}")
