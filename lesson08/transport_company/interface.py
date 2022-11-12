from view import get_value
from view import get_name
from view import get_servise_number
from view import send_list_print
from view import get_data_employee
from view import get_date
from transfer_data import print_csv
from transfer_data import read_csv
from transfer_data import add_record
from transfer_data import change_info_file


def start_menu():
    print("\n"*3)
    print("-"*30)
    print(" "*5, "Staff of company")
    print("-"*30)
    print()
    print("1 Show all employees",
          "2 Search by last name",
          "3 Search by service number",
          "4 Employees by department",
          "5 Employees by profession",
          "6 Add a new employee ",
          "7 Сhange employee information",
          "8 Delete employee",
          "9. Exit", sep="\n")
    print()
    choice_start = get_value("Input item number: ")
    return choice_start


def search_by_service_number():
    num = get_servise_number("Servise_number: ")
    data = read_csv()
    if data[0] == 0:
        return ""
    for i in data:
        if i[1] == num:
            res = f"service_number - {i[1]}, {i[2]} {i[3]} - {i[5]} отдела {i[4]}"
            return res
    else:
        return "The service number is missing!"
    # res = (f"service_number - {i[1]}, {i[2]} {i[3]} - {i[5]} отдела {i[4]}" for i in data if i[1]==l_name)


def search_by_last_name():
    l_name = get_name("Input last name: ")
    data = read_csv()
    if data[0] == 0:
        return ""
    list_name = []
    for i in data:
        if i[2] == l_name:
            list_name.append(
                f"service_number - {i[1]}, {i[2]} {i[3]} - {i[5]} отдела {i[4]}")
    if len(list_name) > 0:
        return list_name
    else:
        return "The last name is missing!"


def search_by_department():
    d_name = get_name("Input department: ")
    data = read_csv()
    if data[0] == 0:
        return ""
    list_d_name = []
    for i in data:
        if i[4] == d_name:
            list_d_name.append(
                f"service_number - {i[1]}, {i[2]} {i[3]} - {i[5]} отдела {i[4]}")
    if len(list_d_name) > 0:
        return list_d_name
    else:
        return ["The department is missing!"]

def to_continee(messege):
    input(messege)


def search_by_profession():
    p_name = get_name("Input department: ")
    data = read_csv()
    if data[0] == 0:
        return ""
    list_p_name = []
    for i in data:
        if i[5] == p_name:
            list_p_name.append(
                f"service_number - {i[1]}, {i[2]} {i[3]} - {i[5]} отдела {i[4]}")
    if len(list_p_name) > 0:
        return list_p_name
    else:
        return ["The profession is missing!"]


def menu_change_info():
    servise_number = get_servise_number("Input servise number employee: ")
    data = read_csv()
    if data[0] == 0:
        return ""
    for i in data:
        if i[1] == servise_number:
            print(
                f"service_number - {i[1]}, {i[2]} {i[3]} - {i[5]} отдела {i[4]}")
            id, s_n, last_name, first_name, department, profession, salary, date_employment, date_dismissal = i
            break
    else:
        return "The service number is missing!"

    print()
    print("1 last name", "2 first name", "3 department", "4 profession", "5 salary",
          "6 date of employment", "7 date of dismissal", "8 return to the  main menu",  sep="\n")
    num = get_value("\n Select field for chenge: ")
    match num:
        case 1:
            last_name = get_name('Input last name: ')
            to_continee("To continue peress Enter")
        case 2:
            first_name = get_name('Input first name: ')
            to_continee("To continue peress Enter")
        case 3:
            last_name = get_name('Input department: ')
            to_continee("To continue peress Enter")
        case 4:
            department = get_name('Input department: ')
            to_continee("To continue peress Enter")
        case 5:
            profession = get_name('Input profession: ')
            to_continee("To continue peress Enter")
        case 6:
            salary = get_value('Input  salary: ')
            to_continee("To continue peress Enter")
        case 7:
            date_employment = get_date('Input date of employment: ')
            to_continee("To continue peress Enter")
        case 8:
            date_dismissal = get_date('Input date of dismissal: ')
            to_continee("To continue peress Enter")
        case _:
            print()
    change_info_file(id, s_n, last_name, first_name, department,
                     profession, salary, date_employment, date_dismissal)


def menu_del_info():
    servise_number = get_servise_number("Input servise number employee: ")
    data = read_csv()
    if data[0] == 0:
        return "The service number is missing!"
    for i in data:
        if i[1] == servise_number:
            print(
                f"service_number - {i[1]}, {i[2]} {i[3]} - {i[5]} отдела {i[4]}")
            id, s_n, last_name, first_name, department, profession, salary, date_employment, date_dismissal = i
            break
    last_name = "Empty"
    first_name = " "
    department = " "
    profession = " "
    salary = " "
    date_employment = " "
    date_dismissal = " "
    change_info_file(id, s_n, last_name, first_name, department,
                     profession, salary, date_employment, date_dismissal)


def to_continee(messege):
    input(messege)


def action():
    while True:
        choice_st = start_menu()
        match choice_st:
            case 1:  # 1 Show all employees
                send_list_print([["id", "s/n", "last name", "first name", "department",
                                  "profession", "salary", "date of employment", "date of dismissal"]])
                print_csv()
                to_continee("To continue peress Enter")
            case 2:  # 2 Search by last name
                l_name = search_by_last_name()
                send_list_print(l_name)
                to_continee("To continue peress Enter")
            case 3:  # 3  Search by service number
                lst = search_by_service_number()
                send_list_print(lst)
                to_continee("To continue peress Enter")
            case 4:  # 4 Employees by department
                lst = search_by_department()
                send_list_print(lst)
                to_continee("To continue peress Enter")
            case 5:  # "5 Employees by profession"
                lst = search_by_profession()
                send_list_print(lst)
                to_continee("To continue peress Enter")
            case 6:  # 6 Add a new employee
                lst = get_data_employee()
                if lst[0] != 0:
                    add_record(lst[0], lst[1], lst[2],
                               lst[3], lst[4], lst[5], lst[6])
                    to_continee("To continue.. peress Enter")
                else:
                    to_continee("To continue,, peress Enter")
            case 7:  # 7 Сhange employee information
                menu_change_info()
                to_continee("To continue peress Enter")
            case 8:  # 8 Delete employee
                menu_del_info()
                to_continee("To continue peress Enter")
            case 9:  # "9. Exit"
                exit("The program is completed!")
