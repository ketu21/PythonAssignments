#Python script to check if a given key already exists in a dictionary.
check = input("Enter the key to check : ")
values={'a':1,'b':2,'c':3,'d':4}
marker=False
for i in values.keys():
    if check == i:
        print("Key Matched.")
        marker = True
if marker == False:
    print("Key did not match.")


