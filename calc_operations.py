import user_interface as mod
from log import logging

def actions():
    num_1, num_2, act_operation = mod.get_values()
    if act_operation == '1': return num_1 + num_2
    elif act_operation == '2': return num_1 - num_2
    elif act_operation == '3': return num_1 * num_2
    elif act_operation == '4': return num_1 / num_2
    elif act_operation == '5': return num_1 ** num_2
    elif act_operation == '6': return num_1 ** (1/num_2)
    elif act_operation == '7': return num_1 % num_2
    elif act_operation == '8': return num_1 // num_2
    elif act_operation == '0': actions()
