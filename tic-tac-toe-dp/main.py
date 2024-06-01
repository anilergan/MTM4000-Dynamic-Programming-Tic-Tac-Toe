# Following code is to run the game in terminal (recommended)

# from play import play_tic_tac_toe 
# play_object = play_tic_tac_toe()
# play_object.play()


# Following code is to run the game in user interface (recommended)

from PyQt6.QtWidgets import QApplication
from game_gui import AppWindow
from sys import argv

app = QApplication(argv)

window = AppWindow()
window.show()

app.exec()