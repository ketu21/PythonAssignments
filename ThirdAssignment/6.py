#program to find all numbers divisible by 5 between (2000 and 3000) and insert those elements in a list and then print them

#below is the use of list comprehension whih makes it easier and reduces the lie of code
values = [i for i in range(2001,3000) if i % 5 == 0]
print(values)

#below is by using for loop concept
values2 = []
for i in range(2001,3000):
    if i % 5 == 0:
        values2.append(i)
print(values2)

