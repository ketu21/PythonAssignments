#program to find the factorial of a number.

number = eval(input("Enter any number : "))
print(("The factors of",number,"are :"))
#all the numbers that can divide the given number are the factors of that given number.

for i in range(1,number+1):
    if number % i == 0:
        print(i)