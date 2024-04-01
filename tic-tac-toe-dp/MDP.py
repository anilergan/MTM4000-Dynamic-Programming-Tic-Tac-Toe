from play import play_tic_tac_toe
import numpy as np
import json

class MDP(play_tic_tac_toe):

    def __init__(self, mark: int):
        """
        Parameters:
        mark (int) -> 1 or 2: Agent's mark must be described explicitly.
        mark: 1 -> 'x' aka player 1 who starts the game first
        mark: 2 -> 'o' aka player 2 
        """

        self.mark = mark

        if self.mark not in [1, 2]:
            raise ValueError("Value must be either 1 or 2.")
        
        if self.mark == 1:
            self.opp_mark = 2

        else: self.opp_mark = 1
        
        # LEGAL STATES
        self.states = [] 
        self.generate_all_configs() # All Configurations

        self.possible_states = self.generate_possible_states() # Legal States for agent's mark 
        
        # TERMINAL STATES
        self.termination_states = set()
        self.generate_termination_states()

        # ACTIONS Dictionary
        self.actions = {} # key: state(list), # value: actions(list)
        self.generate_actions()

    

    def generate_all_configs(self):
        # Creating all board configuration states
        for s in np.ndindex(3,3,3,3,3,3,3,3,3):
            state = tuple(s)
            self.states.append(state)


    def eliminate_two_win_states(self):
        no_two_win_states = []

        # Eliminate two win states
        x_wins, o_wins = np.array([1,1,1]), np.array([2,2,2]) 
        
        for state in self.states:
            if not super().win(state, check_two_win = True):
                no_two_win_states.append(state)
        
        return no_two_win_states
        

    def generate_possible_states(self):
        """
        This function eliminates the states which contains more O than X 
        """

        possible_states = []
        for state in self.eliminate_two_win_states():
   
            if self.mark == 1: # Agent is X player
                cond = state.count(1) == state.count(2) or state.count(0) == 9 # False # False -> False
                if cond: possible_states.append(state) 
    

            elif self.mark == 2: # Agent is O player
                # Remember that X always starts first
                cond = state.count(1) - state.count(2) == 1
                if cond: possible_states.append(state)


        return possible_states
        

    def generate_termination_states(self):
        for state in self.eliminate_two_win_states():
            if super().win(state): self.termination_states.add(state)
            elif state.count(0) == 0: self.termination_states.add(state)

                

    def generate_actions(self):
        """
        This function takes all possible states and update the possible actions for each state
        """
        for state in self.states:
            self.actions[state] = None
            if state not in self.termination_states:
                self.actions[state] = []
                for i in range(9):
                    # example state: [1,0,2,0,1,0,0,0,2]
                    # [X   O]
                    # [  X  ]
                    # [    O]
                    if state[i] == 0:
                        self.actions[state].append(i)  



    def transition_function(self, state, a):
        """
        The probability of each action that can be taken for a given state
        """
        

        return 1 / (len(self.actions[state]) - 1)


    def threat_detector(self, state, a):
        s_a = list(state).copy()
        s_a[a] = self.mark
        
        t_s = s_a.copy()
        t_s_actions = []
        for index, cell in enumerate(t_s):
            if cell == 0:
                t_s_actions.append(index)
        
        opp_definite_action = None
        for action in t_s_actions:
            t_s_a = list(t_s).copy()
            t_s_a[action] = self.mark

            if super().win(t_s_a):
                opp_definite_action = action
        
        if opp_definite_action:
            s_a[opp_definite_action] = self.opp_mark
            return tuple(s_a)


        
        



    def opponents_fury(self, s_a):
        """
        If opponent has a action which avoids your next action that wins the game, opponent takes that action definetly.
        """
        s_a_actions = []
        for index, cell in enumerate(s_a):
            if cell == 0:
                s_a_actions.append(index)


        for action in s_a_actions:
            s_prime = list(s_a).copy()
            s_prime[action] = self.opp_mark
            
            s_prime_action = s_prime.copy()
        
            s_prime_acions_list = []
            for index, cell in enumerate(s_prime_action):
                if cell == 0: s_prime_acions_list.append(index)
            
            opp_fury = None
            for action in s_prime_acions_list:
                s_prime_action[action] = self.mark
                if super().win(s_prime_action): # If agent wins
                    opp_fury = action
                    break
                
            if opp_fury:
                for action in s_a_actions:
                    if action == opp_fury:
                        s_a[action] = self.opp_mark
                        return s_a # S Prime
                




    def possible_next_states(self, state, action):
        """
        This is the function returns very next possible states as tuple
        """

        s_a = list(state) 
        
        s_a[action] = self.mark 

        if self.win(s_a):
            return []

        s_primes = []
        for index, cell in enumerate(s_a):
            if cell == 0:
                s_prime = s_a.copy()
                s_prime[index] = self.opp_mark
                s_primes.append(tuple(s_prime))
        
        return s_primes
        


    def reward_function(self, state):
        """
        This function takes a state and returns the reward of the state
        """
        if super().win(state) == 1 and self.mark == 1: return 1
        elif super().win(state) == 2 and self.mark == 1: return -1
        elif super().win(state) == 1 and self.mark == 2: return -1
        elif super().win(state) == 2 and self.mark == 2: return 1
        else: return 0


    def get_possible_states(self):
        for state in self.possible_states:
            state = tuple(state) # It is criticial code allows to make it as a dictionary key, otherwise it is not possible to make a list as a dictionary key.
        return self.possible_states
    
    def get_terminal_states(self):
        return self.termination_states
    
    def get_actions(self):
        return self.actions
        

    # def improved_transition_probability(self, state, action):
    #     """
    #     This function takes a state and returns the probability of each possible next state
    #     inspired from value iteration policy
    #     """
    #     # if the game is over, return 0
    #     if state in self.termination_states: return 0
    #     # if the game is not over, return 1/number of possible actions for O
    #     else: return 1 if action == self.policy[state] else 0
        

