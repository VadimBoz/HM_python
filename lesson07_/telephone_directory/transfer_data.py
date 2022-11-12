
from os import path


def add_data_CSV(first_name, last_name, tel):
    with open('telefone.csv', 'a', encoding="utf-8") as file:
        file.write('{0};{1};{2}\n'.format(first_name, last_name, tel))
    print("Data added to telefone.csv")


def add_data_txt(first_name, last_name, tel):
    data = [("fist name:", first_name),
            ("last name:", last_name), ("telefone:", tel)]
    with open('telefone.txt', 'a', encoding="utf-8") as file:
        [file.write(f"{data[i][0]}: {data[i][1]}\n") for i in range(len(data))]
        file.write(" \n")
    print("Data added to telefone.txt")


def read_txt():
    if path.isfile("telefone.txt"):
        with open('telefone.txt', 'r', encoding="utf-8") as txt_file:
            print()
            [print(i[:-1]) for i in txt_file.readlines()]
    else:
        print("File not found, write the data to a file")


def read_csv():
    if path.isfile("telefone.csv"):
        with open('telefone.csv', 'r', encoding="utf-8") as file:
            [print(i[:-1]) for i in file.readlines()]
            print()
            # print(data)
        return 1
    else:
        print("File not found, write the data to a file")
        return 0



