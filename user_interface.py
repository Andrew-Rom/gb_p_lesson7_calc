import logging

def menu():
    while True:
        type_num = input("Choice\n"
                         "1 - rational\n"
                         "2 - complex\n"
                         "3 - exit\n")
        match type_num:
            case "1":
                rational_num()
            case "2":
                complex_num()
            case "3":
                logging.info("stop program")
                break
            case _:
                logging.error("Err")
                print("Err")


def operation():
    while True:
        operat = input("Choice\n"
                       "1 - sum\n"
                       "2 - subtraction\n"
                       "3 - multiplication\n"
                       "4 - division\n"
                       "5 - pow\n"
                       "6 - sqrt\n"
                       "7 - previous menu\n"
                       "8 - exit\n")
        match operat:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                menu()
            case "8":
                logging.info("stop program")
                break
            case _:
                logging.error("Err")
                print("Err")


def rational_num():
    num_1 = input("Enter 1 number: ")
    num_2 = input("Enter 2 number: ")
    # operation()
    # res =
    # print(res)

def complex_num():
    num_1 = input("Enter 1 real part: ")
    num_2 = input("Enter 1 imaginary number: ")
    num_3 = input("Enter 2 real part: ")
    num_4 = input("Enter 2 imaginary number: ")
    # operation()
    # res =
    # print(res)