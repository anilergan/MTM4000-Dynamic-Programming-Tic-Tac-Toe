from play import play_tic_tac_toe
import numpy as np

class computer(play_tic_tac_toe):

    def __init__(self):
        super().__init__()

            
    def play_game_as_x(self, agent_move_function):

        self.agent_move_function = agent_move_function
        while super().get_game_on() == True: 
            
            turn = super().which_player(self.move_turn) #if 0 it's first player if 1 it's second player

            if turn == 0:
                self.user_move('X', turn)
            elif turn == 1: 
                self.agent_move_function(turn)
            
            self.move_turn = super().is_game_going_on(self.move_turn)
            if not self.move_turn: break
            

    def play_game_as_o(self, agent_move_function):
        
        self.agent_move_function = agent_move_function
        while super().get_game_on() == True:
            

            turn = super().which_player(self.move_turn) #if 0 it's first player if 1 it's second player 

            if turn == 0:
                self.agent_move_function(turn)
            elif turn == 1: 
                self.user_move('O', turn)
            
            self.move_turn = super().is_game_going_on(self.move_turn)
            if not self.move_turn: break



    def user_move(self, mark, turn):
        
        move_coordinate = input('Move {}: '.format(mark))
        move_coordinate = self.check_input(move_coordinate)
        if not move_coordinate: 
            self.user_move(mark, turn)
            return
        
        move_row = int(str(move_coordinate)[0]) - 1
        move_col = int(str(move_coordinate)[1]) - 1

        if (self.game_matrix[move_row, move_col] != 0):
            print('Please leave a mark in an empty cell')
            self.user_move(mark, turn)
            return
        
        self.game_matrix[move_row, move_col] = turn + 1 



    def empty_cells_in_board(self):
        empty_cells_list = []
        for row in range(3):
            for col in range(3):
                mark_value = self.game_matrix[row,col] 
                if mark_value == 0: empty_cells_list.append([row,col])
        return empty_cells_list


    def inception_mark_selection(self):
        while True:
            im = input('Select inception mark (x/o): ')
            check_list = ['x', 'o']
            if im not in check_list:
                print('Please enter a valid key!')
            
            else: 
                return im


    def check_input(self, inp):
        error_message = 'Please enter a number according to Tutorial Board'
        try: inp = int(inp)
        except: 
            print(error_message)
            return
        
        move_check_list = [11,12,13,21,22,23,31,32,33]
        if inp not in move_check_list: 
            print(error_message)
            return
        
        return inp