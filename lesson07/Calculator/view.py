from exception import exception_kind
from exception import exception_actions
from exception import exception_number



def get_value_kind(message):
    while True:
        value=input(message)
        if exception_kind(value): 
            break
        else:
            print("-"*20, "Invalid number, repeat input")
    return int(value)
        

def get_value_actions(message):
    value=input(message)
    if exception_actions(value): 
        return int(value)
    else:
        print("\n","-"*20, "Invalid number, repeat input")
        return 0


def get_value_num(message):
    while True:
        value=input(message)
        if exception_number(value): 
            res = float(value.replace(',', '.'))
            res = int(res) if res%1<0.001 else res 
            break
        else:
            print("\n","-"*20, "Invalid number, repeat input")
    return res


def to_console(data):
    print()
    print('-'*30)
    print("Result =", data)
    print('-'*30)
