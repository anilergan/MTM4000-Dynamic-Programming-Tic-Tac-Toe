import sys
sys.path.append("tic-tac-toe-dp//gui")

from xox import Ui_MainWindow
import resources_rc

# Game Dynamis
from play_with_the_master import the_master
from play_with_naive_agent import naive_agent
from play_one_player import self_play

# User Interface Libs (PyQt6)
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator



class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # SIGNAL-SLOTS ------------------------

        # Login Page Buttons
        self.ui.button_spm.clicked.connect(self.func_button_spm)
        self.ui.button_easy_mode(self.func_button_easy_mode)
        self.ui.button_hard_mode(self.func_button_hard_mode)
        self.ui.button_exit(self.func_button_exit)

        # Game Page Buttons
        self.ui.button_menu(self.func_button_menu)
        self.ui.button_reset(self.func_button_reset)



        # --------------------------------------

        # QStackedWidget's Pages
        self.page_login_index = 0
        self.page_game_index = 1


        self.init_page()

    
    def init_page(self):
        self.ui.stackedwidget_content.setCurrentIndex(self.page_login_index)

    # SİGNAL SLOTS -----------------------------
    
    # Login Page Buttons Functions
        
    def func_button_spm(self): pass
    # 1) reset game matrix
    # 2) go to game page
    # 3) activate self-play dynamics
        

    @check_mark_selection
    def func_button_easy_mode(self, func): pass


    @check_mark_selection
    def func_button_hard_mode(self, func): pass

    
    def func_button_exit(self): pass 

    # Game Page Buttons Functions

    def func_button_menu(self): pass

    
    def func_button_reset(self): pass   


    # ---------------------------------------- 

    
    # Support Function -----------------------
    def check_mark_selection(self): 
        def wrapper(self):
            pass

        return wrapper
        

    # GAME DYNAMICS --------------------------

    def init_board(self):


    def play_x(self)



app = QApplication(sys.argv)

window = AppWindow()
window.show()

app.exec()