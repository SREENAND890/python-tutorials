#inter section method print item that items in both set
a={1,2}
b={1,2,3,4}
c=a & b
print(c)


# - method
a={1,2,}
b={1,2,3,4}
c=b - a
print(c)

#^ method

a={1,2,5}
b={1,2,3,4}
c=a ^ b
print(c)


a={1,2}
b={1,2,3,4}
print(a.issubset(b))


a={1,2}
b={1,2,3,4}
print(a.issuperset(b))

