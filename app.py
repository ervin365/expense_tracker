import streamlit as st
import csv
from datetime import datetime

# Load expenses from a CSV file
def load_expenses():
    try:
        with open("expenses.csv", mode="r") as file:
            reader = csv.reader(file)
            expenses = [row for row in reader]
        return expenses
    except FileNotFoundError:
        return []

# Save expenses to a CSV file
def save_expenses(expenses):
    with open("expenses.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(expenses)

# Add a new expense
def add_expense(expenses, date, category, amount):
    expenses.append([date, category, amount])
    save_expenses(expenses)
    st.success(f"Added expense: ₹{amount:.2f} under '{category}' on {date}")

# Calculate total expenses and totals by category
def calculate_totals(expenses):
    total = sum(float(expense[2]) for expense in expenses)
    category_totals = {}
    for expense in expenses:
        category = expense[1]
        amount = float(expense[2])
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    return total, category_totals

# Main Streamlit app
def main():
    st.title("Enhanced Expense Tracker")

    # Load existing expenses
    expenses = load_expenses()

    # Input form
    with st.form("expense_form"):
        date = st.date_input("Date")
        category = st.selectbox("Category", ["Food", "Rent", "Travel", "Other"])
        if category == "Other":
            category = st.text_input("Specify Category")
        amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
        submitted = st.form_submit_button("Add Expense")
        if submitted:
            add_expense(expenses, str(date), category, amount)

    # Display expenses
    st.write("### Expense List")
    for expense in expenses:
        st.write(f"{expense[0]} | {expense[1]} | ₹{float(expense[2]):.2f}")

    # Calculate totals
    if st.button("Calculate Totals"):
        total, category_totals = calculate_totals(expenses)
        st.write(f"**Total expenses:** ₹{total:.2f}")
        st.write("**Totals by Category:**")
        for cat, amt in category_totals.items():
            st.write(f"- {cat}: ₹{amt:.2f}")

if __name__ == "__main__":
    main()