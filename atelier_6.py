# Satisfait de votre dernier outil, le modélisateur vous fait maintenant confiance. 
# Il s'appelle Jason et vous annonce qu'il est le maire de la ville. Rassuré de s'être fait un ami, 
# il se confie un peu à vous. Certains bandits menacent de piller la ville. Pour se protéger, 
# et c'est pour cette raison qu'il veut redessiner la ville en commençant par l'ajout de défense. 
# Il vous demande encore de l'aide pour construire des clôtures. Étant un tech artist, 
# votre réflexe est, bien sûr, de faire un script dans Maya pour accélérer le processus.

import sys
import json
import maya.cmds as cmds
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFileDialog


class MessageBoard(QWidget):


    def __init__(self): # Constructeur
        super().__init__()  # Constructeur QWidget
        self.data = None

        self.setWindowTitle("Outliner Organiser")   # Titre de la fenetre

        #Items à ajouter à la fenetre
        # self.create_ui()
        # self.create_json_find()
        # self.create_checkbox()
        # self.button()

        
    def create_ui(self):
        # Création de l'interface principale
        self.layout = QVBoxLayout(self)
        # label = QLabel("Enter JSON path")
        # self.layout.addWidget(label)

        self.message = QtWidgets.QLineEdit()
        self.message.setFixedSize(400, 40)
        self.layout.addWidget(self.message)


    # Configuration du bouton principal
    def button(self):
        button = QtWidgets.QPushButton()
        self.layout.addWidget(button)
        button.setText("APPLY")

        # Relie bouton d'execution avec la fonction
        button.clicked.connect(self.verify_checkbox)

     
    # def create_checkbox(self):
    #     # Nom et configuration des checkbox
    #     self.checkbox_selected = QtWidgets.QCheckBox("Apply on selected only")
    #     self.checkbox_color = QtWidgets.QCheckBox("Apply colors")
    #     self.checkbox_reorder = QtWidgets.QCheckBox("Apply reorder")

    #     # Ajoute les checkbox dans l'interface
    #     self.layout.addWidget(self.checkbox_selected)
    #     self.layout.addWidget(self.checkbox_color)
    #     self.layout.addWidget(self.checkbox_reorder)


    # Fonction principale
    def apply_changes(self):
        cmds.undoInfo(openChunk=True) # CTRL Z 
        
        try:
            # Activation de la sélection
            if self.checkbox_selected.isChecked():
                objects = cmds.ls("SM_*", "FX_*", "LGT_*", selection=True)

            else:
                objects = cmds.ls("SM_*", "FX_*", "LGT_*")

            #Main logic de couleurs
            if self.checkbox_color.isChecked():
                prefix = self.data

                for obj in objects:

                    for prefix, rgb in self.data.items():

                        if obj.startswith(prefix):
                            cmds.setAttr(obj + ".useOutlinerColor", 1)
                            cmds.setAttr(obj + ".outlinerColor", rgb[0], rgb[1], rgb[2], type="double3")

            # Logique de reorganisation
            if self.checkbox_reorder.isChecked():
                objects = sorted(objects)
            
                for obj in reversed(objects):
                    cmds.reorder(obj, front=True) 

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
