Project Overview
This project focuses on analyzing and recommending Dual Antiplatelet Therapy (DAPT) duration based on patient-specific clinical data. The algorithm uses patient demographic, clinical, and risk-related metrics to provide personalized therapy recommendations. It aligns with the study objectives of optimizing treatment strategies and improving patient outcomes.

Key Objectives
Data Integration: Merging multiple datasets (processed_sheet1.csv and processed_sheet2.csv) based on patient IDs to create a comprehensive dataset.
Risk Stratification: Assessing bleeding and ischemia risks to tailor DAPT duration for individual patients.
Visualization: Generating plots to visualize BMI distribution and other key metrics.
Data Analysis: Creating summary statistics and splitting datasets into relevant parts for further analysis.
Recommendation Generation: Providing evidence-based DAPT duration recommendations based on clinical data.
Project Files
The repository includes the following files:

Input Files:

processed_sheet1.csv: Contains demographic and baseline clinical information.
processed_sheet2.csv: Contains risk-related information and additional metrics.
Output Files:

merged_file.csv: The merged dataset combining input files.
BMI_Distribution.png: A plot showing BMI distribution by gender.
DAPT_recommendation_Result_Part1.csv: Split dataset focusing on demographic and baseline data.
DAPT_recommendation_Result_Part2.csv: Split dataset focusing on DAPT duration and risk factors.
DAPT_Recommendation_Final.csv: Final dataset with personalized DAPT recommendations.
Summary_Statistics.csv: Summary statistics for all dataset columns.
Algorithm Script:

DAPT_Recommendation_Algorithm.py: The main Python script performing all analyses and generating outputs.
Features
Dataset Merging:
Ensures all relevant columns are included.
Fills missing columns with placeholder values for consistency.
BMI Distribution Visualization:
Histogram with KDE (Kernel Density Estimation) plot for gender-based BMI analysis.
Dataset Splitting:
Separates merged data into Part 1 (demographic and baseline data) and Part 2 (DAPT and risk factors).
Personalized Recommendations:
DAPT duration is tailored based on bleeding and ischemia risks using an algorithmic approach.
Summary Statistics:
Provides a statistical overview of the dataset for academic reporting.
How to Run the Algorithm
Prerequisites:

Python 3.x installed on your local machine.
Required Python libraries:
pandas
numpy
matplotlib
seaborn
Steps:

Upload the input files (processed_sheet1.csv and processed_sheet2.csv) to your working directory.
Run the script DAPT_Recommendation_Algorithm.py:
bash

python DAPT_Recommendation_Algorithm.py
Outputs will be generated in the working directory.
Testing:

You can also test the algorithm on Google Colab. Upload the input files and script, and execute the cells to validate outputs.
Expected Outputs
A merged dataset with complete patient data.
Split datasets (Part 1 and Part 2) for targeted analysis.
Visualized BMI distribution saved as a .png file.
Final recommendations for DAPT duration in a CSV file.
Summary statistics for academic documentation.
Academic Relevance
This project is aligned with ongoing research into personalized medicine and treatment optimization in cardiovascular care. It integrates real-world clinical data, applying data science methodologies to address critical healthcare challenges. The algorithm demonstrates the practical application of patient-specific data in tailoring therapy recommendations.

Future Scope
Enhancing the algorithm to include additional risk factors.
Expanding the dataset with more patient records for robust recommendations.
Incorporating machine learning models to predict outcomes based on therapy recommendations.
Limitations
The recommendations are based solely on the provided datasets. Additional clinical validation is necessary before real-world implementation.
Missing or incomplete data may affect the accuracy of analyses.
License
This project is licensed under the MIT License, allowing free use, modification, and distribution, provided the original authors are credited.



