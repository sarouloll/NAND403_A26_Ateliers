from PySide6.QtWidgets import (
    QtWidgets,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
    QMessageBox

)

class RandomAnimationUI():
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Animation Tool")
        self.setMinimumWidth(400)
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout(self)
        title = QLabel("Message board")
        layout.addWidget(title)   

        global text_box
        text_box = QTextEdit()
        layout.addWidget(title)
        
        button = QPushButton("Send", self)
        layout.addWidget(button)
        button.setText("OK")
        
        button.clicked.connect(self.on_click)
        
        
    def on_click(self):
        message_box = QMessageBox.information (self, "message", text_box.toPlainText())
    


