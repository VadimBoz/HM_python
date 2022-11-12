def exception_menu_item(value) -> bool:
    if value.isdigit() and (int(value) in [1,2,3,4,5]):
        return True
    else: 
        return False

def exception_telefone(value) -> bool:
    find_plus=value.replace(" ", '').find("+")
    value=value.replace(" ", '').replace("-", '').replace("+", '')
    l = len(value)
    if value.isdigit() and l==11 and find_plus==0:
        return True
    else: 
        return False


def exception_name(message):
    for i in "!@#$%^&/*?<>1234567890'\"":
            if message.find(i)>=0:
               return False
    else:
        return True