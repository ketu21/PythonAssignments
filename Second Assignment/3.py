#program to find prime number.
number = eval(input("Enter any number : "))
#number is prime is it is divilible by 1 or itself only.
for i in range(2,number):
    if number % i == 0:
        print("The number is not prime.")

print("The number is prime.")
