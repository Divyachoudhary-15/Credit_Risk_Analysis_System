
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(
    page_title="Credit Risk Analysis System",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Credit Risk Analysis System")
st.write("Analyze loan applications and credit risk.")

# Load dataset
if os.path.exists("loan_data.csv"):
    df = pd.read_csv("loan_data.csv")
elif os.path.exists("data/loan_data.csv"):
    df = pd.read_csv("data/loan_data.csv")
else:
    st.error("loan_data.csv file not found.")
    st.stop()

st.subheader("📊 Dataset Overview")

col1, col2 = st.columns(2)
col1.metric("Total Applications", len(df))
col2.metric("Dataset Columns", len(df.columns))

st.subheader("📋 Loan Dataset")
st.dataframe(df, use_container_width=True)

st.subheader("📈 Applicant Income Distribution")

if "ApplicantIncome" in df.columns:
    fig, ax = plt.subplots()
    ax.hist(df["ApplicantIncome"].dropna(), bins=10)
    ax.set_xlabel("Applicant Income")
    ax.set_ylabel("Number of Applicants")
    st.pyplot(fig)
    plt.close(fig)

st.subheader("💰 Loan Amount Analysis")

if "LoanAmount" in df.columns:
    fig, ax = plt.subplots()
    ax.hist(df["LoanAmount"].dropna(), bins=10)
    ax.set_xlabel("Loan Amount")
    ax.set_ylabel("Number of Applicants")
    st.pyplot(fig)
    plt.close(fig)

if "LoanStatus" in df.columns:
    st.subheader("🎯 Loan Status Distribution")
    status_counts = df["LoanStatus"].value_counts()
    st.bar_chart(status_counts)

st.subheader("🔎 Check an Applicant")

income = st.number_input(
    "Applicant Income",
    min_value=0,
    value=30000
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0,
    value=150000
)

credit_history = st.selectbox(
    "Credit History",
    [1, 0],
    format_func=lambda x: "Good (1)" if x == 1 else "Poor (0)"
)

if st.button("Analyze Applicant"):
    if income >= 40000 and credit_history == 1:
        st.success(
            "Preliminary result: Lower risk. "
            "Further verification is required."
        )
    elif credit_history == 0:
        st.warning(
            "Preliminary result: Higher risk. "
            "Manual review is recommended."
        )
    else:
        st.info(
            "Preliminary result: Manual review recommended."
        )

st.caption(
    "Educational project only. This preliminary result is "
    "not a real loan approval or a validated model prediction."
)
