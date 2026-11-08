import os
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
    QMessageBox

)

# import de librairie de base/classique
import os
import sys


# on a obtenu le folder dans lequel il y a notre fichier courant
# __file__ = le fichier courant
absolute_file_path = os.path.abspath(__file__)
absolute_folder_path = os.path.dirname(absolute_file_path)
print(absolute_folder_path) #C: \Users\sigaaya\repos\NAND403_A26_Ateliers\atelier_8
# ici on vient ajouter absolute_folder_path au path de python pour qu'il puisse trouver ui_atelier.py
sys.path.append(absolute_folder_path)

import importlib
import ui
importlib.reload(ui)

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
    

def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    random_animation_ui = ui.RandomAnimationUI()
    random_animation_ui.show()
 
main()
