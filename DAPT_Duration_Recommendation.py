# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Step 2: Load the datasets
sheet1 = pd.read_csv('processed_sheet1.csv')
sheet2 = pd.read_csv('processed_sheet2.csv')

# Step 3: Merge the datasets
data = pd.merge(sheet1, sheet2, on='Patient_ID', how='inner')

# Step 4: Data Preprocessing
# Handle missing values
data.fillna(data.median(numeric_only=True), inplace=True)

# Encode categorical variables
categorical_columns = ['Gender', 'Smoking_Status', 'Obesity_Category', 'Region']
for column in categorical_columns:
    le = LabelEncoder()
    if column in data.columns:
        data[column] = le.fit_transform(data[column].astype(str))

# Scale numerical features
scaler = StandardScaler()
numerical_columns = ['Age', 'BMI', 'Total_Cholesterol (mg/dL)', 'Follow_Up_Duration_Months']
data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

# Step 5: Define features (X) and target (y)
X = data[['Age', 'BMI', 'Smoking_Status', 'Hypertension', 'Diabetes', 'Coronary_Artery_Disease', 
          'Total_Cholesterol (mg/dL)', 'Physical_Activity']]
y = data['DAPT_Duration_Months']

# Step 6: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Train a regression model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Step 8: Evaluate the model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model Evaluation:\nMean Absolute Error (MAE): {mae}\nR² Score: {r2}")

# Step 9: Save the predictions and model
data['Predicted_DAPT_Duration'] = model.predict(X)
data.to_csv('dapt_duration_recommendation_result.csv', index=False)
print("Results saved to 'dapt_duration_recommendation_result.csv'")
