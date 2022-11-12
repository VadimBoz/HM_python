
def str_to_int_real(value): 
    res = float(value.replace(',', '.'))
    res = int(res) if res%1<0.001 else res 
    return res

  
def str_to_complex(value):
    value=value.replace(',', '.').strip()
    str_list=value.split(" ")
    res=complex(str_to_int_real(str_list[0]),str_to_int_real(str_list[1]))
    return res

