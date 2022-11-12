import math

def log10(x):
    return math.log(x)

def mult(x,y): 
    return x * y

def div(x,y): 
    return x / y

def sum(x,y): 
    return x + y

def dif(x,y): 
    return x - y

def int_div(x,y): 
    return x // y

def int_mod(x,y): 
    return x % y

def exponentiation(x,y):
    return x**y

def sqrt(x): 
    return x**0.5

def factorial(x):
    if x < 1:
       return 1
    else:
        return  x * factorial(x - 1)

def exp(x):
    return 2.7182818284**x