import streamlit as st
import joblib
import pandas as pd

# Page config
st.set_page_config(page_title="💼 Salary Predictor")

# Load model and features
model = joblib.load('salary_model1.pkl')
features = joblib.load('features1.pkl')
# UI
st.title("💼 Employee Salary Prediction")
st.write("Estimate salary based on job role, location, and skills")

# Dropdowns
job = st.selectbox("Job Role", ['data', 'software', 'project', 'manager', 'business'])
location = st.selectbox("Location", ['San Francisco, CA', 'New York, NY', 'Seattle, WA', 'Austin, TX'])


# Skill checkboxes
python = st.checkbox("Python")
excel = st.checkbox("Excel")
sql = st.checkbox("SQL")

# Prepare input DataFrame with all features set to 0
input_data = pd.DataFrame(columns=features)
input_data.loc[0] = 0  # Initialize first row with 0s

input_data.at[0, 'python_yn'] = int(python)
input_data.at[0, 'excel_yn'] = int(excel)
input_data.at[0, 'sql_yn'] = int(sql)

# Predict
if st.button("Predict Salary"):
    try:
        salary = model.predict(input_data)[0]
        st.success(f"💰 Estimated Salary: ${int(salary * 1000):,}")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")

