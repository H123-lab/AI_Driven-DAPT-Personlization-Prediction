# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the datasets
print("Loading datasets...")
sheet1 = pd.read_csv("processed_sheet1.csv")
sheet2 = pd.read_csv("processed_sheet2.csv")
print("Datasets loaded successfully!")

# Step 2: Ensure the 'Patient_ID' column exists in both datasets
if "Patient_ID" not in sheet2.columns:
    print("'Patient_ID' column not found in processed_sheet2.csv. Adding a placeholder column...")
    sheet2["Patient_ID"] = sheet1["Patient_ID"][:len(sheet2)]

# Step 3: Merge the datasets
print("Merging datasets...")
merged_data = pd.merge(sheet1, sheet2, on="Patient_ID", how="inner")
print("Datasets merged successfully!")

# Step 4: Handle missing columns
expected_columns = [
    'Patient_ID', 'Age', 'Gender', 'BMI', 'Cholesterol', 'Hypertension', 'Diabetes',
    'Smoking_Status', 'DAPT_Duration', 'Bleeding_Risk', 'Ischemia_Risk'
]
for col in expected_columns:
    if col not in merged_data.columns:
        print(f"Column '{col}' is missing. Filling with NaN...")
        merged_data[col] = np.nan

# Step 5: Save the merged dataset
merged_data.to_csv("merged_file.csv", index=False)
print("Merged dataset saved as 'merged_file.csv'.")

# Step 6: Analyze BMI distribution by gender
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.histplot(data=merged_data, x="BMI", hue="Gender", kde=True, bins=30, palette="viridis")
plt.title("BMI Distribution by Gender")
plt.xlabel("BMI")
plt.ylabel("Frequency")
plt.savefig("BMI_Distribution.png")
plt.show()
print("BMI Distribution plot saved as 'BMI_Distribution.png'.")

# Step 7: Split the dataset into Part 1 and Part 2
print("Splitting dataset into Part 1 and Part 2...")
part1_columns = ['Patient_ID', 'Age', 'Gender', 'BMI', 'Cholesterol', 'Smoking_Status']
part2_columns = ['Patient_ID', 'DAPT_Duration', 'Bleeding_Risk', 'Ischemia_Risk']

part1_data = merged_data[part1_columns]
part2_data = merged_data[part2_columns]

# Save Part 1 and Part 2 datasets
part1_data.to_csv("DAPT_recommendation_Result_Part1.csv", index=False)
part2_data.to_csv("DAPT_recommendation_Result_Part2.csv", index=False)
print("Part 1 saved as 'DAPT_recommendation_Result_Part1.csv'.")
print("Part 2 saved as 'DAPT_recommendation_Result_Part2.csv'.")

# Step 8: Recommend DAPT Duration based on risks
print("Generating DAPT Duration recommendations...")
def recommend_dapt_duration(row):
    if row['Bleeding_Risk'] == 'High' or row['Ischemia_Risk'] == 'Low':
        return "3 months"
    elif row['Bleeding_Risk'] == 'Moderate' and row['Ischemia_Risk'] == 'Moderate':
        return "6 months"
    else:
        return "12 months"

merged_data['DAPT_Recommendation'] = merged_data.apply(recommend_dapt_duration, axis=1)
merged_data.to_csv("DAPT_Recommendation_Final.csv", index=False)
print("Final dataset with DAPT recommendations saved as 'DAPT_Recommendation_Final.csv'.")

# Step 9: Generate summary statistics
print("Generating summary statistics...")
summary_stats = merged_data.describe(include='all').transpose()
summary_stats.to_csv("Summary_Statistics.csv")
print("Summary statistics saved as 'Summary_Statistics.csv'.")

print("Algorithm execution completed successfully!")