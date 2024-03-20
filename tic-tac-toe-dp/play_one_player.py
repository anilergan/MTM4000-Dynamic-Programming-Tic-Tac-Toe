from play import play_tic_tac_toe 

class self_play(play_tic_tac_toe):

    def __init__(self):
        super().__init__()
        self.self_play()


    def self_play(self):
        super().board_move_tutor()
        move_turn = 0 

        while super().get_game_on() == True: # "Inherited from the superclass (tic_tac_toe)
            turn = super().which_player(move_turn) #if 0 it's first player if 1 it's second player 
            self.move(turn)
            move_turn = super().is_game_going_on(move_turn)
            if not move_turn: break
            

    def move(self, turn):
        if turn == 0: mark = 'X'
        elif turn == 1: mark = 'O'
        move_coordinate = input('Move {}: '.format(mark))
        
        move_coordinate = self.check_input(move_coordinate)
        if not move_coordinate: 
            self.move(turn)
            return

        move_row = int(str(move_coordinate)[0]) - 1
        move_col = int(str(move_coordinate)[1]) - 1

        if (super().get_game_matrix()[move_row, move_col] != 0):
            print('Please leave a mark in an empty cell')
            self.move(turn)
            return

        super().get_game_matrix()[move_row, move_col] = turn + 1      


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