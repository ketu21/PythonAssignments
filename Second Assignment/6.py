#program to check if a number is positive,negative or zero.

number = eval(input("Enter any number: "))
#number is positive if it is greater then 0
#number is negative if it is less then 0
if number >0:
    print("The number is positive.")
elif number <0:
    print("The number is negative.")
else:
    print("The number is 0.")