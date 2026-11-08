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

def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    random_animation_ui = ui.RandomAnimationUI()
    random_animation_ui.show()
 
main()