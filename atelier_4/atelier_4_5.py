import random
from maya import cmds
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QGridLayout,
    QLabel,
    
)

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setMinimumWidth(400)
        self.setMinimumHeight(250)
        self.build_ui()
    
    def build_ui(self):
        layout = QGridLayout(self)

        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)

        # Nom et configuration des zones de textes
        
        self.obj = QtWidgets.QLineEdit("")
        self.posX = QtWidgets.QLineEdit("")
        self.posY = QtWidgets.QLineEdit("")
        self.posZ = QtWidgets.QLineEdit("")
        self.scale = QtWidgets.QLineEdit("")

        self.posX_max = QtWidgets.QLineEdit("")
        self.posY_max = QtWidgets.QLineEdit("")
        self.posZ_max = QtWidgets.QLineEdit("")
        self.scale_max = QtWidgets.QLineEdit("")

        self.obj.setFixedSize(100, 25)
        self.posX.setFixedSize(100, 25)
        self.posY.setFixedSize(100, 25)
        self.posZ.setFixedSize(100, 25)
        self.scale.setFixedSize(100, 25)

        self.posX_max.setFixedSize(100, 25)
        self.posY_max.setFixedSize(100, 25)
        self.posZ_max.setFixedSize(100, 25)
        self.scale_max.setFixedSize(100, 25)
        

        layout.addWidget(QLabel("Nombre d'objets"), 1, 0)
        layout.addWidget(QLabel('Position x'), 5, 0)
        layout.addWidget(QLabel('Position Y'), 7, 0)
        layout.addWidget(QLabel('Position Z'), 9, 0)
        layout.addWidget(QLabel('Scale'), 11, 0)
        layout.addWidget(QLabel('min'), 3, 1)
        layout.addWidget(QLabel('max'), 3, 2)

        layout.addWidget(self.obj, 1, 1)
        layout.addWidget(self.posX, 5, 1)
        layout.addWidget(self.posY, 7, 1)
        layout.addWidget(self.posZ, 9, 1)
        layout.addWidget(self.scale, 11, 1)

        layout.addWidget(self.posX_max, 5, 2)
        layout.addWidget(self.posY_max, 7, 2)
        layout.addWidget(self.posZ_max, 9, 2)
        layout.addWidget(self.scale_max, 11, 2)

        layout.addWidget(self.create_button)

    def get_values(self):

        
        self.posX = float(self.posX.text())
        self.posY = float(self.posY.text())
        self.posZ = float(self.posZ.text())
        self.scale = float(self.scale.text())

        self.posX_max = float(self.posX.text())
        self.posY_max = float(self.posY.text())
        self.posZ_max = float(self.posZ.text())
        self.scale_max = float(self.scale.text())
    
    def create_object(self):
        forme = random.choice(["cube", "cylindre", "sphere"])
        self.obj = int(self.obj.text())
        
        for i in range(self.obj):
            
            if forme == "cube":
                objet = cmds.polyCube()[0]
                
            elif forme == "cylindre":
                objet = cmds.polyCylinder()[0]

            else:
                objet = cmds.polySphere()[0]

         
            random_value_X = random.uniform(float(self.posX())), (float(self.posX_max()))
            random_value_Y = random.uniform(float(self.posY())), (float(self.posY_max()))
            random_value_Z = random.uniform(float(self.posZ())), (float(self.posZ_max()))
            random_value_s = random.uniform(float(self.scale())), (float(self.scale_max()))

            cmds.move(random_value_X, random_value_Y, random_value_Z, objet)
            cmds.scale(self.scale, self.scale_max, objet)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()

# https://www.pythonguis.com/tutorials/pyside6-widgets/