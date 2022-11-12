# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
import os.path

f_read_data = "rle_data_for.txt"
f_coded_data = "rle_coded_data.txt"
f_decoded_data = "rle_decoded_data.txt"


# f_read_data=input("Enter the name of the file with the text: ")
# if not os.path.isfile(f_read_data):
#     exit("указан несуществующий файл с данными")

# f_coded_data = input("Enter the file name to record: ")
# f_decoded_data = input("Enter the name of the file to decode: ")


def read_file(filename):  # чтение данных из файла--------------------------------------------------
    with open(filename, "r", encoding="utf-8") as my_f:
        data = [_.replace("\n", '') for _ in my_f.readlines()]
    return data
# end ------------------------------------------------------------------------------------------------



def compression_data(data):  # кодирование данных --------------------------------------------------
    res = []
    for stroke in data:
        j = 0
        temp_list = []
        while j < len(stroke):
            count = 1
            k = j
            while k < len(stroke)-1:
                if stroke[k] == stroke[k+1]:
                    count += 1
                    k += 1
                else:
                    break
            temp_list.append(f"{count}{stroke[k]}")
            j += count
        res.append("".join(temp_list))
    return res
# end ------------------------------------------------------------------------------------------------


def record_data_in_file(filename, c_data):  # запись кодированных данных в файл
    with open(filename, "w", encoding="utf-8") as my_f:
        [my_f.write(i+"\n") for i in c_data]
    return print("данные записаны в файл ", filename)
# end ------------------------------------------------------------------------------------------------


def decod_data(data):  # декодирование данных ------------------------------------------------------
    out_data = []
    for srtoke in data:
        len_stroke = len(srtoke)
        i = 0
        str = ""
        data_str = ""
        while i < len_stroke:
            s_int = ""
            while i < len_stroke:
                if srtoke[i].isdigit():
                    s_int += srtoke[i]
                    i += 1
                else:
                    break
            if s_int != '':
                data_str += srtoke[i]*int(s_int)
            i += 1
        out_data.append(data_str)
    return out_data
# end ------------------------------------------------------------------------------------------------

print("\n" * 20)
r_data = read_file(f_read_data)
print("Исходные данные из файла", f"{f_read_data}" )
print(r_data)

c_data = compression_data(r_data)
print()
print("Кодированные данные для записи в файл")
print(c_data)
record_data_in_file(f_coded_data, c_data)

print()
print("Кодированные данные прочитанные из файла", f"{f_coded_data}")
с_data2 = read_file(f_coded_data)
print(с_data2)

dec_data = decod_data(с_data2)
print()
print("декодированные данные")
print(dec_data)


record_data_in_file(f_decoded_data, dec_data)
