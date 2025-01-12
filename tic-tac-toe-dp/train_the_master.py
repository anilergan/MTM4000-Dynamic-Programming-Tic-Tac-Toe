from dynamic_programming import DP
import json

# Policy Iteration
def define_an_agent_PI(mark):
    if mark == 'X': mark_number = 1
    elif mark == 'O': mark_number = 2
    else: 
        raise print("Mark parameter must be 'X' or 'O'.")
    
    the_master = DP(mark_number)   
    policy, action_values = the_master.policy_iteration()
    

    # print('Policy iteration traning is DONE! Policies will attempt to be saved')

    policy_str_keys = {str(key): int(value) for key, value in policy.items()}

    # print(the_master.action_values)

    action_values_str_keys = {str(key): value for key, value in action_values.items()}

    json_file_path = f"tic-tac-toe-dp\\policies\\policy_iteration_{mark}.json"
    with open(json_file_path, 'w') as json_file:
        json.dump(policy_str_keys, json_file)
    
    json_file_path = f"tic-tac-toe-dp\\action-values\\action_values_{mark}_PI.json"
    with open(json_file_path, 'w') as json_file:
        json.dump(action_values_str_keys, json_file)
    

    print("There is a new messeage from the master: 'I KNOW KUNG-FU'\n")


# Value Iteration
def define_an_agent_VI(mark):
    if mark == 'X': mark_number = 1
    elif mark == 'O': mark_number = 2
    else: 
        raise print("Mark parameter must be 'X' or 'O'.")
    
    the_master = DP(mark_number)   
    policy, action_values = the_master.value_iteration()
    

    # print('Policy iteration traning is DONE! Policies will attempt to be saved')
    
    policy_str_keys = {str(key): int(value) for key, value in policy.items()}

    # print(the_master.action_values)

    action_values_str_keys = {str(key): value for key, value in action_values.items()}

    json_file_path = f"tic-tac-toe-dp\\policies\\value_iteration_{mark}.json"
    with open(json_file_path, 'w') as json_file:
        json.dump(policy_str_keys, json_file)
    
    json_file_path = f"tic-tac-toe-dp\\action-values\\action_values_{mark}_VI.json"
    with open(json_file_path, 'w') as json_file:
        json.dump(action_values_str_keys, json_file)
    

    print("There is a new messeage from the master: 'I KNOW KUNG-FU'\n")


define_an_agent_VI(mark='X') 
define_an_agent_VI(mark='O')