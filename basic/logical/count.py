# a="the cat and the dog"
# print("the",a.count('the'),"cat",a.count('cat'),'and',a.count('and'),"dog",a.count("dog"))
#1
lis=[10,2,45,70,45,60,90,100,45,7]
a=max(lis)
print(a)
b=min(lis)
print(b)

#2
c=lis[::-1]
print(c)

#3
d=lis.count(45)
print(d)


#4
set1=(set(lis))
list1=(list(set1))
print(list1)

#5
li=[1,2,3,4,5]
li1=["a","b","c","d"]
li2=li+li1
print(li2)

#6
lis=[1,2,90,100,57]
lis.sort()
print(lis[-2])


#7
lis2="malayalam"


if lis2 == lis2[::-1]:
    print("palindrom")
elif lis2 !=lis2 [::-1]:
    print("not palidrom")    

#8


#9
a=["apple","mango","orenge","banana"]
temp_list=(tuple(a))
print(temp_list)
a=(list(temp_list))
print(a)

#10



#13
t=("orenge","apple","mango")

for x in t:
    print(x)