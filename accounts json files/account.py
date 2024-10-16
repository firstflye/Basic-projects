# Program that prompts a user to input their information 
# The informatin is then saved and when the user needs to see their informaton they can  access it with their account number

import sys
import json
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit, QPushButton,QVBoxLayout, QMessageBox, QStackedWidget, QFormLayout, QHBoxLayout, QInputDialog)


class BankingSystem(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()

        self.create_home_page()
        self.create_sign_up_page()
        self.create_sign_in_page()

        self.stacked_widget.setCurrentWidget(self.home_page)

        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

        self.setWindowTitle("Account Creation System")
        self.resize(400, 300)

        self.file_path = "C:/Users/AMOS KIPCHIRCHIR/Desktop/vs code/py stuff/Pyfiles/userinfo.json"


    def create_home_page(self):
        self.home_page = QWidget()

        home_layout = QVBoxLayout()
        sign_up_button = QPushButton("Sign Up", self)
        sign_in_button = QPushButton("Sign In", self)

        # Connection buttons
        sign_up_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.sign_up_page))
        sign_in_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.sign_in_page))

        home_layout.addWidget(QLabel("Welcome User"))
        home_layout.addWidget(sign_in_button)
        home_layout.addWidget(sign_up_button)

        self.home_page.setLayout(home_layout)
        self.stacked_widget.addWidget(self.home_page)


    def create_sign_up_page(self):
        self.sign_up_page = QWidget()

        form_layout = QFormLayout()

        self.name_input = QLineEdit(self)
        self.account_input = QLineEdit(self)
        self.email_input = QLineEdit(self)

        form_layout.addRow("Name:", self.name_input)
        form_layout.addRow("Account Number:", self.account_input)
        form_layout.addRow("Email:", self.email_input)

        sign_up_button = QPushButton("Sign Up", self)
        sign_up_button.clicked.connect(self.sign_up)

        button_layout = QHBoxLayout()
        button_layout.addWidget(sign_up_button)

        # Back Button
        back_button = QPushButton("Back", self)
        back_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.home_page))

        button_layout = QHBoxLayout()
        button_layout.addWidget(sign_up_button)
        button_layout.addWidget(back_button)

        form_layout.addRow(button_layout)

        self.sign_up_page.setLayout(form_layout)
        self.stacked_widget.addWidget(self.sign_up_page)

    def sign_up(self):
        name = self.name_input.text()
        account_number = self.account_input.text()
        email = self.email_input.text()

        user_info = {"Name": name, "Account": account_number, "Email": email}

        try:
            # Load existing data
            with open(self.file_path, "r") as file:
                data = json.load(file)
                if not isinstance(data, list):
                    if isinstance(data, dict):
                        data = [data]
                    else:
                        raise ValueError("Data format is incorrect. Expected a list")
        
        except (FileNotFoundError,json.JSONDecodeError):
            # if file doesn't exist or is empty, start with an empty list
            data = []

        # Add user info
        data.append(user_info)

        # Write updated data
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

        QMessageBox.information(self, "Success", "Sign-up completed successfully!")
        self.stacked_widget.setCurrentWidget(self.home_page)
        
    def create_sign_in_page(self):
        self.sign_in_page = QWidget()


        form_layout = QFormLayout()

        self.login_account_input = QLineEdit(self)
        self.account_info = QLabel(self)

        form_layout.addRow("Account Number:", self.login_account_input)
        form_layout.addRow("Account information", self.account_info)

        sign_in_button = QPushButton("Sign In", self)
        sign_in_button.clicked.connect(self.sign_in)


        # Back button
        back_button = QPushButton("Back", self)
        back_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.home_page))
         
         # Button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(sign_in_button)
        button_layout.addWidget(back_button)

        form_layout.addRow(button_layout)



        self.sign_in_page.setLayout(form_layout)
        self.stacked_widget.addWidget(self.sign_in_page)

    def sign_in(self):
        entered_account = self.login_account_input.text()

        try:
            # Load data from file
            with open(self.file_path, "r") as file:
                data = json.load(file)

            # search for the user

            for user in data:
                if user["Account"] == entered_account:
                    info = f"Name: {user['Name']}\n Email: {user['Email']}"
                    self.account_info.setText(info)
                    return

            # If account not found
            self.account_info.setText("Account not found!")

        except FileNotFoundError:
            self.account_info.setText("No user data found!")



if __name__=="__main__":
    app = QApplication(sys.argv)
    banking_system = BankingSystem()
    banking_system.show()
    sys.exit(app.exec_())
