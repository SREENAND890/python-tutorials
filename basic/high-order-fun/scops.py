x=10 #global_function
def out_fun():#outer_function
    x=5
    def inner_fun():#inner_fun
        x=2
        print(x) #OUTPUT:2
    inner_fun()
out_fun()
print(x)  #OUT PUT:10      


