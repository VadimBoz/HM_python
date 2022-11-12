from exception import exception_menu_item
from exception import exception_name
from exception import exception_servise_number
from exception import exception_number
from exception import exception_date


def get_value(message) -> int:
    while True:
        value = input(message)
        if exception_menu_item(value):
            return int(value)
        else:
            print("\n", "-"*20, "Invalid number, repeat input", "-"*20)



def get_name(message):
    while True:
        value = input(message)
        if exception_name(value):
            return value
        else:
            print("\n", "-"*20, "Invalid name, repeat input", "-"*20)



def get_servise_number(message):
    while True:
        value = input(message)
        if exception_servise_number(value):
            return value
        else:
            print("\n", "-"*20, "Invalid name, repeat input", "-"*20)



def send_to_print(value):
    print(value)


def send_list_print(value):
    for i in value:
        print(i)


def get_date(value):
    while True:
        value = input(value)
        if exception_date(value):
            return value
        else:
            print("\n", "-"*20, "Invalid date, repeat input", "-"*20)



def get_data_employee():
    while True:
        last_name = input("Inter last_name: ")
        if exception_name(last_name):
            break
        else:
            print("\n", "-"*20, "Invalid name, repeat input", "-"*20)
    while True:
        first_name = input("Inter first_name: ")
        if exception_name(first_name):
            break
        else:
            print("\n", "-"*20, "Invalid name, repeat input", "-"*20)
    while True:
        department = input("Inter department: ")
        if exception_name(department):
            break
        else:
            print("\n", "-"*20, "Invalid department, repeat input", "-"*20)
    while True:
        profession = input("Inter profession: ")
        if exception_name(profession):
            break
        else:
            print("\n", "-"*20, "Invalid profession, repeat input", "-"*20)
    while True:
        salary = input("Inter salary: ")
        if exception_number(salary):
            break
        else:
            print("\n", "-"*20, "Invalid salary, repeat input", "-"*20)
    while True:
        date_employment = input("Inter date of employment: ")
        if exception_date(date_employment):
            break
        else:
            print("\n", "-"*20, "Invalid date_employment, repeat input", "-"*20)
    while True:
        date_dismissal = input(
            "Inter  date_dismissal ('0' if he still works): ")
        if exception_date(date_dismissal):
            break
        else:
            print("\n", "-"*20, "Invalid date_dismissal, repeat input", "-"*20)
    r=input("If the entered data are correctly enter 1  else  0: ")
    if r=="0":
        return [0]
    
    res = [last_name, first_name, department, profession,
           salary, date_employment, date_dismissal]
    return res
