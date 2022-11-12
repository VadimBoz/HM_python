def exception_menu_item(value) -> bool:
    if value.isdigit() and (int(value) in [1, 2, 3, 4, 5, 6, 7, 8, 9]):
        return True
    else:
        return False

def exception_name(message):
    for i in "!@#$%^&/*?<>1234567890'\"":
            if message.find(i)>=0:
               return False
    else:
        return True


def exception_servise_number(message):
    value = message.replace(" ", '')
    if value.isdigit() and len(value)==4:
        return True
    else: 
        return False

def exception_number(value):
    value = value.replace(" ", '')
    if value.isdigit():
        return True
    else: 
        return False

def exception_date(value):
    value = value.replace(" ", '').replace(".", '')
    if value=="0":
        return True
    if value.isdigit():
        if 0<int(value[:2])<32 and 0<int(value[2:4])<13 and 1900<int(value[4:])<2024:
            return True
    else: 
        return False