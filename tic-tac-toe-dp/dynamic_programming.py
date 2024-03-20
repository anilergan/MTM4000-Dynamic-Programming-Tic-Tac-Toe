from time import time, sleep
from MDP import MDP
import numpy as np

class DP(MDP):

    def __init__(self, agent_mark, gamma = 0.9, epsilon = 1.0e-10, ):
        super().__init__(agent_mark)

        self.gamma = gamma
        self.epsilon = epsilon

        self.states = super().get_possible_states() 
        self.t_states = super().get_terminal_states()
        self.actions = super().get_actions()
        
        self.values = {}
        self.initialize_V()

        self.policy = {}
        self.initialize_P()


    def initialize_V(self):
        for state in self.states:
            self.values[state] = 0

    def initialize_P(self):
        for state in self.states:
            self.policy[state] = None


    def policy_evaluation(self):
        """
        This function represents Policy Evaluation Algorithm. It evaluate 
        """
        epoch = 1
        while True:
             # That will be representation of value's variation
            delta = 0
            # Terminal State Exception
            for state in self.states:
                v = self.values[state]

                if state in self.t_states:
                    self.values[state] = self.reward_function(state)
                    continue
                    
                # First let's evaluate the transitions well. First make s_primes as a list and push it into transition function. Remember to adjust transition function appropriate for that. 

                s_prime_list = []
                for s_prime in super().possible_next_states(state, self.actions[state]):
                    s_prime_list.append(s_prime)
                
                transition_dictionary = super().transition_function(s_prime_list)



                for s_prime in super().possible_next_states(state, self.actions[state]): # state as a list & action as a list
                    # The sum of the values of the new states that can be reached after taking an action 

                    if s_prime in self.t_states: # There is no s_prime, so it means I won the game after I had taken the action 
                        self.values[state] = super().reward_function(s_prime)
            
                    
                    else: 
                    
                        self.values[state]
                        self.values[s_prime]

                        self.values[state] += super().transition_function(state)* (super().reward_function(state) + self.gamma * self.values[s_prime])  



            delta = max(delta, abs(v - self.values[state]))  
            
            if delta < self.epsilon: # until delta < epsilon 
                print('   Delta < Epsilon!')
                break
            else: 
                epoch += 1 
            

    def policy_improvement(self): 
        for state in self.states:
            temp = self.policy[state]

            if state in self.t_states:
                continue

            best_action = None
            best_value = float("-inf")
            policy_stable = True
            

            for action in self.actions[state]:
                expected_value = self.reward_function(state)
                for s_prime in self.possible_next_states(state, action):

                                    
                    expected_value += super().transition_function(state) * (super().reward_function(state) + self.gamma * self.values[s_prime])

                if expected_value > best_value:
                    best_value = expected_value # -inf is utilized in order to take on an unbounded upper value for comparision role
                    best_action = action
                
            self.policy[state] = best_action

            if temp != self.policy[state]: # Comparision Random Action and Best Action
                policy_stable = False 
        
        return policy_stable
            
        


    def policy_iteration(self):
        start_time = time()
        for s in self.states:
            # choose a random action for each state
            if s not in self.t_states:
                # A random action selection for every single policy
                self.policy[s] = np.random.choice(self.actions[s])
            
        policy_iter = 1
        while True:
            print("Policy Iteration loop: {}".format(policy_iter))
            self.policy_evaluation()

            if self.policy_improvement(): 
                break

            else: policy_iter += 1
        
        end_time = time()

        print(f"Policy Iteration process has taken {end_time - start_time} sec.")

        return self.policy
        
            

    def value_iteration(self):
        """
        Value Iteration for estimating π ≈ π*

        Algortihm parameter: a small threshhold θ > 0 determining accuracy of estimation Initalize V(s), for all s ∈ S+, arbitrarly except that V(terminal) = 0

        Loop:
        |    Δ ← 0
        |    Loop for each s ∈ S:
        |        v ← V(s)
        |        V(s) ← max[a](∑[s',r] p(s', r|s, a)[r + γ V(s')])
        |        Δ ← max(Δ,|v-V(s)|)
        until Δ < 0

        Output a deterministic policy, π ≈ π* such that
            π(s) 0 argmax[a](∑[s',r] p(s', r|s, a)[r + γ V(s')])
        """


        # Gamma: Discount factor which represents coefficient determines the importance of subsequent states in determinining policy for current state
        # Epsilon: That represents the number (which is proposed to be a very small) of condition to break infinitive loop 
        # Delta: Value variation
        
        # BELLMAN EQUATION NOTATION MEANINGS
        # p(s', r|s, a): Each next state's transition probability
        # [r + γ V(s')]: 
            # r: The instant reward
            # γ: Discount factor to consider next states in current state
            # V(s'): Calculated value function for next state
        
        delta = 0

         # possible states only due to agent's mark
         



