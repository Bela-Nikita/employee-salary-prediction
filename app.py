import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="💼 Salary Predictor")

model = joblib.load('salary_model.pkl')
features = joblib.load('features.pkl')

st.title("Employee Salary Prediction 💰")
st.write("Estimate salary based on job title and location")

job = st.selectbox("Job Role", ['data', 'software', 'project', 'manager', 'business'])
location = st.selectbox("Location", ['San Francisco, CA', 'New York, NY', 'Seattle, WA', 'Austin, TX'])

input_data = pd.DataFrame(columns=features)
input_data.loc[0] = 0
col_job = f"Job Simplified_{job}"
col_loc = f"Location_{location}"
if col_job in features:
    input_data[col_job] = 1
if col_loc in features:
    input_data[col_loc] = 1

if st.button("Predict Salary"):
    salary = model.predict(input_data)[0]
    st.success(f"Estimated Salary: ${int(salary*1000):,}")
