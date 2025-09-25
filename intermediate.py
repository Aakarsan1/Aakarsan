int1 = int(input("Give me number 1: "))
int2 = int(input("Give me number 2: "))
options = input("Do you want to /*+-? ")
if options == "/":
    div = print(int1/int2)
    print(div)
elif options == "*":
    mul = print(int1 * int2)
    print(mul)
elif options == "+":
    add = print(int1 * int2)
    print(add)
else:
    print(int1 - int2)

