from os import path


def print_csv():
    if path.isfile("staff.csv"):
        with open('staff.csv', 'r', encoding="utf-8") as file:
            [print(i.replace("\n", '')[:-1].split(";"))
             for i in file.readlines()]
            print()
            # print(data)
        return 1
    else:
        print("File not found, write the data to a file")
        return 0


def read_csv() -> list[str]:
    if path.isfile("staff.csv"):
        data = []
        with open('staff.csv', 'r', encoding="utf-8") as file:
            data = [(i.replace("\n", '')[:-1].split(";"))
                    for i in file.readlines()]
        return data
    else:
        print("File not found, previosly write the data to a file")
        return [0]



def change_info_file(id: str, s_n: str, last_name, first_name, department, profession, salary, date_employment, date_dismissal):
    new_str = '{0};{1};{2};{3};{4};{5};{6};{7};{8};\n'.format(id, s_n, last_name, first_name, department, profession, salary, date_employment, date_dismissal)
    if path.isfile("staff.csv"):
        with open('staff.csv', 'r', encoding="utf-8") as file1:
            data = file1.readlines()
            for i in range(len(data)):
                lst = data[i].replace("\n", '')[:-1].split(';')
                if lst[1] == s_n:
                    data[i] = new_str
                    break
        with open('staff.csv', 'w', encoding="utf-8") as file2:   
            file2.writelines(data)    
        print("Data added to staff.csv.csv")
    else:
        print("File not found, write the data to a file")
        return 0



def add_record(last_name, first_name, department, profession, salary, date_employment, date_dismissal):
    if not path.isfile("staff.csv"):
        print("file staff.csv not found, creating the new file staff.csv")
    with open('end_id.txt', 'r+', encoding="utf-8") as file_id:
        data = file_id.readlines()
        print(data)
        id = str(int(data[0].replace("\n", ""))+1)
        s_n = str(int(data[1].replace("\n", ""))+1)
        file_id.seek(0)
        file_id.write(id+"\n")
        file_id.write(s_n+"\n")
    with open('staff.csv', 'a', encoding="utf-8") as file:
        file.write('\n{0};{1};{2};{3};{4};{5};{6};{7};{8};'.format(
            id, s_n, last_name, first_name, department, profession, salary, date_employment, date_dismissal))
        print("Data added to staff.csv.csv")
