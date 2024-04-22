from time import time, sleep
import json
import os
import numpy as np
from play import play_tic_tac_toe as pttt
from MDP import MDP
from dynamic_programming import DP

"""
class Game():
    def __init__(self):
        print('Game')
        self.game_att = np.array([0,0,0])
    


    
class Play(Game):
    def __init__(self):
        super().__init__()
        print('Play')


class Computer(Play):
    def __init__(self):
        super().__init__()
        print('Computer')
        game_obj = Computer()
        print(game_obj.game_att)
        game_obj.set_game_att(1,10)
        print(game_obj.game_att)
        print(game_obj.get_game_att())

    def set_game_att(self, index, number):
        self.game_att[index] = number
    
    def get_game_att(self):
        return self.game_att


class Game():
    def __init__(self):
        print('Game')
        self.game_attr = np.array([[0,0,0], [0,0,0], [0,0,0]])

    def set_game_attr2(self, row, col, num):
            self.game_attr[row, col] = num


class Play(Game):
    def __init__(self):
        super().__init__()
        print('Play')


class Computer(Play):
    def __init__(self):
        super().__init__()
        print('Computer')
    
    


class NaiveAgent(Computer):
    def __init__(self):
        super().__init__()
        print('Naive Agent')
    
    def set_game_attr(self, row, col, num):
        self.game_attr[row, col] = num


class Ui(Play):
    def __init__(self):
        super().__init__()
        print('Ui')

        naive_agent_obj = NaiveAgent()

        matrix1 = naive_agent_obj.game_attr
        print(matrix1)
        naive_agent_obj.set_game_attr2(2,2,88)
        print(matrix1)
        

Ui_obj = Ui()
"""

# action_dic = {
#     (1,2,0): [2],
#     (2,0,0): [1,2],
#     (0,2,1): [0]
# }

# for key, val in action_dic.items():
#     print(key, val)



# naive_agent_object = NaiveAgent()
# print(naive_agent_object.game_attr)
# naive_agent_object.set_game_attr(0, 23)
# print(naive_agent_object.game_attr)







# class NaiveAgent(Computer):
#     def __init__(self):
#         super().__init__()
#         print('Naive Agent')
    
#     def na_func(self, num):
#         super().get_att()[0] = num


# class Ui(Play):
#     def __init__(self):
#         super().__init__()
#         print('Ui')
#         print('Once: ', super().get_att())
#         na_object = NaiveAgent()
#         na_object.na_func(1)
#         print('Sonra: ', super().get_att())


# Ui_obj = Ui()



student_tuples = {
    1: 1,
    2: 12,
    3: 9
}

k = sorted(student_tuples.items(), key=lambda x: x[1], reverse=True)

print(k[0][1])