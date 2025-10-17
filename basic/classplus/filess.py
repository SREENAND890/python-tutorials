try:
    fname=input("enter file name:")
    with open(fname,"r") as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("error:FileNotFoundError")