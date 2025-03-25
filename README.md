# Project Overview: Thyroid Cancer Recurrence Prediction

## Title:
### A Comprehensive Analysis and Machine Learning Prediction of Thyroid Cancer Recurrence with Deployment

## Objective
Thyroid cancer recurrence is a significant concern in clinical decision-making. Accurately predicting recurrence can help improve patient outcomes and guide treatment strategies. This project aims to:

* Analyze patient data to identify factors influencing thyroid cancer recurrence.
* Build machine learning models to predict the likelihood of recurrence based on patient demographics, medical history, and tumor characteristics.
* Deploy an interactive web application using Streamlit to allow real-time prediction of recurrence based on user input.

## Scope
### Data Collection and Preprocessing
* Handling missing values, removing duplicates, ensuring correct data types, and encoding categorical variables.
* Standardizing numeric features to improve model performance.
* Visualizing trends and relationships among variables to understand recurrence risk factors.

### Machine Learning Model Development
* Train and compare multiple classification models (e.g., Decision Tree, Random Forest, Support Vector Machine, XGBoost and Gradient Boosting) to predict thyroid cancer recurrence.
* Tune hyperparameters using RandomizedSearchCV and GridSearchCV to improve accuracy.
* Evaluate models using accuracy, precision, recall, F1-score, and confusion matrix.

### Model Deployment
* Create an interactive Streamlit web app where users can input patient details and receive recurrence predictions in real-time.
* Ensure a user-friendly experience by incorporating dropdowns, number inputs, and visualizations.

## Data Description
The dataset used in this project provides a comprehensive overview of thyroid cancer patients, including demographic details, medical history, tumor characteristics, and treatment responses.

### Key Variables and Their Description
Age: The patient's age at diagnosis.

Gender: Categorized as Male or Female.

Smoking & Smoking History: Indicates smoking status and history (Yes/No).

Radiotherapy History: Whether the patient has undergone radiotherapy (Yes/No).

Thyroid Function: The patient’s thyroid function status.

Physical Examination: Results of the clinical examination.

Adenopathy: Presence of swollen lymph nodes.

Pathology: Classification of the tumor.

Focality: Whether the cancer is Unifocal or Multifocal.

Risk Level: Risk assessment of the cancer..

TNM Staging:

T (Tumor Stage): Tumor size classification.

N (Node Stage): Lymph node involvement.

M (Metastasis): Presence of distant metastasis.

Stage: Overall stage of the cancer (I, II, III, IV).

Response to Treatment:

Recurred: The target variable, indicating whether the cancer has recurred (Yes/No).

## Methodology
 * Build an interactive Streamlit web application where users can input patient details and get real-time recurrence predictions.
 * Ensure the model is robust and reliable by validating it on test data.

