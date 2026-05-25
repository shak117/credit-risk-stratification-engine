import streamlit as st

st.title("Credit Risk Prediction System")

st.sidebar.header("Customer Input")

age = st.number_input("Age")

income = st.number_input("Income")

loan = st.number_input("Loan Amount")

if st.button("Predict Risk"):

    st.success("Prediction placeholder")