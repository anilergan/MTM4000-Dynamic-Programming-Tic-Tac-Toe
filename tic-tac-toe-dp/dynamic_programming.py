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

        self.action_values = {}
        # for state, action in self.actions.items():
        #     if action: 
        #         self.action_values[state] = [0 for a in action]

        

    def get_action_values(self, status):
        return self.action_values[status]
        

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
            print(f"   Policy Evaluation ecoch: {epoch}")
             # That will be representation of value's variation
            delta = 0
            # Terminal State Exception
            for state in self.states:
                v = self.values[state]

                if state in self.t_states:
                    self.values[state] = self.reward_function(state)
                    continue
                    
                # First let's evaluate the transitions well. First make s_primes as a list and push it into transition function. Remember to adjust transition function appropriate for that.


                # Check every single s_prime and list them. So in possible next state function we'll be able to observe if rival has a winning action according to our move. If there is, so that's possibility is absolute.
                 
                # for action in self.actions[state]:
                #     all_s_primes = []
                #     for s_prime in super().possible_next_states(state, action):
                #         if s_prime == 0 or s_prime == 1: 
                #             continue
                #         else:
                #             all_s_primes.append(s_prime)
                
                # caution = False
                # for s_prime in all_s_primes:
                #     if self.reward_function(s_prime) == -1:
                #         caution = True

                
                action_value_list = []
                for action in self.actions[state]:
                    for s_prime in super().possible_next_states(state, action):  
                        if s_prime == 1:
                            action_value = 1
                        
                        elif s_prime == 0:
                            action_value = 0
                        
                        else:
                            action_value = super().transition_function(state) * (super().reward_function(state) + self.gamma * self.values[s_prime])
                        

                        self.values[state] += action_value
                
                    action_value_list.append(round(action_value, 2))
                    
                self.action_values[state] = action_value_list

            delta = max(delta, abs(v - self.values[state]))  
            
            if delta < self.epsilon: # until delta < epsilon 
                break
            else: 
                epoch += 1 
            

    def policy_improvement(self): 
        policy_stable = True # stop condition

        for state in self.states:
 
            a = self.policy[state] # best actions

            if state in self.t_states:
                continue

            best_action = None
            best_value = float("-inf") # initialize value is negative infinite due to handle first comparison 
            
            
            for action in self.actions[state]:
                all_s_primes = []
                for s_prime in super().possible_next_states(state, action):
                    if s_prime == 0 or s_prime == 1: 
                        continue
                    else:
                        all_s_primes.append(s_prime)     

            for action in self.actions[state]:
                action_value = 0
                
                for s_prime in self.possible_next_states(state, action):   
                    if s_prime == 1:
                        action_value = 1
                    elif s_prime == 0:
                        action_value = 0
                    else:
                        action_value += super().transition_function(state) * (super().reward_function(state) + self.gamma * self.values[s_prime])  

                if action_value > best_value:
                        best_value = action_value 
                        best_action = action
                
            
            self.policy[state] = best_action

            # when the above loop ends, all actions can be taken for a particular state was evaluated and the best action is selected according to action value's which is calculated informations we get in policy evaluation
            # however, we had considered a random action in policy evaluation and calculated state values according to this. If we could not satisfied the action we select random and the new best action we get now is equal, THEN WE MUST REPEAT POLICY EVALUATION PROCESS WITH THE NEW BEST ACTION WE GOT.

            if a != self.policy[state]: # Comparision Random Action and Best Action
                policy_stable = False 
        
        return policy_stable, 
            
        
    def policy_iteration(self):
        start_time = time()
    
        print('Total Possible State:',len(self.states))
        for s in self.states:
            # choose a random action for each state
            if s not in self.t_states:
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

        
        end_time = time()

        print(f"Policy Iteration process has taken {end_time - start_time} sec.")

        return self.policy, self.action_values
        
          

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

        while True:
            delta = 0
            for state in self.states:
                
                for action in self.actions[state]:
                    all_s_primes = []
                    for s_prime in super().possible_next_states(state, action):
                        if s_prime == 0 or s_prime == 1: 
                            continue
                        else:
                            all_s_primes.append(s_prime)    

                v = self.values[state]
                max_a = float("-inf")
                for action in self.actions:
                    for s_prime in super().possible_next_states(state, action):
                        a = super().transition_function(s_prime, all_s_primes) * (super().reward_function(state) + self.gamma * self.values[s_prime])
                        if a > max_a: max_a = a

                self.values[state] = max_a
                if delta < abs(v-self.values[state]): delta = abs(v-self.values[state])
                if delta < self.epsilon: break


            # for state in self.states:
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
         




