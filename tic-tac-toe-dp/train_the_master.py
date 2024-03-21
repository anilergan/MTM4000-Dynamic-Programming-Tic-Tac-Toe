from dynamic_programming import DP
import json


def define_an_agent(mark):
    if mark == 'X': mark_number = 1
    elif mark == 'O': mark_number = 2
    else: 
        raise Exception("Mark parameter must be 'X' or 'O'.")
    

    the_master = DP(mark_number) # X

    
    the_master.policy_iteration()
    

    print('Policy iteration traning is DONE! Policies will attempt to be saved')

    policy_str_keys = {str(key): value for key, value in the_master.policy.items()}

    with open(f"tic-tac-toe-dp\policies\policy_iteration_{mark}.json", 'w') as json_file:
        json.dump(policy_str_keys, json_file)
    

    print('There is a new messeage from the master: I KNOW KUNG-FU')



define_an_agent(mark='X') #