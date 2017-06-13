# 1. program to show usage of class and object.
# 2. program to show usage of inheritance
# 4. program to show usage of constructor
# 7.python script which has class having two below methods and access those methods in another class

class StringClass():
    '''This class is used to get string input from user and then print it when function is called'''

    #defining the constructor to initialize the value equal to null
    def __init__(self):
        self.value = ''


    def getString(self):
        '''this function gets the user input and stores it to class variable'''
        self.value = input("Enter any string :")
        return


    def printString(self):
        '''this method prints the string value in all upper case characters'''
        print(self.value.upper())       #upper() is a inbuilt method that converts all characters to upper case.
        return

#implementing the inheritance concept
class SubStringClass(StringClass):
    '''this class inherits the StringClass. So it can now access the methods of StringClass.'''
    def printClass(self):
        print("This is Child Class. And program is successful.")

if __name__ =="__main__":
    obj1 = SubStringClass()     #creating object for SubStringClass
    obj1.getString()            #usning object of child class calling the method of parent class
    obj1.printString()
    obj1.printClass()
