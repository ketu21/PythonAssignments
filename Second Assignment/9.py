#program to insert elements in list.

#creating empty list.
values = []
#get the number of elements to be inserted.
number = eval(input("enter the number og elements to be inserted : "))

for i in range(number):
    values.append(input("Enter any value "))

print(values)