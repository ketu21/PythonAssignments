#program that perform read and write operations on a file

def readfile(filename):
    '''this function reads from the file. The filename is passed as argument during functon call.'''
    f = open(filename,"r")
    lines = f.readline()
    print(lines)
    f.close()
    print("\nRead Operation Successful.")
    return


def writefile(filename,text):
    '''this function writes the data to the file. The filename and the Text are given as arguments during function call. 
    In This function the data present previously will be overwritten.'''
    f = open(filename,"w+")     #'w+' means open the file in write mode and if file not found then create a file.
    f.write(text)
    f.close()
    print("\nWrite Operation Successful.")
    return


def appendfile(filename,text):
    '''this function appends the data to the file. The filename and the Text are given as arguments during function call.'''
    f = open(filename, "a+")  # 'a+' means open the file in append mode and if file not found then create a file.
    f.write(text)
    f.close()
    print("\nAppend Operation Successful.")
    return

if __name__ == "__main__":
    i=True
    while(i):
        print("File Operations"
              "\nTo read from file enter 1."
              "\nTo write to a file enter 2."
              "\nTo append to a file enter 3."
              "\nTo exit enter 4.")
        choice = eval(input("\nYour choice : "))
        if choice == 1:
            filename = input("Enter the file name : ")
            readfile(filename)
        elif choice == 2:
            filename = input("Enter the file name : ")
            textvalue = input("Enter the data to be written.")
            writefile(filename,textvalue)
        elif choice == 3:
            filename = input("Enter the file name : ")
            textvalue = input("Enter the data to be appended.")
            appendfile(filename,textvalue)
        elif choice == 4:
            i=False
        else:
            print("Enter from the options given.")
print("Program Successful")
