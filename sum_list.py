def s_list(lst):
    if not lst:
        return 0
    else:
        return lst[0]+s_list(lst[1:])
print(s_list([1,2,3,4,5]))