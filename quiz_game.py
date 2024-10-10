# a game in which as user is asked a question
# if they  a player gets the answer the score is increased
# if they fail the score is reduced
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                            QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class Quizgame(QWidget):
    def __init__(self):
        super().__init__()

        #Widgetsfor setting up the question and answer
        self.setup_label = QLabel("Enter a question : ", self)
        self.question_label = QLabel("Enter your question: ", self)
        self.question_input = QLineEdit(self)
        self.answer_label = QLabel("Enter the correct answer: ", self)
        self.answer_input = QLineEdit(self)
        self.try_to_answer_button = QPushButton("Try to answer", self)

        #Widgets for Gameplay
        self.play_question_label = QLabel("", self) #Empty will show the question later
        self.guess_label = QLabel("Enter your guess: ", self)
        self.guess_input = QLineEdit(self)
        self.submit_guess_button = QPushButton("Submit Answer", self)
        self.score_label = QLabel("score: 0", self)
        self.score = 0
        self.correct_answer = "" #Hidden correct answer

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Quiz game")

        vbox =QVBoxLayout()

        vbox.addWidget(self.setup_label)
        vbox.addWidget(self.question_label)
        vbox.addWidget(self.question_input)
        vbox.addWidget(self.answer_label)
        vbox.addWidget(self.answer_input)
        vbox.addWidget(self.try_to_answer_button)

        # Gameplay UI (hidden until question is added)
        vbox.addWidget(self.play_question_label)
        vbox.addWidget(self.guess_label)
        vbox.addWidget(self.guess_input)
        vbox.addWidget(self.submit_guess_button)
        vbox.addWidget(self.score_label)

        self.setLayout(vbox)

        self.try_to_answer_button.clicked.connect(self.add_guess)
        self.submit_guess_button.clicked.connect(self.check_answer)

        self.play_question_label.hide()
        self.guess_label.hide()
        self.guess_input.hide()
        self.submit_guess_button.hide()

    def add_guess(self):

        question = self.question_input.text()
        answer = self.answer_input.text()

        if question and answer:
            self.correct_answer = answer

        self.play_question_label.setText(f"Question: {question} ")

        self.question_input.clear()
        self.answer_input.clear()

        self.setup_label.hide()
        self.question_label.hide()
        self.question_input.hide()
        self.answer_label.hide()
        self.answer_input.hide()
        self.try_to_answer_button.hide()

        self.play_question_label.show()
        self.guess_label.show()
        self.guess_input.show()
        self.submit_guess_button.show()

    def check_answer(self):
        guess = self.guess_input.text()

        if guess == self.correct_answer:
            self.score += 1
        else:
            self.score -= 1

        self.score_label.setText(f"Score: {self.score}")
        self.guess_input.clear()

if __name__=="__main__":
    app = QApplication(sys.argv)
    quiz_game = Quizgame()
    quiz_game.show()
    sys.exit(app.exec_())




