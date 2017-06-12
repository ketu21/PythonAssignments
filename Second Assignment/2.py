#Program to find greater number of the three numbers.

#creating an empty list to store the values
values = []
#Loop to take 3 input from the user
for i in range(3):
    values.append(eval(input("Enter any number : ")))

if values[0] > values[1] and values[0] > values[2]:
    print("The Greatest value is ", values[0])
elif values[1] > values[2]:
    print("The Greatest value is ", values[1])
else:
    print("The Greatest value is ", values[2])