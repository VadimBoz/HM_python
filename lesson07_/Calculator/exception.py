
def exception_kind(value) -> bool:
    if value.isdigit() and (int(value) in [1,2,3]):
        return True
    else: 
        return False

def exception_actions(value) -> bool:
    if value.isdigit() and 0<int(value)<12:
        return True
    else: 
        return False

def exception_number(value) -> bool:
    if value.replace(" ", '').replace(".", '').replace(",", '').replace("-", '').isdigit():
        return True
    else: 
        return False