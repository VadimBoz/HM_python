from datetime import datetime
# from time import time

def log_data(n1, n2, op , res):
    time = datetime.now().strftime(' %d/%m/%Y %H:%M:%S')
    with open('log.txt', 'a', encoding="utf-8") as file:
        file.write('{0}"  "{1} (оператор № {3}) {2} = {4}\n'.format(time, n1, n2, op ,res))

