import numpy as np

import sys
sys.path.append("tic-tac-toe-dp//gui")
from xox import Ui_MainWindow
import resources_rc

# Game Dynamis
from play import play_tic_tac_toe as PlayTicTacToe

# User Interface Libs (PyQt6)
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt6.QtGui import QPixmap, QIcon





class AppWindow(QMainWindow, PlayTicTacToe):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # SIGNAL-SLOTS ------------------------

        # Login Page Buttons
        self.ui.button_spm.clicked.connect(self.func_button_spm)
        self.ui.button_easy_mode.clicked.connect(lambda: self.play_against_computer(self.func_button_easy_mode, 'easy_mode'))

        self.ui.button_hard_mode.clicked.connect(self.func_button_hard_mode)
        # ------------------- Hard Mode Selection -------------------
        self.ui.button_hms_back.clicked.connect(self.func_button_hms_back)
        self.ui.button_hms_PI.clicked.connect(lambda: self.play_against_computer(self.func_button_hard_mode_section, 'policy_iteration'))
        self.ui.button_hms_VI.clicked.connect(lambda: self.play_against_computer(self.func_button_hard_mode_section, 'value_iteration'))
        self.ui.button_exit.clicked.connect(self.func_button_exit)

        # ------------------- Game Page Buttons -------------------
        self.ui.button_menu.clicked.connect(self.func_button_menu)
        self.ui.button_reset.clicked.connect(self.func_button_reset)

        # ------------------- Game Cells -------------------
        self.ui.mark_11.clicked.connect(lambda: self.func_mark('11'))
        self.ui.mark_12.clicked.connect(lambda: self.func_mark('12'))
        self.ui.mark_13.clicked.connect(lambda: self.func_mark('13'))
        self.ui.mark_21.clicked.connect(lambda: self.func_mark('21'))
        self.ui.mark_22.clicked.connect(lambda: self.func_mark('22'))
        self.ui.mark_23.clicked.connect(lambda: self.func_mark('23'))
        self.ui.mark_31.clicked.connect(lambda: self.func_mark('31'))
        self.ui.mark_32.clicked.connect(lambda: self.func_mark('32'))
        self.ui.mark_33.clicked.connect(lambda: self.func_mark('33'))

        # Game Values
        def update_cell_values(self):
            pass



        # --------------------------------------


        self.init_page()

    
    def init_page(self):
        self.ui.stackedwidget_content.setCurrentIndex(0)

    # SİGNAL SLOTS -----------------------------
    
    # Login Page Buttons Functions
        
    def func_button_spm(self): 
        # 1) reset game matrix
        
        self.mode = 'spm'

        self.agent = PlayTicTacToe()

        # 2) Reset game page
        self.reset_game_page()

        self.move_turn = 0
        
        # 3) Go to game page
        self.ui.stackedwidget_content.setCurrentIndex(1)                 

        
    def play_against_computer(self, func, mode):

        if not self.check_mark_selection():
            self.mark_selection_warning(undo = False)
            return
        

        self.user_mark = self.check_mark_selection()


        if self.user_mark == 1: self.agent_mark = 2
        if self.user_mark == 2: self.agent_mark = 1

        self.mark_list = ['x', 'o']

        self.ui.stackedwidget_content.setCurrentIndex(1)


        PlayTicTacToe.__init__(self)
        
        self.reset_game_page()

        func(mode)
        

    def func_button_easy_mode(self, mode):

        self.mode = mode
        
        from play_with_naive_agent import naive_agent as NaiveAgent
        self.agent = NaiveAgent()

        if self.user_mark == 2: self.agent_plays()
        

    def func_button_hard_mode(self):
        if not self.check_mark_selection():
            self.mark_selection_warning(undo = False)
            return
        
        self.ui.stackedwidget_pac.setCurrentIndex(1)

    def func_button_hms_back(self):
        self.ui.stackedwidget_pac.setCurrentIndex(0)


    def func_button_hard_mode_section(self, mode):

        self.mode = mode

        from play_with_the_master import the_master as TheMaster
        self.agent = TheMaster(dp_method=self.mode)

        if self.user_mark == 2: self.agent_plays() 


    
    def func_button_exit(self): 
        QApplication.quit()

    # Game Page Buttons Functions

    def func_button_menu(self):
        self.reset_game_page()
        self.mark_selection_warning(undo = True)
        self.ui.stackedwidget_pac.setCurrentIndex(0)
        self.ui.stackedwidget_content.setCurrentIndex(0)

    
    def func_button_reset(self): 
        if self.mode == 'spm':
            self.func_button_spm()

        elif self.mode == 'easy_mode':
            self.play_against_computer(self.func_button_easy_mode)

        elif self.mode == 'policy_iteration' or self.mode == 'value_iteration':
            self.play_against_computer(self.func_button_hard_mode_section, self.mode)
        


    
    # Support Functions -----------------------

    def mark_selection_warning(self, undo):
        if not undo:
            self.ui.frame_mark_selection.setStyleSheet(
            "#frame_mark_selection{"
"border: 3px dashed rgb(233,20,76);"
"background-color: rgba(233,20,76, 50);"
"border-radius: 25px; "
"}"

"QLabel{"
"""font: 700 14pt "Arial";"""
"color: rgb(233,20,76);"
"padding: 0 0 0 5;"

"}"

"QRadioButton {"
"width: 48px;"
"height: 48px;"
"border-radius: 25px;"
"border: 1px solid rgb(233,20,76);"
"}"


"QRadioButton::hover {"
"border: 1px solid rgba(20,124,236, 50);"
"background-color: rgba(20,124,236, 25)"
"}"

"QRadioButton::indicator {"
"width: 48px; "
"height: 48px; "
"border: None;"
"}"
        )
            
        else: 
            self.ui.frame_mark_selection.setStyleSheet(
            #frame_mark_selection{
"border: 2px solid rgb(215, 219, 221);"
"background-color: rgb(215, 219, 221);"
"border-radius: 25px; "
"}"
"QLabel{"
"""font: 14pt "Arial";"""
"color: rgba(12,16,25);"
"padding: 0 0 0 5;"

"}"

"QRadioButton {"
"width: 48px;"
"height: 48px;"
"border-radius: 25px;"
"border: 1px solid rgb(202, 207, 210);"
"}"


"QRadioButton::hover {"
"border: 1px solid rgba(20,124,236, 50);"
"background-color: rgba(20,124,236, 25)"
"}"

"QRadioButton::indicator {"
"width: 48px; "
"height: 48px; "
"border: None;"
"}"
            )

    def check_mark_selection(self): 
        if self.ui.radio_button_x.isChecked() or self.ui.radio_button_o.isChecked(): 
            if self.ui.radio_button_x.isChecked(): mark_selection = 1
            elif self.ui.radio_button_o.isChecked(): mark_selection = 2
            return mark_selection

    def reset_game_page(self): 
        self.ui.winner_mark.clear()
        self.ui.crown.clear()
        self.ui.frame_winner_announce.setStyleSheet("")
        self.ui.draw.setText("")

        for button in self.ui.frame_game.findChildren(QPushButton):
            button.setIcon(QIcon()) 
            button.setStyleSheet("")
        
        for row in range(3):
                for col in range(3):
                    coo = str(row + 1) + str(col + 1)
                    cell = self.findChild(QLabel, f"value_cell_{coo}")
                    cell.setText("")
                        



    def win_cells(self):
        board = self.agent.game_matrix
        win_cells_items = None
        for mark in [1,2]:
            for i in range(3):
                try: 
                    if np.array_equal(board[i], np.full(3, mark)): 
                        win_cells_items =  'Horizontal', i, mark
                        break
                    elif np.array_equal(board.T[i], np.full(3, mark)): 
                        win_cells_items = 'Vertical', i, mark
                        break
                except: print(board)

            if np.array_equal(np.diag(board), np.full(3, mark)): 
                win_cells_items = 'Diagonal', 0, mark
                break
            elif np.array_equal(np.diag(np.fliplr(board)), np.full(3, mark)): 
                win_cells_items = 'Diagonal', 1, mark
                break

            if win_cells_items: break
        

        if not win_cells_items: return
        
        elif win_cells_items[0] == 'Horizontal': 
            return [f'{i+1}1', f'{i+1}2', f'{i+1}3'], mark
        
        elif win_cells_items[0] == 'Vertical': 
            return [f'1{i+1}', f'2{i+1}', f'3{i+1}'], mark
        
        elif win_cells_items[0] == 'Diagonal' and win_cells_items[1] == 0: 
            return [f'11', f'22', f'33'], mark
        
        elif win_cells_items[0] == 'Diagonal' and win_cells_items[1] == 1: 
            return [f'31', f'22', f'13'], mark
        
        
    def edit_win_cells(self, coordinates, mark):
        coordinates = [int(x) for x in coordinates]
        for coo in coordinates:
            cell_button = self.findChild(QPushButton, f"mark_{coo}")
            cell_button.setStyleSheet(
    "QPushButton {\n"
     "   background-color: rgba(233,20,76,55);\n"
    "}"
        )
            icon = QIcon(f":/icons/{mark}_red.png")
            cell_button.setIcon(icon)
    


    def announce_winner(self, mark):
        pixmap = QPixmap(f':/icons/{mark}_crown.png')
        self.ui.winner_mark.setPixmap(pixmap)

        pixmap = QPixmap(':/icons/crown.png')
        self.ui.crown.setPixmap(pixmap)

        self.ui.frame_winner_announce.setStyleSheet(
    "#frame_winner_announce {\n"
     "   background-color: rgba(255,183,67,55);\n"
     "border: 1px solid rgba(255,183,67,255);\n"
     "border-radius: 15px"
    "}"
        )
        # rgba(255,183,67,255)



    # Game Dynamics
    def func_mark(self, cell, agent=None):

        def leave_mark(mark):
            cell_button = self.findChild(QPushButton, f"mark_{cell}")
            icon = QIcon(f":/icons/{mark}.png")
            cell_button.setIcon(icon)

        
        def win_func(): 
                    win_cells_coordinate_list, mark = self.win_cells()
                    
                    if mark == 1: mark = 'x'
                    elif mark == 2: mark = 'o'
        
                    self.edit_win_cells(win_cells_coordinate_list, mark)
                    self.announce_winner(mark)


        def draw_check():
            if self.agent.game_matrix.flatten().tolist().count(0) == 0:
                self.ui.draw.setText('Draw')
                self.ui.frame_winner_announce.setStyleSheet(
                "#frame_winner_announce {\n"
                "   background-color: rgba(255,183,67,55);\n"
                "border: 1px solid rgba(255,183,67,255);\n"
                "border-radius: 15px"
                "}")
                return True
            

        def display_action_values():
            cell_values = self.agent.action_values_dic[tuple(self.old_board.flatten())]

            if not cell_values: 
                Exception('Value is not valid by the state:\n', self.old_board)
            

            order = 0
            for row in range(3):
                for col in range(3):
                    coo = str(row + 1) + str(col + 1)
                    cell = self.findChild(QLabel, f"value_cell_{coo}")
                    if self.old_board[row, col] == 0:
                        cell.setText(str(round(cell_values[order], 2)))
                        order += 1
                    else: 
                        cell.setText("")
                    


    
        # If attemt to clicked a button which is marked do nothing.
        row, col = list(cell)
        row, col = int(row), int(col)

        if not self.mode == 'spm':

            if not agent: # This means func_mark called by USER
                if self.agent.game_matrix[row-1, col-1]: return
                self.agent.game_matrix[row-1, col-1] = self.user_mark

                if super().win(board=self.agent.game_matrix):
                    win_func()
                    return
                
                mark = self.mark_list[self.user_mark-1]
                leave_mark(mark)

                if draw_check(): 
                    return
                
                # Let agent moves 
                self.agent_plays()
            
            else:

                object_name = type(self.agent).__name__
                if object_name == "the_master":
                    display_action_values()

                if super().win(board=self.agent.game_matrix): 
                    win_func()
                    return
                
                mark = self.mark_list[self.agent_mark-1]
                leave_mark(mark)

                if draw_check(): 
                    return

                

        else: 

            turn = super().which_player(self.move_turn)

            if self.agent.game_matrix[row-1, col-1]: return
            self.agent.game_matrix[row-1, col-1] = turn + 1

            print()

            if super().win(board=self.agent.game_matrix): 
                win_func()
                return
            
            if turn == 0: mark = 'x'
            elif turn == 1: mark = 'o'
            leave_mark(mark)

            if draw_check(): 
                return

            self.move_turn += 1


    def agent_plays(self):
           
        self.old_board = self.agent.game_matrix.copy()
        self.agent.agent_move(self.agent_mark - 1) #It represent turn of agent, if self.agent_mark == 1 it means agent plays x and turn must be 0 and vice versa.
        new_board = self.agent.game_matrix.copy()
        
        cell_coordinate = np.where(new_board!=self.old_board)
        row, col = cell_coordinate
        
        # we added 1 to coordinates becouse game matrix index starts in zero to two but board cell's name starts in one to three 
        self.func_mark((str(int(row) + 1) + str(int(col) + 1)), self.agent)
            
            


app = QApplication(sys.argv)

window = AppWindow()
window.show()

app.exec()