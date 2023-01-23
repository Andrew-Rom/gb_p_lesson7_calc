import logging


def operation():

    while True:
        type_num = menu()
        if type_num == '1':
            operat = input("Choice\n"
                        "1 - sum\n"
                        "2 - subtraction\n"
                        "3 - multiplication\n"
                        "4 - division\n"
                        "5 - remainder of the division\n"
                        "6 - integer division\n"
                        "7 - pow\n"
                        "8 - sqrt\n")

        elif  type_num == '2':
            operat = input("Choice\n"
                        "1 - sum\n"
                        "2 - subtraction\n"
                        "3 - multiplication\n"
                        "4 - division\n"
                        "7 - pow\n"
                        "8 - sqrt\n")


        return(type_num, operat)

def menu():
    while True:
        type_num = input("Choice\n"
                         "1 - rational\n"
                         "2 - complex\n"
                         "3 - exit\n")
        return type_num            


def rational_num():
    num_1 = float(input("Enter 1 number: "))
    num_2 = float(input("Enter 2 number: "))
    return num_1, num_2

def complex_num():
    num_1 = int(input("Enter 1 real part: "))
    num_2 = int(input("Enter 1 imaginary number: "))
    num_3 = int(input("Enter 2 real part: "))
    num_4 = int(input("Enter 2 imaginary number: "))
    num_C_1 = complex(num_1, num_2)
    num_C_2 = complex(num_3, num_4)
    return num_C_1, num_C_2
