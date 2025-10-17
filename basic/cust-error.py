class NegativeNumberError(Exception):
    pass

def checkNum(num):
    if num<0:
        raise NegativeNumberError("neg num are not allowed!")
    else:
        print(f"result is {num}")
    
try:
    checkNum(-10)
except NegativeNumberError as e:
    print(e)