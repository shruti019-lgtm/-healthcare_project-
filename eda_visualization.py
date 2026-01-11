import pandas as pd
import matplotlib.pyplot as plt
# Load cleaned dataset
df = pd.read_csv("healthcare_cleaned.csv")

print("Dataset loaded successfully")
print(df.head())
plt.figure()
plt.hist(df["Billing Amount"], bins=30)
plt.title("Distribution of Billing Amount")
plt.xlabel("Billing Amount")
plt.ylabel("Frequency")
plt.show()

# Average billing by medical condition
avg_billing_condition = df.groupby("Medical Condition")["Billing Amount"].mean()

plt.figure()
avg_billing_condition.sort_values().plot(kind="barh")
plt.title("Average Billing Amount by Medical Condition")
plt.xlabel("Average Billing Amount")
plt.ylabel("Medical Condition")
plt.show()

# Average billing by admission type
avg_billing_admission = df.groupby("Admission Type")["Billing Amount"].mean()

plt.figure()
avg_billing_admission.plot(kind="bar")
plt.title("Average Billing Amount by Admission Type")
plt.xlabel("Admission Type")
plt.ylabel("Average Billing Amount")
plt.show()

# Gender distribution
gender_counts = df["Gender"].value_counts()

plt.figure()
gender_counts.plot(kind="bar")
plt.title("Patient Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

