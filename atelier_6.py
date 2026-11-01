# Satisfait de votre dernier outil, le modélisateur vous fait maintenant confiance. 
# Il s'appelle Jason et vous annonce qu'il est le maire de la ville. Rassuré de s'être fait un ami, 
# il se confie un peu à vous. Certains bandits menacent de piller la ville. Pour se protéger, 
# et c'est pour cette raison qu'il veut redessiner la ville en commençant par l'ajout de défense. 
# Il vous demande encore de l'aide pour construire des clôtures. Étant un tech artist, 
# votre réflexe est, bien sûr, de faire un script dans Maya pour accélérer le processus.

import sys
import maya.cmds as cmds
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFileDialog, QDoubleSpinBox, QGridLayout, QPushButton


class MessageBoard(QWidget):

    def __init__(self): # Constructeur
        super().__init__()  # Constructeur QWidget

        self.create_ui()
        self.get_value
        
        
    def create_ui(self):
        layout = QGridLayout(self)
        self.setWindowTitle("Fence maker")   # Titre de la fenetre
        #spinbox = QDoubleSpinBox()
        #spinbox.setMinimum(-10)
        #spinbox.setMaximum(10)
        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.apply_changes)


        #spinbox.valueChanged.connect(self.value_changed)
        self.message = QtWidgets.QLineEdit()
        self.message.setFixedSize(200, 40)
        #self.layout.addWidget(self.message)

        #spinbox = QDoubleSpinBox()

        #spinbox.setMinimum(-10)
        #spinbox.setMaximum(10)
        #spinbox.setSingleStep(3)

        #spinbox.valueChanged.connect(self.value_changed)

        self.hauteur = QtWidgets.QLineEdit("")
        self.distanceMilieu = QtWidgets.QLineEdit("")
        self.largeur = QtWidgets.QLineEdit("")
        self.longueur = QtWidgets.QLineEdit("")

        self.hauteur.setFixedSize(100, 25)
        self.distanceMilieu.setFixedSize(100, 25)
        self.largeur.setFixedSize(100, 25)
        self.longueur.setFixedSize(100, 25)

        layout.addWidget(QLabel("Hauteur"), 1, 0)
        layout.addWidget(QLabel('Distance Milieu'), 5, 0)
        layout.addWidget(QLabel('Largeur'), 7, 0)
        layout.addWidget(QLabel('Longueur'), 9, 0)


        layout.addWidget(self.hauteur, 1, 1)
        layout.addWidget(self.distanceMilieu, 5, 1)
        layout.addWidget(self.largeur, 7, 1)
        layout.addWidget(self.longueur, 9, 1)

        layout.addWidget(self.create_button)
    

    def get_value(self, value):
        print(value)

        self.hauteur = float(self.hauteur.text())
        self.distance = float(self.distanceMilieu.text())
        self.largeur = float(self.largeur.text())
        self.longueur = float(self.longueur.text())


    # Fonction principale
    def apply_changes(self):

        # hauteur = self.hauteur.value()
        # distance = self.distanceMilieu.value()
        # largeur = self.largeur.value()
        # longueur = self.longueur.value()
        
        cmds.undoInfo(openChunk=True) # CTRL Z 
        
        try:
             #obj_value = int(self.obj.text())

             for i in range:

                poteauV = cmds.polyCube(name="fence_vertical", width=self.largeur, height=self.hauteur, depth=self.largeur)[0]

                for y in range:

                    poteauH = cmds.polyCube(name="fence_horizontal",width=self.longueur,height=self.largeur,depth=self.largeur)[0]


        finally:
            cmds.undoInfo(closeChunk=True) # CTRL Z


def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()
