# Copyright (C) ${2025} ${Deepak Soma Reddy} (${sdeepak001@gmail.com})

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import signal
import datetime
from tabulate import tabulate


class Expense:
    '''This class will store the expense of the user'''

    def __init__(self):
        # list store the expense
        self.__expense = []
        self.__montly_budget = 0

    # Check if the date is in correct format
    def __validate_date(self, date):
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please enter date in yyyy-mm-dd format.")
            return False
        return True

    # Add expense to the list
    def __add_expense(self):
        print("\nAdd Expense:")
        expense = Expense()
        date = input("Enter date (yyyy-mm-dd): ")
        if not self.__validate_date(date):
            return

        category = input("Enter category: ")
        if category == "":
            print("Category cannot be empty. Please enter a valid category.")
            return
        
        amount = input("Enter amount(rs): ")
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount. Please enter a valid amount.")
            return
        
        description = input("Enter description: ")
        if description == "":
            print("Description cannot be empty. Please enter a valid description.")
            return
        
        self.__expense.append({"Date": date, "Category": category, "Amount": amount, "Description": description})

        print("Expense added successfully.\n")

    # View the expense list
    def __view_expense(self):
        print("\nView Expense:")
        if not self.__expense and len(self.__expense) == 0:
            print("No expense to save.")
            return
        
        print(tabulate(self.__expense, headers='keys', tablefmt="grid"))

    # Add the monthly budget
    def __add_track_expense(self) -> int:
        budget = 0
        while True:
            budget = input("Enter Monthly Expense budget:")
            try:
                budget = float(budget)
                break
            except ValueError:
                print("Invalid budget. Please enter a valid budget.")
        return budget
    
    # Calculate the total expense
    def __calculate_total_expense(self):
        total_expense = 0
        for expense in self.__expense:
            total_expense += expense["Amount"]
        return total_expense

    # Track the expense
    def __track_expense(self):
        print("\nTrack Expense")
        if not self.__montly_budget:
            self.__montly_budget = self.__add_track_expense()
        else:
            print(f"Specified Monthly Expense budget: {self.__montly_budget}. Do you want to update?")
            choice = input("Enter 'Y' to update or any key to continue:")
            if choice.lower() == "y":
                self.__montly_budget = self.__add_track_expense()
        
        total_expense = self.__calculate_total_expense()
        print(f"Total Expense: {total_expense}")
        if total_expense > self.__montly_budget:
            print("**You have exceeded the budget.**")
        else:
            print("**You have %s left in your budget.**" % (self.__montly_budget - total_expense))

    # Save the expense to a file
    def __save_expense(self):
        print("\nSave Expense")
        if not self.__expense and len(self.__expense) == 0:
            print("No expense to save.")
            return
        csv_file = input("Enter file name to save: ")
        if not csv_file:
            print("File name cannot be empty. Please enter a valid file name.")
            return
        with open(csv_file, "w") as file:
            file.write(",".join(self.__expense[0].keys()) + "\n")
            for expense in self.__expense:
                file.write(f"{expense['Date']},{expense['Category']},{expense['Amount']},{expense['Description']}\n")
        print("Expense saved successfully.\n")
        pass

    # Load the expense from a file
    def __load_expense(self):
        print("\nLoad Expense")
        csv_file = input("Enter file name to load: ")
        if not csv_file:
            print("File name cannot be empty. Please enter a valid file name.")
            return
        if not os.path.exists(csv_file):
            print("File not found. Please enter a valid file name.")
            return
        try:
            with open(csv_file, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) != 4:
                        print("Invalid data found in file. Please enter a valid file.")
                        return
                    
                    if data[0].strip() == "Date" and data[1].strip() == "Category" and data[2].strip() == "Amount" and data[3].strip() == "Description":
                        continue


                    if not self.__validate_date(data[0]):
                        return
                    
                    if data[1] == "":
                        print("Category cannot be empty. Please enter a valid category.")
                        return

                    if not data[2].isdigit() and data[2].isdecimal():
                        print("Invalid amount found in file. Please enter a valid file.")
                        return
                    
                    if data[3] == "":
                        print("Description cannot be empty. Please enter a valid description.")
                        return
                    
                    self.__expense.append({"Date": data[0], "Category": data[1], "Amount": float(data[2]), "Description": data[3]})

        except Exception as e:
            print(f"An error occurred while loading the expense: {e}")
            return
        
        print("Expense loaded successfully.\n")

    # Exit the program
    def __exit(self):
        sys.exit()

    # Manage the expense
    def manage_expense(self, choice):
        if choice == 1:
            self.__add_expense()
        elif choice == 2:
            self.__view_expense()
        elif choice == 3:
            self.__track_expense()
        elif choice == 4:
            self.__save_expense()
        elif choice == 5:
            self.__load_expense()
        elif choice == 6:
            print("Thank you for using Expense Tracker")
            self.__exit()
        else:
            print("Invalid choice. Please enter a valid choice.")

    # Display the menu
    def menu_expense(self):
        while True:
            print("Welcome to Expense Tracker:")
            print("1. Add Expense")
            print("2. View Expense")
            print("3. Track Expense")
            print("4. Save Expense")
            print("5. Load Expense")
            print("6. Exit")
            choice = input("Please enter your choice between 1-6: ")

            if choice in ["1", "2", "3", "4", "5", "6"]:
                return int(choice)
            else:
                input("Invalid choice. Please enter a valid choice. press any key to continue to retry...")
                os.system("clear")

# Handle the signal
def signal_handler(sig, frame):
    print("\nThank you for using Expense Tracker")
    sys.exit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    # Create an instance of Expense class
    expense = Expense()

    # Display the menu
    while True:
        choice = expense.menu_expense()
        expense.manage_expense(choice)
        input("\npress any key to continue...")