from exception import exception_menu_item
from exception import exception_telefone
from exception import exception_name

def get_value(message):
    while True:
        value=input(message)
        if exception_menu_item(value): 
            return int(value)
        else:
            print("\n","-"*20, "Invalid number, repeat input","-"*20)
            return 0
    


def get_string(message):
    while True:
        value=input(message)
        if exception_name(value):
            return value.replace(" ",'')
        else:
            print("\n","-"*20, "Invalid name, repeat input","-"*20)
         
   


def get_telefone(message):
    while True:
        value = input(message)
        if exception_telefone(value):
            return value.replace(" ",'')
        else:
            print("\n","-"*20, "Invalid number, repeat input","-"*20)
