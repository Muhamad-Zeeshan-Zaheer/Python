a = float(input("Enter the number 1: "))
b = float(input("Enter the number 2: "))
c = float(input("Enter the number 3: "))
d = float(input("Enter the number 4: "))

if a > b and a > c and a > d:
    print("a is greatest")
elif b > a and b > c and b > d:
    print("b is greatest")
elif c > a and c > b and c > d:
    print("c is greatest")
else:
    print("d is greatest")
