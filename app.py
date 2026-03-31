import streamlit as st
import pandas as pd

st.title("💰 Personal Budget Tracker")

# Create session state to store expenses
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Input fields
date = st.date_input("Select Date")
item = st.text_input("Expense Item")
amount = st.text_input("Amount Spent")

# Submit button
if st.button("Add Expense"):
    try:
        amount_value = float(amount)

        if amount_value < 0:
            raise ValueError("Negative value")

        # Save data
        st.session_state.expenses.append({
            "Date": date,
            "Item": item,
            "Amount": amount_value
        })

        st.success("Expense added successfully!")

    except:
        st.error("❌ Please enter a valid positive number for Amount!")

# Display table
if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    st.subheader("📊 Expense Table")
    st.dataframe(df)

    total = df["Amount"].sum()
    st.write("### 💵 Total Spent: RM", total)
