# a = "hello world this is js"
# b = a.replace(" ", "-")
# print(b)

# for a in range(1,7):
#     print("*" *a)
# print("")
# for a in range(6,0,-1):
#     print("*" *a)


# st=str(input("enter first:"))
# sr=str(input("enter second:"))

# if sorted(st)== sorted(sr):
#     print("string are anagrams")
# else:
#     print("string are not anagrams")

def decimal_to_binary(n):
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary if binary != "" else "0"


decimal_number = 7
print("Decimal number:", decimal_number)
print("Binary of", decimal_number, "is", decimal_to_binary(decimal_number))



