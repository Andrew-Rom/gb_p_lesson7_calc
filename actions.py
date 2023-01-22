import calc_operations as c
import МОДУЛЬ_ВВОДА as mod


def actions_with_real():
    act_num_1, act_num_2, act_operation = mod.МЕТОД_ПОЛУЧЕНИЯ_ЗНАЧЕНИЙ()     # Требует актуализации после написания модуля ввода
    if act_operation == '+':
        return c.oper_add(act_num_1, act_num_2)
    elif act_operation == '-':
        return c.oper_sub(act_num_1, act_num_2)
    elif act_operation == '*':
        return c.oper_mult(act_num_1, act_num_2)
    elif act_operation == '/':
        return c.oper_simp_div(act_num_1, act_num_2)
    elif act_operation == '//':
        return c.oper_div(act_num_1, act_num_2)
    elif act_operation == '%':
        return c.oper_mod(act_num_1, act_num_2)
    elif act_operation == '**':
        return c.oper_pow(act_num_1, act_num_2)


def actions_with_complex():
    act_num_1, act_num_2, act_operation = mod.МЕТОД_ПОЛУЧЕНИЯ_ЗНАЧЕНИЙ()    # Требует актуализации после написания модуля ввода
    if act_operation == '+':
        return c.oper_add(act_num_1, act_num_2)
    elif act_operation == '-':
        return c.oper_sub(act_num_1, act_num_2)
    elif act_operation == '*':
        return c.oper_mult(act_num_1, act_num_2)
    elif act_operation == '/':
        return c.oper_simp_div(act_num_1, act_num_2)
    elif act_operation == '**':
        return c.oper_pow(act_num_1, act_num_2)


def action():
    if USERINPUT == 1:                                                      # Требует актуализации после написания модуля ввода
        actions_with_real()
    else:
        actions_with_complex()

def data_printer(data, title):
    print(f'{title} = {data}')
