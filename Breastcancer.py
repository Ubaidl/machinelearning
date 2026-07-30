import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('cancer_model.pkl', 'rb'))
scaler = pickle.load(open('cancer_scaler.pkl', 'rb'))
feature_names = pickle.load(open('cancer_features.pkl', 'rb'))

st.title("🩺 Breast Cancer Prediction")
st.write("Enter the cell measurement values below:")

# Create input fields dynamically for all 30 features
input_values = []
cols = st.columns(3)
for i, feature in enumerate(feature_names):
    with cols[i % 3]:
        val = st.number_input(feature, value=0.0, format="%.5f")
        input_values.append(val)

if st.button('Predict'):
    input_array = np.array(input_values).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.error("⚠️ Malignant (Cancerous)")
    else:
        st.success("✅ Benign (Non-cancerous)")