Data Collection for AI-Driven DAPT Personalization Study
Introduction
This document outlines the data collection process for the study on AI-driven personalization of dual antiplatelet therapy (DAPT) duration post-percutaneous coronary intervention (PCI). The study integrates data from global and regional sources to ensure a comprehensive understanding of ischemic and bleeding risks in diverse populations.

Data was gathered from two key sources:

The MIMIC-IV PhysioNet database, which provides a rich dataset of global critical care data.
The UAE-specific dataset, titled "Prevalence of Obesity in the UAE," from the Bayanat Data Portal (data.bayanat.ae).
These datasets were selected to incorporate international and regional patient characteristics, ensuring the model accounts for unique UAE-specific risk factors alongside global trends.

Data Sources
Source 1: MIMIC-IV PhysioNet
Scope: The MIMIC-IV database includes de-identified clinical data for ICU patients, including demographics, diagnoses, lab results, medication records, and follow-up outcomes.
Purpose: This dataset was used to train AI algorithms and benchmark global trends in ischemic and bleeding risks associated with DAPT duration.
Citation:
Johnson AEW, Pollard TJ, Shen L, et al. MIMIC-IV (version 2.0). PhysioNet. DOI: 10.13026/9efh-wj98.

Source 2: UAE Dataset
Dataset Title: Prevalence of Obesity in the UAE
Source: Bayanat Data Portal (data.bayanat.ae).
Scope: This open dataset provides UAE-specific data on demographics, lifestyle factors, obesity prevalence, and regional healthcare practices.
Purpose: To analyze UAE-specific risk factors, including genetic predispositions and lifestyle variations, that influence ischemic and bleeding outcomes in patients undergoing DAPT.
Relevance: Incorporating regional insights ensures precision medicine strategies tailored to the UAE population.
Variables Collected
Sheet 1: Patient-Level Data
Demographics: Age, Gender, BMI, Smoking Status.
Comorbidities: Hypertension, Diabetes.
Clinical Metrics: Resting Heart Rate, Heart Rate Variability, Autonomic Function Score, Arrhythmia Type.
Treatment: DAPT Medication, DAPT Duration (months).
Outcomes: Ischemic Event, Bleeding Event, Event-Free Survival.
Follow-Up Metrics: Follow-Up Duration (months), Medication Adherence (%).
Sheet 2: Time-Series Clinical Data
Follow-Up Metrics: Follow-Up Duration (months), Medication Adherence (%).
Genetic and Regional Factors: Genetic Risk Score, Region, Obesity Category.
Clinical Data: ICU Stay, Diagnosis, Lab Results, ECG Timestamp, Heart Rate (bpm), Arrhythmia Type (AFib, VT).
Lifestyle Factors: Weight (kg), Physical Activity.
Outcomes: Total Cholesterol (mg/dL), Coronary Artery Disease.
Data Collection Methodology
Data Extraction: Data from MIMIC-IV and Bayanat datasets was extracted using standardized queries to ensure completeness and relevance to study objectives.
Data Cleaning:
Missing values for critical variables like BMI and lab results were imputed using median imputation.
Outliers were identified and managed using z-score thresholds for continuous variables.
Data Preprocessing: Variables were standardized where necessary (e.g., cholesterol levels) to ensure compatibility across datasets.
De-Identification: All patient data was de-identified to comply with data privacy regulations, ensuring no personally identifiable information (PII) was included.
Data Organization
Sheet 1:
Focus: Patient-level data summarizing demographics, comorbidities, clinical metrics, and treatment outcomes.
Purpose: Provides baseline information for risk modeling and outcome analysis.
Sheet 2:
Focus: Time-series clinical data with detailed follow-up metrics, including genetic and regional factors.
Purpose: Supports dynamic risk prediction and identification of UAE-specific influences on DAPT outcomes.
Ethical Considerations
The study complies with the ethical guidelines and data usage policies outlined by the respective data sources.
Both the MIMIC-IV PhysioNet and Bayanat Data Portal datasets are publicly available, de-identified, and meet ethical standards for secondary research.
All data was handled securely, ensuring patient confidentiality and compliance with data-sharing agreements.