#program to swap(exchange value of two variables) without using third variable.

a = 10
b = 12
#when we want more then one values to be printed we can use .format() to assign the order.
print("Before Swapping a={0} and b={1}".format(a,b))
#swapping the values
a,b=b,a
print("After Swapping a={0} and b={1}".format(a,b))