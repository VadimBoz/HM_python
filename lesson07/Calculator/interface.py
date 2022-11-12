from view import get_value_kind
from view import get_value_actions
from view import get_value_num
from view import to_console
import math_real
from logger import log_data


def start_menu():
    print("\n"*3)
    print("Strange calculator")
    print("\n")
    print("-"*25)
    print("  Type of calculations:   \n \n \n",
          "  1 - rational numbers \n   2 - complex numbers \n   3 - exit")
    print("-"*25)
    choice1 = get_value_kind("Your choice: ")
    if choice1 ==3:
         exit("The program is completed")
    main(choice1)


def menu_real_numbers():
    while True:
        print("\nOperations on real numbers")
        choice_actions = get_value_actions(f"\n 1 - '*'{' '*4}2 - '/'\n"
                                           f" 3 - '+'{' '*4}4 - '-'\n"
                                           f" 5 - '//'{' '*3}6 - '%'\n"
                                           f" 7 - '**'{' '*3}8 - 'n!'\n"
                                           f" 9 - sqtr \n "
                                           f"10 - return to start menu\n 11 - EXIT\n Мake your choice: ")
        if choice_actions != 0:
            break
    return choice_actions


def menu_complex_numbers():
    while True:
        print("\nOperations on complex numbers")
        choice_actions = get_value_actions(f"\n 1 - '*'{' '*4}2 - '/'\n"
                                           f" 3 - '+'{' '*4}4 - '-'\n"
                                           f" 5 - '**'\n"
                                           f" 6 - sqtr \n "
                                           f"7 - return to start menu\n 8 - EXIT\n Мake your choice: ")
        if choice_actions != 0:
            break
    return choice_actions


def after_calculation(choice2):
    print("Choice:  \n 1  - for return to start menu\n 2 - continue calculation\n 3 - EXIT")
    choice = get_value_kind("Your choice: ")
    if choice == 1:
        start_menu()
    elif choice == 2:
        main(choice2)
    else:
        exit("The program is completed")


def main(choice1):
    n2 = ""
    match choice1:
        case 1:
            choice2 = menu_real_numbers()
            n1 = get_value_num("\nEnter first number: ")
            if choice2 in [1, 2, 3, 4, 5, 6, 7]:
                n2 = get_value_num("Enter second number: ")
            match choice2:
                case 1:
                    res = math_real.mult(n1, n2)
                case 2:
                    res = math_real.div(n1, n2)
                case 3:
                    res = math_real.sum(n1, n2)
                case 4:
                    res = math_real.dif(n1, n2)
                case 5:
                    res = math_real.int_div(n1, n2)
                case 6:
                    res = math_real.int_mod(n1, n2)
                case 7:
                    res = math_real.exponentiation(n1, n2)
                case 8:
                    res = math_real.factorial(n1)
                case 9:
                    res = math_real.sqrt(n1)
                case 10:
                    start_menu()
                case 11:
                    exit("The program is completed")
        case 2:
            choice2 = menu_complex_numbers()
            n1_r = get_value_num("\nEnter real part of 1 number: ")
            n1_im = get_value_num("Enter imaginary part of 1 number: ")
            n1 = complex(n1_r, n1_im)
            if choice2 in [1, 2, 3, 4, 5]:
                n2_r = get_value_num("\nEnter real part of 2 number: ")
                n2_im = get_value_num("Enter imaginary part of 2 number: ")
                n2 = complex(n2_r, n2_im)
            match choice2:
                case 1:
                    res = math_real.mult(n1, n2)
                case 2:
                    res = math_real.div(n1, n2)
                case 3:
                    res = math_real.sum(n1, n2)
                case 4:
                    res = math_real.dif(n1, n2)
                case 5:
                    res = math_real.exponentiation(n1, n2)
                case 6:
                    res = math_real.sqrt(n1)
                case 7:
                    start_menu()
                case 8:
                    exit("The program is completed")
    to_console(res)
    log_data(n1, n2, choice2, res)
    # print(n1, n2, choice2 , res)
    after_calculation(choice1)
