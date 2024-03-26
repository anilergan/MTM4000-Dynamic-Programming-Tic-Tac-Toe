from play_with_computer import computer
from MDP import MDP
import numpy as np
import json, ast

class the_master(computer):
    def __init__(self): # random mark is selected for now
        super().__init__() 

    def play(self):
        player_mark = super().inception_mark_selection()
        
        super().board_move_tutor()
        self.move_turn = 0

        if player_mark == 'x': 
            super().play_game_as_x(self.agent_move)

        elif player_mark == 'o': 
            super().play_game_as_o(self.agent_move)


    def agent_move(self, turn):
        # turn returns 0 for mark X and 1 for mark O
        mark_num = turn + 1 
        
        if mark_num == 1: mark = 'X'
        elif mark_num ==2: mark = 'O'
        
        policy_path = f"tic-tac-toe-dp\policies\policy_iteration_{mark}.json"

        with open(policy_path, 'r') as file:
            policy_json = file.read()

        policy_dic = json.loads(policy_json)
        
        policy_dic = {self.str_to_tuple(key): value for key, value in policy_dic.items()}

        game_matrix = self.game_matrix()

        best_action = policy_dic[tuple(game_matrix.flatten())]

        row, col = self.convert_index_to_coordinate(best_action)

        game_matrix[row, col] = mark_num

    

    def convert_index_to_coordinate(self, index_):
        """
        This function converts the number which points a state tuple action to a coordinate to point the game matrix.
        For example, if there is a state such as: (0,0,1,2,0,0,2,1,0)
        En there is a action like: 0
        If we convert the state into game matrix it would seems like: 
        [[0,0,1],
         [2,0,0],
         [2,1,0]]
        After the action it would become:
        [[1,0,1],
         [2,0,0],
         [2,1,0]]
        
        Due to actualize this, ought to convert the number 0 into coordinate as (0,0) 
        """

        # 0, 1, 2 -> (0, iter) 
        # 3, 4, 5 -> (1, iter)
        # 6, 7, 8 -> (2, iter)

        row = int(index_ / 3)
        col = index_ % 3

        return row, col



    def str_to_tuple(self, str_):
        """
        This function structures and returns an expression like '(1,2,3)' in tuple form (1,2,3).
        """
        tuple_ = tuple(map(int, str_.strip('()').split(',')))
        return tuple_



    def check_values_of_a_status(status):
        


        
        