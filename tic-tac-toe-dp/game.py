import numpy as np

class tic_tac_toe:
    def __init__(self):
        self.game_on = True
        
        self.game_matrix = np.array([[0,0,0], [0,0,0], [0,0,0]])

        self.dic_board_cells = {
            'c11': ' ', 'c12': ' ', 'c13': ' ',
            'c21': ' ', 'c22': ' ', 'c23': ' ',
            'c31': ' ', 'c32': ' ', 'c33': ' '
        }

        self.update_game_board()

        print("Welcome to Anil Ergan's Tic-Tac-Toe Game!")
    


    def board_move_tutor(self):
        print("\n 11 | 12 | 13 \n-----------\n 21 | 22 | 23 \n-----------\n 31 | 32 | 33 \n")



    def update_game_board(self):
        self.game_board = f"\n {self.dic_board_cells['c11']} | {self.dic_board_cells['c12']} | {self.dic_board_cells['c13']} \n-----------\n {self.dic_board_cells['c21']} | {self.dic_board_cells['c22']} | {self.dic_board_cells['c23']} \n-----------\n {self.dic_board_cells['c31']} | {self.dic_board_cells['c32']} | {self.dic_board_cells['c33']} \n"


    def display_board(self):
        print(self.game_board)
    
        
    def edit_game_board(self):

        for row in range(1,4):
            for col in range(1,4):
                cell = self.game_matrix[row-1,col-1]
                if cell == 0: continue
                elif cell == 1: 
                    cell_pointer = 'c'+str(row)+str(col)
                    self.dic_board_cells[cell_pointer] = 'X'
                    self.update_game_board()
                elif cell == 2:
                    cell_pointer = 'c'+str(row)+str(col)
                    self.dic_board_cells[cell_pointer] = 'O'
                    self.update_game_board()
    


    def get_game_on(self):
        return self.game_on
    
    def get_game_matrix(self):
        return self.game_matrix
    
    def end_the_game(self):
        self.game_on = False

