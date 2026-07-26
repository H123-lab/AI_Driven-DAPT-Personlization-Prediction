# AI-Driven DAPT Personalization After PCI

## Overview

This repository accompanies the study:

**"Explainable Artificial Intelligence for Personalized Dual Antiplatelet Therapy Risk Stratification Following Percutaneous Coronary Intervention: External Validation and Economic Evaluation."**

The project develops and externally validates an explainable machine-learning framework for individualized prediction of ischemic and bleeding risk among patients receiving dual antiplatelet therapy (DAPT) after percutaneous coronary intervention (PCI).

---

## Study Objectives

The study aimed to:

* Develop an explainable machine-learning model for post-PCI risk stratification.
* Predict both ischemic and major bleeding events.
* Compare machine-learning performance with conventional clinical risk scores.
* Evaluate model calibration and clinical utility.
* Explore the potential economic implications of AI-guided DAPT personalization.

---

## Study Cohorts

### Development Cohort

United Arab Emirates PCI cohort

* n = 4,812 patients
* Used for model development and internal validation

### External Validation Cohort

MIMIC-IV database

* n = 3,406 patients
* Used for independent external validation

---

## Outcomes

### Composite Ischemic Events

* Myocardial infarction
* Ischemic stroke
* Stent thrombosis
* Cardiovascular death

### Major Bleeding Events

Defined according to:

* BARC Type 3
* BARC Type 5

---

## Models Evaluated

### Primary Model

* Weighted LightGBM

### Benchmark Models

* Logistic Regression
* Random Forest
* Neural Network

---

## Model Explainability

Model interpretability was evaluated SHAP_Global_Feature:

Analyses included:

* Global feature importance
* Feature contribution assessment
* Clinical plausibility evaluation

---

## Performance Evaluation

Model performance was assessed using:

* AUROC
* Calibration plots
* Calibration intercept
* Calibration slope
* Decision curve analysis
* Internal cross-validation
* Independent external validation

---

## Clinical Utility Assessment

Clinical usefulness was evaluated using:

* Risk stratification analyses
* Decision curve analysis
* Model-based clinical impact projections

The study does not evaluate observed treatment effects and should be interpreted as predictive and hypothesis-generating.

---

## Economic Evaluation

Exploratory health-economic analyses included:

* Quality-adjusted life-years (QALYs)
* Incremental cost-effectiveness ratios (ICERs)
* Deterministic sensitivity analysis
* Probabilistic sensitivity analysis
* Monte Carlo simulation

Economic findings are based on modeled projections and not prospective interventional outcomes.

---

## External Validation (MIMIC-IV)

External validation was performed using the MIMIC-IV database (PhysioNet credentialed access), which represents an independent critical care cohort distinct from the UAE PCI development cohort.

The model was applied without recalibration to assess transportability across heterogeneous clinical settings.

Performance metrics including AUROC, calibration slope, calibration intercept, and decision curve analysis were computed independently in the external cohort.

---

## Data Availability

Patient-level clinical data cannot be publicly shared because of privacy, ethical, and regulatory restrictions.

The MIMIC-IV database is available through PhysioNet credentialed access.

Aggregated study outputs and documentation are provided to support transparency and reproducibility.

We provide the requested information regarding the data sources used in this study.
 
1. MIMIC-IV dataset
 
The external validation cohort was obtained from the Medical Information Mart for Intensive Care IV (MIMIC-IV) database.
 
Dataset:
Medical Information Mart for Intensive Care IV (MIMIC-IV)
 
Access platform:
PhysioNet Credentialed Health Data Access framework
 
Dataset access link:
https://physionet.org/content/mimiciv/
 
Data governance authority:
PhysioNet Credentialed Health Data Access
 
Contact email:
[physionet-support@mit.edu]
 
Access to MIMIC-IV requires completion of the required training, credentialing process, and approval through PhysioNet due to the inclusion of sensitive de-identified clinical information.
 
2. UAE dataset
 
The UAE dataset referenced in the manuscript was obtained from the Bayanat Open Data Portal.
 
Dataset:
“Prevalence of Obesity in the UAE”
 
Source:
Bayanat Open Data Portal
 
Access link:
https://data.bayanat.ae
 
This dataset is publicly available under the data-sharing policies of the Bayanat Open Data Portal and therefore does not require institutional data governance approval for access.

Institutional data governance authority (UAE development cohort):
Ministry of Health and Prevention (MOHAP), United Arab Emirates
Website: https://mohap.gov.ae
General contact email: info@mohap.gov.ae

Institutional data governance authority (MIMIC-IV external validation cohort):
PhysioNet Credentialed Health Data Access Framework
Dataset: Medical Information Mart for Intensive Care IV (MIMIC-IV)
Dataset page: https://physionet.org/content/mimiciv/
Support email: physionet-support@mit.edu

---

## Reproducibility

This repository contains:

* Documentation of analytical workflows
* Variable definitions
* Model performance summaries
* Reproducibility materials

No identifiable patient information is included.

---

## Disclaimer

This repository is intended for academic and research purposes only.

The predictive models described are investigational and should not be used for clinical decision-making without prospective validation and regulatory approval.

---

## License

MIT License


