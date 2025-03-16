# Expense Tracker

## Overview
Expense Tracker is a comprehensive application designed to help users manage their expenses effectively. The application allows users to record, categorize, and analyze their spending habits, providing insights into their financial patterns. This project is built using Python and supports CSV-based expense tracking.

## Features
- **Expense Management:** Add, edit, and delete expenses with ease.
- **Categorization:** Classify expenses into predefined or custom categories.
- **Data Storage:** Stores expense data in a CSV file for easy access and manipulation.
- **User-Friendly Interface:** Simple and intuitive interface for smooth navigation.
- **Export/Import Functionality:** Save and retrieve expense data in CSV format.

## Technologies Used
- **Python**: Core language for the application logic.
- **CSV Module**: Handles reading and writing expense data.
- **Streamlit**: Handles interface.

## Installation

### Prerequisites
Ensure you have Python installed on your system. Download it from [Python's official site](https://www.python.org/).

### Setup
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd ExpenseTracker
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python app.py
   ```

## Usage
1. **Launching the App:**
   - Run `python app.py` to start the application.
   - Follow the on-screen prompts to enter expenses.
   
2. **Adding an Expense:**
   - Enter the date, amount, category, and description.
   - The expense is saved in `expenses.csv`.
   
3. **Viewing Expenses:**
   - Open `expenses.csv` in a spreadsheet or text editor.
   - Alternatively, the app can display recent expenses.
   
4. **Editing/Deleting an Expense:**
   - Modify `expenses.csv` manually or add functionality in `app.py`.
   
5. **Generating Reports:**
   - Future updates may include automated financial reports.

## File Structure
```
ExpenseTracker/
│── app.py                # Main application file
│── expenses.csv          # CSV file storing expense data
│── requirements.txt      # Dependencies
│── README.md             # Documentation
│── .git/                 # Git version control files
```

## Future Enhancements
- **Graphical User Interface (GUI)** for a more interactive experience.
- **Database Integration** to replace CSV storage.
- **Expense Filtering & Sorting** for better insights.
- **Authentication System** to allow multiple users.
- **Cloud Backup** for secure data storage.

## Contributing
If you would like to contribute, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

