import user_interface as mod


def actions():
    typ_num, act_operation = mod.operation()
    if typ_num == '1':
        num_1, num_2 = mod.rational_num()
    elif typ_num == '2':
        num_1, num_2 = mod.complex_num()

    if act_operation == '1':
        return num_1 + num_2
    elif act_operation == '2':
        return num_1 - num_2
    elif act_operation == '3':
        return num_1 * num_2
    elif act_operation == '4':
        return num_1 / num_2
    elif act_operation == '6':
        return num_1 // num_2
    elif act_operation == '5':
        return num_1 % num_2
    elif act_operation == '7':
        return num_1 ** num_2
    elif act_operation == '8':
        return num_1 ** (1/num_2)
import logging