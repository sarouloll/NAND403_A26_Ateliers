from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QMessageBox
from PySide6 import QtWidgets

# # snake case
# this_is_a_snake_case_syntax

# # camel case
# thisIsACamelCaseSyntax

# # pascal case
# ThisIsAPascalCaseSyntax


class MessageBoard(QWidget):
    def __init__(self): # Constructeur
        super().__init__()  # Constructeur QWidget
        self.setWindowTitle("Message board")
        self.create_ui()

    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Message board")
        layout.addWidget(label)
        
        self.message = QtWidgets.QTextEdit()
        layout.addWidget(self.message)

        button = QtWidgets.QPushButton()
        layout.addWidget(button)
        button.setText("OK")

        button.clicked.connect(self.on_click)


    def on_click(self):
        print("on click called")
        message = self.message.toPlainText()
        QMessageBox.information (self, "message", message)
        
 
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()