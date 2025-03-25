import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load the saved Random Forest model
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)
   
# Initialize LabelEncoder
label_encoder = LabelEncoder()

# Title
st.title('Thyroid Disease Prediction App')
st.write('Provide the required inputs to Predict Market Sales')

# User Inputs
age = st.number_input("Age", min_value=10, value=95)

# Encode categorical features using LabelEncoder
categorical_features = {
    "Gender": ["Male", "Female"],
    "Smoking": ["Yes", "No"],
    "SmokingHistory": ["Never", "Former", "Current"],
    "RadiotherapyHistory": ["Yes", "No"],
    "ThyroidFunction": ["Normal", "Hypo", "Hyper"],
    "PhysicalExamination": ["Normal", "Abnormal"],
    "Adenopathy": ["Present", "Absent"],
    "Pathology": ["Benign", "Malignant"],
    "Focality": ["Unifocal", "Multifocal"],
    "Risk": ["Low", "Moderate", "High"],
    "Stage": ["I", "II", "III", "IV"],
    "Response": ["Complete", "Partial", "None"]
}

# Function to apply Label Encoding
def encode_input(feature_name, selected_value):
    label_encoder.fit(categorical_features[feature_name])  # Fit encoder with feature values
    return label_encoder.transform([selected_value])[0]  # Transform selected value to numeric

# Collect user inputs
gender_val = encode_input("Gender", st.selectbox("Gender", categorical_features["Gender"]))
smoking_val = encode_input("Smoking", st.selectbox("Smoking Status", categorical_features["Smoking"]))
smoking_history_val = encode_input("SmokingHistory", st.selectbox("Smoking History", categorical_features["SmokingHistory"]))
radiotherapy_val = encode_input("RadiotherapyHistory", st.selectbox("Radiotherapy History", categorical_features["RadiotherapyHistory"]))
thyroid_function_val = encode_input("ThyroidFunction", st.selectbox("Thyroid Function", categorical_features["ThyroidFunction"]))
physical_examination_val = encode_input("PhysicalExamination", st.selectbox("Physical Examination", categorical_features["PhysicalExamination"]))
adenopathy_val = encode_input("Adenopathy", st.selectbox("Adenopathy", categorical_features["Adenopathy"]))
pathology_val = encode_input("Pathology", st.selectbox("Pathology", categorical_features["Pathology"]))
focality_val = encode_input("Focality", st.selectbox("Focality", categorical_features["Focality"]))
risk_val = encode_input("Risk", st.selectbox("Risk Level", categorical_features["Risk"]))
stage_val = encode_input("Stage", st.selectbox("Overall Stage", categorical_features["Stage"]))
response_val = encode_input("Response", st.selectbox("Response to Treatment", categorical_features["Response"]))


# Numeric inputs
T = st.number_input("T Stage", min_value=0, max_value=4, value=1)
N = st.number_input("N Stage", min_value=0, max_value=3, value=0)
M = st.number_input("M Stage", min_value=0, max_value=1, value=0)

# Prepare input features
input_features = np.array([[age, gender_val, smoking_val, smoking_history_val, radiotherapy_val,
                            thyroid_function_val, physical_examination_val, adenopathy_val, pathology_val,
                            focality_val, risk_val, T, N, M, stage_val, response_val]])


# Make Prediction
if st.button("Predict Thyroid Cancer Recurrence"):  
    prediction = model.predict(input_features) 
    
    # Convert prediction (0 or 1) into "Yes" or "No"
    result = "Yes" if prediction[0] == 1 else "No"

    st.write(f"Predicted Thyroid Cancer Recurrence: {result}**")


