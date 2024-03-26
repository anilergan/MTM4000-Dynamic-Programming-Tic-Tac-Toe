from play_with_computer import computer
import numpy as np

class naive_agent(computer):

    def __init__(self):
        super().__init__()


    def play(self):
        im = super().inception_mark_selection()
        
        super().board_move_tutor()
        self.move_turn = 0

        if im == 'x': super().play_game_as_x(self.agent_move)
        elif im == 'o': super().play_game_as_o(self.agent_move)


    def agent_plays_random(self, ep_cell_co_list, mark):
        random_index = np.random.randint(len(ep_cell_co_list))
        random_coordination = ep_cell_co_list[random_index]
        self.game_matrix[random_coordination[0], random_coordination[1]] = mark

    
    def agent_move(self, turn):
        # turn returns 0 for mark X and 1 for mark O
        mark_num = turn + 1
        empty_cells_coordination_list = super().empty_cells_in_board()
        self.agent_plays_random(empty_cells_coordination_list, mark_num)