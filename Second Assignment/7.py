#program to check leap year.

year = eval(input("Enter any year: "))
# a year is leap year if it is perfectly divisible by 4 and if it is not a century year i.e ending with 00.
#if it is a century year and it is exactly divisible by 4 and 400 then it is a leap year.
if year % 4 == 0 and year % 100 == 0 and year % 400 ==0:
    print(year,"is a Leap Year.")
elif year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year.")
else:
    print(year, "is not a Leap Year.")