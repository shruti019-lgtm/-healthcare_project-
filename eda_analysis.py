import pandas as pd

# Load cleaned data
df = pd.read_csv("healthcare_cleaned.csv")

print("Dataset loaded successfully")
print(df.head())
print(df.info())
# =========================
# 7. Investigate Negative Billing Records
# =========================
negative_billing = df[df['Billing Amount'] < 0]

print("\nNegative Billing Records:")
print(negative_billing)

print("\nCount of negative billing records:", negative_billing.shape[0])
# =========================
# 8. Patterns in Negative Billing
# =========================
print("\nNegative billing by Medical Condition:")
print(negative_billing['Medical Condition'].value_counts())

print("\nNegative billing by Admission Type:")
print(negative_billing['Admission Type'].value_counts())

print("\nNegative billing by Insurance Provider:")
print(negative_billing['Insurance Provider'].value_counts())
# =========================
# 9. Revenue-safe billing column
# =========================
df['Billing_Adjusted'] = df['Billing Amount'].apply(
    lambda x: x if x > 0 else 0
)

print("\nAdjusted billing created (negative values set to 0 for revenue analysis)")
# =========================
# 10. Outlier Analysis
# =========================

print("\n--- OUTLIER ANALYSIS ---")

# Billing Amount Outliers (IQR Method)
Q1 = df['Billing Amount'].quantile(0.25)
Q3 = df['Billing Amount'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

billing_outliers = df[
    (df['Billing Amount'] < lower_bound) |
    (df['Billing Amount'] > upper_bound)
]

print(f"Billing outlier count: {billing_outliers.shape[0]}")
print(billing_outliers[['Name', 'Billing Amount']].head())

# Age Outliers
age_outliers = df[(df['Age'] < 0) | (df['Age'] > 100)]
print(f"\nAge outlier count: {age_outliers.shape[0]}")
