# A game of rock paper scissors against the computer
# The number of times the player wins against the computer is recorded
# If the player loses three consecutive times against the computer, it results in a game loss
# Each Game lasts 30 seconds

import sys
import random
import time
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QHBoxLayout,
                             QPushButton, QVBoxLayout, QMessageBox)
from PyQt5.QtCore import QTimer

class rockpaperscissors(QWidget):
    def __init__(self):
        super().__init__()
        self.rps_art_label = QLabel(self)
        self.start_game_button = QPushButton("Start")
        self.rock_button = QPushButton("👊 Rock")
        self.paper_button = QPushButton("🤚 Paper")
        self.scissors_button = QPushButton("✌ Scissors")
        self.generated_sign = QLabel("computer's choice",self)
        self.score_label = QLabel("score: 0",self)
        self.score = 0
        self.state_label = QLabel(self)
        self.loss_count_label = QLabel("Loss count: ",self)
        self.loss_count = 0
        self.choices = ["👊", "🤚", "✌"]
        self.timer_label = QLabel("Time left: 6 seconds", self)
        self.game_timer = QTimer(self)
        self.game_timer.timeout.connect(self.update_timer)
        self.time_left = 6

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Rock Paper Scissors Game")

        vbox = QVBoxLayout()

        vbox.addWidget(self.rps_art_label)
        vbox.addWidget(self.start_game_button)
        vbox.addWidget(self.score_label)
        vbox.addWidget(self.generated_sign)
        vbox.addWidget(self.timer_label)
        vbox.addWidget(self.state_label)
        vbox.addWidget(self.loss_count_label)

        hbox = QHBoxLayout()

        vbox.addWidget(self.rock_button)
        vbox.addWidget(self.paper_button)
        vbox.addWidget(self.scissors_button)

        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.rock_button.setEnabled(False)
        self.paper_button.setEnabled(False)
        self.scissors_button.setEnabled(False)

        self.start_game_button.clicked.connect(self.play_game)
        self.rock_button.clicked.connect(lambda: self.player_choice("👊"))
        self.paper_button.clicked.connect(lambda: self.player_choice("🤚"))
        self.scissors_button.clicked.connect(lambda: self.player_choice("✌"))

    def play_game(self):
        self.reset_game()

        self.rock_button.setEnabled(True)
        self.paper_button.setEnabled(True)
        self.scissors_button.setEnabled(True)

        self.start_game_button.setEnabled(False)

        self.time_left = 30

        self.timer_label.setText(f"Time left: {self.time_left} seconds")
        self.game_timer.start(1000)

    def player_choice(self, player_choice):

        computer_choice = random.choice(self.choices)

        self.generated_sign.setText(f"Computer's choice: {computer_choice}")
        result = self.check_winner(player_choice, computer_choice)

        if result == "win":
            self.score += 1
            self.loss_count = 0
            self.state_label.setText("Win")

        elif result == "lose":
            self.loss_count += 1
            self.state_label.setText("lose")
        self.score_label.setText(f"Score: {self.score}")


        if self.loss_count == 3:
            self.end_game(game_lost = True)
        else:
            self.loss_count_label.setText(f"loss count: {self.loss_count}")

    def check_winner(self, player, computer):
        if player == computer:
            self.state_label.setText("tie")
            return "tie"
        elif (player == "👊" and computer == "✌") or (player == "🤚" and computer == "👊") or (player == "✌" and computer == "🤚"):
            return "win"
        else:
            return "lose"

    def reset_game(self):
        self.score = 0
        self.loss_count = 0

        self.score_label.setText(f"Score: {self.score}")
        self.generated_sign.setText("Computer's choice: ")

    def end_game(self, game_lost=False):
        self.game_timer.stop()
        self.rock_button.setEnabled(False)
        self.paper_button.setEnabled(False)
        self.scissors_button.setEnabled(False)

        self.start_game_button.setEnabled(True)

        if game_lost:
            QMessageBox.warning(self, "Game Over", "You have lost 3 times consecutively. Game over!")
        else:
            QMessageBox.information(self, "Time's up", "Game over! Final score: " + str(self.score))

    def update_timer(self):
        self.time_left -= 1
        if self.time_left == 0:
            self.end_game()

        self.timer_label.setText(f"Time left: {self.time_left} seconds")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    rock_paper_scissors = rockpaperscissors()
    rock_paper_scissors.show()
    sys.exit(app.exec_())
