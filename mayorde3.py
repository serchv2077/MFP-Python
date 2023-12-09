c=int(input("Cual es tu primer numero?"))
a=int(input("Cual es tu primer segundo?"))
d=int(input("Cual es tu primer tercer?"))

if c > a > d:
    print(c, a, d)

elif a > c >d:
    print(a, c, d)

elif d > a > c:
    print(d, a, c)