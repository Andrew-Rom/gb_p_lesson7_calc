import log
import calc_operations

def select_num_type():
    type_num = input("\n"
                     "*****************************\n"
                     "* Types of numbers:         *\n"
                     "*****************************\n"
                     "* 1 - rational numbers      *\n"
                     "* 2 - complex numbers       *\n"
                     "* 0 - EXIT                  *\n"
                     "*****************************\n"
                     "Your selection: ")
    if type_num not in ['1', '2', '0']:
        log.logging.error("Error")
        print("Error. Incorrect input.")
        select_num_type()
    else:
        return type_num

def operation_for_rational_numbers():
    while True:
        oper = input("\n"
                               "*************************************************************\n"
                               "* Types of operation:                                       *\n"
                               "*************************************************************\n"
                               "* 1 - sum                                                   *\n"
                               "* 2 - subtraction                                           *\n"
                               "* 3 - multiplication                                        *\n"
                               "* 4 - division                                              *\n"
                               "* 5 - exponentiation                                        *\n"
                               "* 6 - root of first number (second number - degree of root) *\n"
                               "* 7 - remainder of division                                 *\n"
                               "* 8 - integer division                                      *\n"
                               "* 0 - previous menu                                         *\n"
                               "* 00 - EXIT                                                 *\n"
                               "*************************************************************\n"
                               "Your selection: ")
        if oper not in ['1', '2', '3', '4', '5', '6', '7', '8', '0', '00']:
            log.logging.error("Error")
            print("Error. Incorrect input.")
            operation_for_rational_numbers()
        elif oper == '00':
            log.logging.info("Stop program")
            exit()
        else:
            return oper

def operation_for_complex_number():
    while True:
        oper = input("\n"
                       "*************************************************************\n"
                       "* Types of operation:                                       *\n"
                       "*************************************************************\n"
                       "* 1 - sum                                                   *\n"
                       "* 2 - subtraction                                           *\n"
                       "* 3 - multiplication                                        *\n"
                       "* 4 - division                                              *\n"
                       "* 5 - exponentiation                                        *\n"
                       "* 6 - root of first number (second number - degree of root) *\n"
                       "* 0 - previous menu                                         *\n"
                       "* 00 - EXIT                                                 *\n"
                       "*************************************************************\n"
                       "Your selection: ")
        if oper not in ['1', '2', '3', '4', '5', '6', '0', '00']:
            log.logging.error("Error")
            print("Error. Incorrect input.")
            operation_for_complex_number()
        elif oper == '00':
            log.logging.info("Stop program")
            exit()
        else:
            return oper

def rational_num():
    op = operation_for_rational_numbers()
    if op == '5' or op == '6':
        try:
            num_1 = float(input("Enter 1 number: ").replace(',', '.'))
            num_2 = int(input("Enter 2 number: ").replace(',', '.'))
        except:
            log.logging.error("Error")
            print("Error. Incorrect input.")
            rational_num()
        return op, num_1, num_2
    elif op == '0':
        calc_operations.actions()
    else:
        try:
            num_1 = float(input("Enter 1 number: ").replace(',', '.'))
            num_2 = float(input("Enter 2 number: ").replace(',', '.'))
        except:
            log.logging.error("Error")
            print("Error. Incorrect input.")
            rational_num()
        return op, num_1, num_2

def complex_num():
    op = operation_for_rational_numbers()
    if op == '5' or op == '6':
        try:
            num_1 = int(input("Enter 1 real part: "))
            num_2 = int(input("Enter 1 imaginary number: "))
            num_3 = int(input("Enter number: "))
            num_C_1 = complex(num_1, num_2)
        except:
            log.logging.error("Error")
            print("Error. Incorrect input.")
            complex_num()
        return op, num_C_1, num_3
    elif op == '0':
        calc_operations.actions()
    else:    
        try:
            num_1 = int(input("Enter 1 real part: "))
            num_2 = int(input("Enter 1 imaginary number: "))
            num_3 = int(input("Enter 2 real part: "))
            num_4 = int(input("Enter 2 imaginary number: "))
            num_C_1 = complex(num_1, num_2)
            num_C_2 = complex(num_3, num_4)
        except:
            log.logging.error("Error")
            print("Error. Incorrect input.")
            complex_num()
        return op, num_C_1, num_C_2

def get_values():
    while True:
        type_n = select_num_type()
        if type_n == '1':
            op, n1, n2 = rational_num()
            return op, n1, n2
        elif type_n == '2':
            op, n1, n2 = complex_num()
            return op, n1, n2
        elif type_n == '0':
            log.logging.info("Stop program")
            exit()
