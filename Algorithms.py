# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
sheet1 = pd.read_csv("processed_sheet1.csv")
sheet2 = pd.read_csv("processed_sheet2.csv")
print("Datasets loaded successfully!")

# Merge the datasets on Patient_ID
merged_data = pd.merge(sheet1, sheet2, on="Patient_ID", how="inner")
print("Datasets merged successfully!")

# Handle missing columns
expected_columns = [
    'Patient_ID', 'Age', 'Gender', 'BMI', 'Cholesterol', 'Hypertension', 'Diabetes',
    'Smoking_Status', 'DAPT_Duration', 'Bleeding_Risk', 'Ischemia_Risk'
]
for col in expected_columns:
    if col not in merged_data.columns:
        merged_data[col] = np.nan  # Fill missing columns with NaN

# Save the merged dataset
merged_data.to_csv("merged_file.csv", index=False)
print("Merged file saved successfully!")

# Split merged data into Part 1 and Part 2
part1_columns = ['Patient_ID', 'Age', 'Gender', 'BMI', 'Cholesterol', 'Smoking_Status']
part2_columns = ['Patient_ID', 'DAPT_Duration', 'Bleeding_Risk', 'Ischemia_Risk']

part1_data = merged_data[part1_columns]
part2_data = merged_data[part2_columns]

# Save Part 1 and Part 2
part1_data.to_csv("DAPT_recommendation_Result_Part1.csv", index=False)
part2_data.to_csv("DAPT_recommendation_Result_Part2.csv", index=False)

print("Part 1 and Part 2 files saved successfully!")

# Plotting for analysis
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.histplot(data=merged_data, x="BMI", hue="Gender", kde=True)
plt.title("BMI Distribution by Gender")
plt.savefig("BMI_Distribution.png")
plt.show()


