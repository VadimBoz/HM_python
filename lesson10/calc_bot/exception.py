
def exception_number(value) -> bool:
    if value.replace(" ", '').replace(".", '').replace(",", '').replace("-", '').isdigit():
        return True
    else: 
        return False
