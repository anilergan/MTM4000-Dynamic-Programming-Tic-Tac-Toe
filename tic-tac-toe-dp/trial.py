from time import time, sleep
import json
import os
import numpy as np
from play import play_tic_tac_toe as pttt
from MDP import MDP
from dynamic_programming import DP

obj = DP(agent_mark=2)

obj.policy_evaluation()

print('Value must be 1, What is: ', obj.values[(2,0,2,0,1,0,1,0,1)])
    

        
    



