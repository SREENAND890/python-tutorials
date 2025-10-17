# def a(**kwargs):
#     for key,value in kwargs.items():
#         print(f'{key}:{value}')


# a(name="john",age=30,city="newyork")

# def ab(**kwargs):
#     return f'name is {kwargs['name']} and my age is {kwargs['age']} and my place is {kwargs['place']}'
# print(ab(name="john",age=30,place="new york"))

# def key(**abc):
#     print(abc)
# key(a=1,b=2,c=3)    

def info(*args, **kwargs):
    print("unaiskaa",args)
    print("vengat_unais",kwargs)

info(1,2,3,name="john",age=30)


def info(abc,*args, **kwargs):
    print("unais",abc)
    print("unaiskaa",args)
    print("vengat_unais",kwargs)

info(1,2,3,name="john",age=30)

