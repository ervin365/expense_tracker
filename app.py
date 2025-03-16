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

# Edit an existing expense
def edit_expense(expenses, index, date, category, amount):
    expenses[index] = [date, category, amount]
    save_expenses(expenses)
    st.success(f"Updated expense: ₹{amount:.2f} under '{category}' on {date}")

# Delete an existing expense
def delete_expense(expenses, index):
    deleted_expense = expenses.pop(index)
    save_expenses(expenses)
    st.success(f"Deleted expense: ₹{deleted_expense[2]} under '{deleted_expense[1]}' on {deleted_expense[0]}")

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
    st.title("Expense Tracker")

    # Load existing expenses
    expenses = load_expenses()

    # Sidebar for adding expenses
    with st.sidebar:
        st.header("Add New Expense")
        date = st.date_input("Date")
        category = st.selectbox("Category", ["Food", "Rent", "Travel", "Other"])
        if category == "Other":
            category = st.text_input("Specify Category")
        amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
        if st.button("Add Expense"):
            add_expense(expenses, str(date), category, amount)
            st.rerun()  # Rerun the app to refresh the expense list

    # Display expenses in a table
    st.write("### Expense List")
    if not expenses:
        st.write("No expenses recorded yet.")
    else:
        # Create a DataFrame-like display for editing and deleting
        for i, expense in enumerate(expenses):
            col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 1, 1])
            with col1:
                st.write(f"**Date:** {expense[0]}")
            with col2:
                st.write(f"**Category:** {expense[1]}")
            with col3:
                st.write(f"**Amount:** ₹{float(expense[2]):.2f}")
            with col4:
                if st.button(f"Edit {i+1}"):
                    st.session_state.edit_index = i
            with col5:
                if st.button(f"Delete {i+1}"):
                    delete_expense(expenses, i)
                    st.rerun()  # Rerun the app to refresh the expense list

    # Edit form (appears when an expense is selected for editing)
    if "edit_index" in st.session_state:
        edit_index = st.session_state.edit_index
        expense = expenses[edit_index]
        with st.form("edit_form"):
            st.header("Edit Expense")
            new_date = st.date_input("Date", value=datetime.strptime(expense[0], "%Y-%m-%d"))
            new_category = st.selectbox("Category", ["Food", "Rent", "Travel", "Other"], index=["Food", "Rent", "Travel", "Other"].index(expense[1]))
            if new_category == "Other":
                new_category = st.text_input("Specify Category", value=expense[1])
            new_amount = st.number_input("Amount (₹)", value=float(expense[2]), min_value=0.0, format="%.2f")
            if st.form_submit_button("Save Changes"):
                edit_expense(expenses, edit_index, str(new_date), new_category, new_amount)
                del st.session_state.edit_index
                st.rerun()  # Rerun the app to refresh the expense list

    # Calculate totals
    if st.button("Calculate Totals"):
        total, category_totals = calculate_totals(expenses)
        st.write(f"**Total expenses:** ₹{total:.2f}")
        st.write("**Totals by Category:**")
        for cat, amt in category_totals.items():
            st.write(f"- {cat}: ₹{amt:.2f}")

if __name__ == "__main__":
    main()