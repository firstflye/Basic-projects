#Number Guessing Game
#Generate a random number
#Track how long it will take the user to guess the number
#Each time providing the user with a hint if he is above or below the generated number

import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                            QLineEdit, QPushButton, QVBoxLayout)

class Numberguesser(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_label = QLabel(self)
        self.generate_random_num_button = QPushButton("Generate", self)
        self.guess_label = QLabel("Guess the number", self)
        self.guess_input = QLineEdit(self)
        self.submit_guess_button = QPushButton("Submit", self)
        self.number_of_tries = QLabel("Tries: 0",self)
        self.hint_label = QLabel(self)
        self.generated_num = None #Store the number
        self.tries = 0 #Track the number of tries

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Number Guesser")

        vbox = QVBoxLayout()

        vbox.addWidget(self.setup_label)
        vbox.addWidget(self.generate_random_num_button)
        vbox.addWidget(self.guess_label)
        vbox.addWidget(self.guess_input)
        vbox.addWidget(self.submit_guess_button)
        vbox.addWidget(self.number_of_tries)
        vbox.addWidget(self.hint_label)

        self.setLayout(vbox)

        self.generate_random_num_button.clicked.connect(self.generate_random_num)
        self.submit_guess_button.clicked.connect(self.check_num)


    def generate_random_num(self):
        self.generated_num = random.randint(0, 100)

        self.tries = 0 #Reset tries
        self.number_of_tries.setText("Tries: 0")
        self.hint_label.setText("")
        self.setup_label.setText("A new number has been generated! Start guessing.")
        self.guess_input.setText("") #Clear the input field



    def check_num(self):

        if self.generated_num is None:

            self.hint_label.setText("Please generate a number first!")
            return

        guess = self.guess_input.text()

        if guess.isdigit():
            guess = int(guess)
            self.tries +=1

            self.number_of_tries.setText(f"Tries: {self.tries}")

            if guess < self.generated_num:
                self.hint_label.setText("Too low!Try Again.")
            elif guess > self.generated_num:
                self.hint_label.setText("Too high!Try again.")
            else:
                self.hint_label.setText(f"Correct ! You have guessed the number in {self.tries} tries.")

        else:
            self.hint_label.setText("Please enter a valid number!")

if __name__=="__main__":
    app = QApplication(sys.argv)
    number_guesser = Numberguesser()
    number_guesser.show()
    sys.exit(app.exec_())