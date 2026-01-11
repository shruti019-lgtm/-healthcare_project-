import pandas as pd

print("=== CLEAN ANALYSIS STARTED ===")

# 1. Load dataset
df = pd.read_csv("healthcare_datasets.csv")

print("\nOriginal Names (before cleaning):")
print(df["Name"].head())

# 2. Clean Names (fix random capitalization & extra spaces)
df["Name"] = (
    df["Name"]
    .str.strip()
    .str.lower()
    .str.title()
)

print("\nCleaned Names (after cleaning):")
print(df["Name"].head())

# 3. Billing statistics
print("\nBilling statistics:")
print(df["Billing Amount"].describe())

# 4. Count negative billing values
negative_count = (df["Billing Amount"] < 0).sum()
print("\nNegative billing count:", negative_count)

# 5. Create Billing Flag
df["Billing_Flag"] = df["Billing Amount"].apply(
    lambda x: "Negative" if x < 0 else "Valid"
)

print("\nBilling_Flag value counts:")
print(df["Billing_Flag"].value_counts())

# 6. Save cleaned file
df.to_csv("healthcare_cleaned.csv", index=False)

print("\n=== CLEANING COMPLETED SUCCESSFULLY ===")
print("Cleaned file saved as: healthcare_cleaned.csv")
