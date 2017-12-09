
a = int(input("Enter 1st number "))
b = int(input("Enter 2d number "))
c = int(input("Enter 3th number "))

l = [a, b, c]

if a==b==c:
    print("3")
elif a==b!=c or b==c!=a or a==c!=b:
    print("2")
else:
    print("0")
