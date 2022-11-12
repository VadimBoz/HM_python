from view import get_value
from view import get_string
from view import get_telefone
from transfer_data import add_data_CSV
from transfer_data import add_data_txt
from transfer_data import read_txt
from transfer_data import read_csv


def start_menu():
    print("\n"*3)
    print('-'*30)
    print("Тelephone Directory")
    print('-'*30)
    print()
    print(  '1 – Record new data in SVC\n'
            '2 – Record new data in TXT\n'
            '3 - Read from SVC\n'
            '4 - Read from TXT\n'
            '5 – Exit' )
    while True:
        choice_start = get_value("Input item number: ")
        if choice_start != 0:
            if choice_start == 5:
                exit("The program is completed")
            break
    return choice_start



def record_in_csv():
    first_name = get_string('Input first name: ')
    last_name = get_string('Input last name: ')
    tel = get_telefone('Input telefon in format "+х-xxx-xxx-xx-xx": ')
    add_data_CSV(first_name, last_name, tel)

def record_in_txt():
    first_name = get_string('Input first name: ')
    last_name = get_string('Input last name: ')
    tel = get_telefone('Input telefon in format "+х-xxx-xxx-xx-xx": ')
    add_data_txt(first_name, last_name, tel)



def action():
    while True:
        choice_st=start_menu()
        match choice_st:
            case 1:
                record_in_csv()
            case 2:
                record_in_txt()
            case 3:
                read_csv()
            case 4:
                read_txt()
            case 5:
                exit("The program is completed")

