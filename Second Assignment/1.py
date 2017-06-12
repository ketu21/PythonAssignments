#Program to check if entered number is even or odd.

#eval is used to consider the type of the value entered. Here to make nmber as integer instead of string
number = eval(input("Enter a number"))
if number %2 == 0:
    print("The number ",number," is Even.")
else:
    print("The number ",number," is Odd.")