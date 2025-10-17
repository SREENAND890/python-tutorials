# single value in tuple
a=("apple")

# tuple to list
a=("apple","mango","orenge","banana")
print(a)
temp_list=(list(a))
print(type(temp_list))
temp_list[1]="greps"
print(temp_list)
a=(tuple(temp_list))
print(type(a))
print(a)
