import numpy as np
from game import tic_tac_toe 
# from play_with_naive_agent import naive_agent
# from play_with_the_master import the_master


class play_tic_tac_toe(tic_tac_toe):
    def __init__(self):
        super().__init__()

        
    def play(self):
        while True:
            mode = input("\n1-) Self-Play\n2-) Play with Naive Agent\n3-) Play with the Master!\ni-) Hey, who is THE Master?\nChoose the game mode: ")

            mc = self.mode_check(mode)
            if mc: break
    
        if mode == '1': 
            from play_one_player import self_play
            self.agent = self_play()
            self.agent.play()

        elif mode == '2': 
            from play_with_naive_agent import naive_agent
            self.agent = naive_agent()
            self.agent.play()

        elif mode == '3': 
            from play_with_the_master import the_master
            self.agent = the_master()
            self.agent.play()

        while True:
            choosen = input('\n1-) Main Menu\nq-) Quit\n')
            egc = self.end_game_choosen(choosen)
            if ((egc is not None) & (choosen == '1')): 
                self.play()
            elif egc is not None and choosen == 'q': 
                break
            
            
                

    def which_player(self, move_turn):
        even_or_odd = move_turn%2
        return even_or_odd
    

    def mode_check(self, mode_input):
        check_list = ['1','2','3','i']
        if mode_input not in check_list: 
            print('Invalid Input! Please enter 1,2,3 or i')
            return 
        elif mode_input == 'i':
            print('\nThe Master is the game agent who has never been defeated before according to a rumor.')
            return 
        else:
            return True
    
    def end_game_choosen(self, choosen):
        check_list = ['1', 'q']
        if choosen not in check_list: 
            print('Invalid Input! Please enter 1 or q')
            return 
        else: return True


    def win(self, board = None, check_two_win = False):
        # Self play

        if np.any(board is None):
            board = super().get_game_matrix()

        else: 
            try: board = np.array(board).reshape(3,3)
            except: 
                raise Exception(f'Board could not be transform into np array in the shape of 3x3.\n Board: {board}')  


        if check_two_win == False:
            for mark in [1,2]:
                for i in range(3):
                    try: 
                        if np.array_equal(board[i], np.full(3, mark)): return mark
                        elif np.array_equal(board.T[i], np.full(3, mark)): return mark
                    except: print(board)

                if np.array_equal(np.diag(board), np.full(3, mark)): return mark
                elif np.array_equal(np.diag(np.fliplr(board)), np.full(3, mark)): return mark


        elif check_two_win == True:
            total_win = 0
            for mark in [1,2]:
                for i in range(3):
                    if np.array_equal(board[i], np.full(3, mark)): total_win += 1 
                    elif np.array_equal(board.T[i], np.full(3, mark)): total_win += 1

                if np.array_equal(np.diag(board), np.full(3, mark)): total_win += 1
                elif np.array_equal(np.diag(np.fliplr(board)), np.full(3, mark)): total_win += 1

                if mark == 1 and total_win == 2: total_win -= 1 
            
            if total_win == 2: return True


    


    def game_over(self, who_win):
        super().end_the_game()
        if who_win == 1: print('X Wins!')
        elif who_win == 2: print('O Wins!')
        else: print('Draw!')

    
    def is_game_going_on(self, move_turn = False):
                # IS GAME GOING ON?
        if self.win():  # Game Over!
            if isinstance(move_turn, int):
                self.edit_game_board()
                self.display_board()
                self.game_over(self.win()) 
                return 
            else: return 'Win State Satisfied'
        
        elif isinstance(move_turn, int):
            self.edit_game_board()
            self.display_board()
            move_turn += 1
            if move_turn == 9: self.game_over(0)
            return move_turn
        
        else:
            if np.all(self.game_matrix != 0):
                self.game_over(0)


