#calculator program.

a = eval(input("Enter first value"))
c = input("Enter the operator")
b = eval(input("Enter the second value"))

if c == '+':
    print(a+b)
elif c =='-':
    print(a-b)
elif c =='*':
    print(a*b)
elif c =='/':
    print(a/b)
elif c =='%':
    print(a%b)
else:
    print("Unable to identify the operator.")
