# Personal Expense Tracker

## Overview

The **Personal Expense Tracker** is a simple command-line application that allows users to track their daily expenses, categorize them, and compare them against a monthly budget. The application supports saving and loading expenses from a CSV file, enabling users to continue tracking expenses even after closing the program. It provides an interactive menu-driven interface for ease of use.

### Features:
- Add daily expenses with date, category, amount, and description.
- View a list of all expenses.
- Set and track the monthly expense budget.
- Save and load expenses to/from a CSV file.
- Exit the program gracefully.

## Requirements

Before running the program, ensure you have the following installed:

- Python 3.x (preferably Python 3.6 or later)
- `tabulate` library for pretty-printing tables (install using `pip` if not already installed)

You can install the required library using pip:
```bash
pip install tabulate
```

## How to Run the Program
### Step 1: Clone or Download the Code
Clone the repository or download the Python file (expense_tracker.py) to your local machine.

```bash
git clone https://github.com/sdeepak001/Personal_Expense_Tracker.git

### step 2: Run the Python Script
The Run the following command:

```bash
    python expense_tracker.py
```
This will start the program and display the interactive menu for you to manage your expenses.

### Step 3: Using the Program
The program will display a menu with the following options:

1. Add Expense: Add a new expense entry with the date, category, amount, and description.
2. View Expense: View all recorded expenses in a tabular format.
3. Track Expense: Track your expenses against the set monthly budget. You can set or update the monthly budget and check if you've exceeded it.
4. Save Expense: Save all recorded expenses to a CSV file.
5. Load Expense: Load expenses from a CSV file (useful for resuming previous sessions).
6. Exit: Exit the application.

Choose an option by entering the corresponding number (1-6). The program will guide you through each option with prompts.

#### Example Workflow:
1. Add some expenses with their details (date, category, amount, and description).
2. View the expenses to check your entries.
3. Set a monthly budget and track your expenses to see if you are within the budget.
4. Save your expenses to a CSV file for later reference.
5. Load expenses from the CSV file when you reopen the program to continue from where you left off.
6. File Format for CSV (Save/Load)

The CSV file is structured with the following columns:
```
Date,Category,Amount,Description
```
Each row represents an individual expense record. The first row in the CSV file contains the headers, and subsequent rows contain the actual expense data.

Example:
```
Date,Category,Amount,Description
2025-01-01,Food,20.50,Lunch at restaurant
2025-01-02,Travel,50.00,Taxi fare
```

## Notes
The date format in the application is YYYY-MM-DD, so ensure that you input dates in this format when adding or loading expenses.
The program will prompt for user input and validate the data to ensure it is correct (e.g., the correct date format, valid amount).
The expenses will be stored in memory during the session. If you want to keep the data, make sure to save it before exiting the program.
Exit
You can gracefully exit the program at any time by selecting the Exit option from the menu, or by pressing Ctrl+C to trigger the exit handler.

License
This project is licensed under the Apache License, Version 2.0. See the LICENSE file for details.

Author
Deepak Soma Reddy
Email: sdeepak001@gmail.com
