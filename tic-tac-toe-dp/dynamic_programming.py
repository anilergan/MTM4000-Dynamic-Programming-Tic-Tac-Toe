from time import time, sleep
from MDP import MDP
import numpy as np

class DP(MDP):

    def __init__(self, agent_mark, gamma = 0.9, epsilon = 1.0e-10, ):
        
        super().__init__(agent_mark)

        self.gamma = gamma
        self.epsilon = epsilon
        
        self.values = {}
        self.initialize_V()

        self.policy = {}
        self.initialize_P()

        self.action_values_PI = {}
        self.action_values_VI = {}


    def initialize_V(self):
        for state in self.possible_states:
            self.values[state] = 0

    def initialize_P(self):
        for state in self.possible_states:
            self.policy[state] = None



    def policy_evaluation(self):
        """
        This function represents Policy Evaluation Algorithm. It evaluate 
        """
        epoch = 1
        

        while True:
            print(f"   Policy Evaluation ecoch: {epoch}")
             # That will be representation of value's variation
            
            # Terminal State Exception
            e = 0
            delta = 0
            for state in self.possible_states:
                
                old_delta = delta
            
                v = self.values[state]
                a = self.policy[state] # random action


                # CHECK TERMINATION STATE for draw or lose
                if state in self.termination_states:
                    self.values[state] = self.reward_function(state)
                    continue

                state_action = list(state).copy()
                state_action[a] = self.mark
                state_action = tuple(state_action)

                # CHECK TERMINATION STATE for win  
                if state_action in self.termination_states:
                    self.values[state] = self.reward_function(s_a = state_action)
                    continue
                
                         
                action_value = 0
                for s_prime in super().possible_next_states(state_action):
                    
                    action_value += super().transition_function(state_action, s_prime) * ((self.gamma * self.values[s_prime]))
                    


                delta = max(delta, abs(v - action_value))
                self.values[state] = action_value
                
                
                if old_delta < delta:
                    e += 1 
                    
                    # if state == [0,0,0,0,0,0,0,0,0]:
                    print('\n')
                    print('     State:', state)
                    print('     Delta:', delta) 
                    # print('     State: ', state)

            print('   \nTotal states not converge:', e)
            print('  ', '-'*40)      
            
            if delta < self.epsilon: # until delta < epsilon 
                break
            else: 
                epoch += 1 
            

    def policy_improvement(self): 
        policy_stable = True # stop condition

        for state in self.possible_states:
 
            action = self.policy[state] # current action

            best_value = float("-inf") # initialize value is negative infinite due to handle first comparison 

            action_value_list = []
            # CHECK TERMINATION STATE for draw or lose
            if state in self.termination_states:
                continue   

            for a in self.actions[state]:

                state_action = list(state).copy()
                state_action[a] = self.mark
                state_action = tuple(state_action)

                # CHECK TERMINATION STATE for win
                if state_action in self.termination_states:
                    action_value = 1
                    self.policy[state] = a

                    if action_value % 1 == 0:
                        action_value_list.append(action_value)
                
                    else: 
                        action_value_list.append(round(action_value, 2))


                action_value = 0
                for s_prime in super().possible_next_states(state_action):
                    action_value += super().transition_function(state_action, s_prime) * (self.gamma * self.values[s_prime])
            

                if action_value > best_value:
                        best_value = action_value 
                        self.policy[state] = a

                
                if action_value % 1 == 0:
                    action_value_list.append(action_value)
                
                else: 
                    action_value_list.append(round(action_value, 2))
                    
            self.action_values_PI[state] = action_value_list

            if action != self.policy[state]: # Comparision Random Action and Best Action
                policy_stable = False 
        
        return policy_stable
            
        
    def policy_iteration(self):
        start_time = time()
    
        print('Total Possible State:',len(self.possible_states))
        for s in self.possible_states:
            # choose a random action for each state
            if s not in self.termination_states:
                # A random action selection for every single policy
                self.policy[s] = np.random.choice(self.actions[s])
        
        policy_iter = 1
        while True:
            print("Policy Iteration loop: {}".format(policy_iter))
            self.policy_evaluation()

            policy_stable = self.policy_improvement()
            if policy_stable: 
                break

            else: 
                policy_iter += 1

        
        self.policy = {key: value for key, value in self.policy.items() if value is not None}

        end_time = time()

        progress_sec = end_time - start_time
        progress_min = int(progress_sec / 60)
        progress_sec = round(progress_sec % 60)

        print("Policy Iteration has taken {} min {} sec".format(progress_min, progress_sec))

        return self.policy, self.action_values_PI
        
          


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
        start_time = time()

        epoch = 0
        while True:
            print(f'Value Iteration Epoch {epoch}')
            delta = 0
            for state in self.possible_states:  

                if state in self.termination_states:
                    self.values[state] = self.reward_function(state, a)
                    continue 

                v = self.values[state]
                
                action_values_dict = {}
                a = 0
                for action in self.actions[state]:
                    # 3,5,6,7
                    for s_prime in super().possible_next_states(state, action):
                        if s_prime == 1: a = 1

                        elif s_prime == 0: a = 0
                
                        else: a += super().transition_function(state, action, s_prime) * (super().reward_function(state) + self.gamma * self.values[s_prime])

                    action_values_dict[action] = a
                
                max_value = float("-inf")
                max_value_action = None
                for action, value in action_values_dict.items():
                        if value > max_value: 
                            max_value = value
                            max_value_action = action
                
                self.action_values_VI[state] = list(action_values_dict.values())
                
                self.policy[state] = max_value_action
                self.values[state] = max_value

                delta  = max(delta, abs(v - self.values[state]))

            if delta < self.epsilon: break
            else: 
                epoch += 1
                print(f'  Delta: {delta}')
        
        self.policy = {key: value for key, value in self.policy.items() if value is not None}

        end_time = time()

        progress_sec = end_time - start_time
        progress_min = int(progress_sec / 60)
        progress_sec = round(progress_sec % 60)

        print("Value Iteration has taken {} min {} sec".format(progress_min, progress_sec))

        return self.policy, self.action_values_VI
         


