import sys
import json
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit, QPushButton,
                             QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox, QFileDialog)

class ChooseYourOwnAdventureGame(QWidget):
    def __init__(self):
        super().__init__()

        # Widgets for setting up the story creation
        self.story_label = QLabel("Enter the story text:", self)
        self.story_input = QLineEdit(self)
        self.option1_label = QLabel("Option 1:", self)
        self.option1_input = QLineEdit(self)
        self.option2_label = QLabel("Option 2:", self)
        self.option2_input = QLineEdit(self)
        self.add_story_button = QPushButton("Add Story", self)

        # Node selection
        self.node_selection_label = QLabel("Choose a node to continue:", self)
        self.node_selection_combo = QComboBox(self)
        self.node_selection_combo.addItem("start")

        # Save and Load buttons
        self.save_button = QPushButton("Save Story", self)
        self.load_button = QPushButton("Load Story", self)

        # Gameplay Widgets
        self.play_story_label = QLabel(self)
        self.option1_button = QPushButton("Option 1", self)
        self.option2_button = QPushButton("Option 2", self)
        self.play_button = QPushButton("Play", self)

        # Story structure
        self.story = {}
        self.current_node = "start"
        self.current_options = []

        # Hide gameplay elements until needed
        self.play_story_label.hide()
        self.option1_button.hide()
        self.option2_button.hide()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Choose your own adventure")

        vbox = QVBoxLayout()

        # Add widgets for story creation
        vbox.addWidget(self.story_label)
        vbox.addWidget(self.story_input)
        vbox.addWidget(self.option1_label)
        vbox.addWidget(self.option1_input)
        vbox.addWidget(self.option2_label)
        vbox.addWidget(self.option2_input)
        vbox.addWidget(self.node_selection_label)
        vbox.addWidget(self.node_selection_combo)
        vbox.addWidget(self.add_story_button)

        # Add save and load buttons
        vbox.addWidget(self.save_button)
        vbox.addWidget(self.load_button)

        # Gameplay layout
        vbox.addWidget(self.play_story_label)
        vbox.addWidget(self.option1_button)
        vbox.addWidget(self.option2_button)
        vbox.addWidget(self.play_button)

        self.setLayout(vbox)

        # Connect buttons to actions
        self.add_story_button.clicked.connect(self.add_story)
        self.play_button.clicked.connect(self.play_game)
        self.option1_button.clicked.connect(lambda: self.choose_option(0))
        self.option2_button.clicked.connect(lambda: self.choose_option(1))
        self.save_button.clicked.connect(self.save_story)
        self.load_button.clicked.connect(self.load_story)

    def add_story(self):
        # Get the main story text and the two options
        story_text = self.story_input.text()
        option1 = self.option1_input.text()
        option2 = self.option2_input.text()
        selected_node = self.node_selection_combo.currentText()

        if not story_text or not option1 or not option2:
            QMessageBox.warning(self, "Error", "Please fill in the story and both options.")
            return

        # Add this story node and its options to the story dictionary
        self.story[selected_node] = {
            "story": story_text,
            "options": [option1, option2]
        }

        # Add new options as nodes in the combo box
        self.node_selection_combo.addItem(f"{selected_node}-{option1}")
        self.node_selection_combo.addItem(f"{selected_node}-{option2}")

        # Clear the input fields
        self.story_input.clear()
        self.option1_input.clear()
        self.option2_input.clear()

        QMessageBox.information(self, "Story Added", "The story and options have been added!")

    def play_game(self):
        # Start the game with the root story
        self.current_node = "start"
        self.display_story()

        # Hide story creation elements and show gameplay elements
        self.story_label.hide()
        self.story_input.hide()
        self.option1_label.hide()
        self.option1_input.hide()
        self.option2_label.hide()
        self.option2_input.hide()
        self.add_story_button.hide()
        self.node_selection_label.hide()
        self.node_selection_combo.hide()
        self.save_button.hide()
        self.load_button.hide()
        self.play_button.hide()

        # Show the gameplay elements
        self.play_story_label.show()
        self.option1_button.show()
        self.option2_button.show()

    def display_story(self):
        # Display the story at the current node
        current_story = self.story.get(self.current_node, None)

        if current_story:
            # Display the story and options
            self.play_story_label.setText(current_story["story"])
            self.option1_button.setText(current_story["options"][0])
            self.option2_button.setText(current_story["options"][1])
            self.current_options = current_story["options"]
        else:
            # End of story
            self.play_story_label.setText("The end")
            self.option1_button.hide()
            self.option2_button.hide()

    def choose_option(self, option_index):
        # Move to the next story node based on the selected option
        if option_index < len(self.current_options):
            self.current_node = f"{self.current_node}-{self.current_options[option_index]}"
            self.display_story()

    def save_story(self):
        # Open a file dialog to save the story
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Story", "", "JSON Files (*.json)", options=options)
        if file_name:
            with open(file_name, 'w') as file:
                json.dump(self.story, file)
            QMessageBox.information(self, "Story Saved", "Your story has been saved successfully!")

    def load_story(self):
        # Open a file dialog to load a story
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Load Story", "", "JSON Files (*.json)", options=options)
        if file_name:
            with open(file_name, 'r') as file:
                self.story = json.load(file)

            # Populate node selection with the loaded nodes
            self.node_selection_combo.clear()
            self.node_selection_combo.addItems(self.story.keys())

            QMessageBox.information(self, "Story Loaded", "Your story has been loaded successfully!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    choose_your_own_adventure_game = ChooseYourOwnAdventureGame()
    choose_your_own_adventure_game.show()
    sys.exit(app.exec_())
