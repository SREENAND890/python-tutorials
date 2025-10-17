try:
    num=int(input("enter a num:"))
    result=10/num
except ZeroDivisionError:
    print("Division by zero is not allowed!")
else:
    print(f"the result is {result}")
finally:
    print("this will always be printed.")
