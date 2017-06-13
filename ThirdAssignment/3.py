#a python script that performs creation of table and insert, select, delete and update operations on that created table

import MySQLdb

def createtable():
    # Open database connection
    db = MySQLdb.connect("localhost", "USERNAME", "PASWORD", "DATABASENAME")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Drop table if it already exist using execute() method.
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    # Create table as per requirement
    sql = """CREATE TABLE EMPLOYEE (
             FIRST_NAME  CHAR(50),
             LAST_NAME  CHAR(50),
             AGE INT,  
             SEX CHAR(1) )"""

    cursor.execute(sql)
    # disconnect from server
    db.close()

def insertrecord():
    # Open database connection
    db = MySQLdb.connect("localhost", "USERNAME", "PASWORD", "DATABASENAME")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
             LAST_NAME, AGE, SEX)
             VALUES ('Ketul', 'Patel', 25, 'M')"""
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()

def readrecord():
    db = MySQLdb.connect("localhost", "USERNAME", "PASWORD", "DATABASENAME")

    cursor = db.cursor()

    sql = "SELECT * FROM EMPLOYEE WHERE AGE > '%d'" % (20)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            # Now print fetched result
            print("fname={0},lname={1},age={2},sex={3}".format(fname, lname, age, sex))
    except:
        print ("Error: unable to fecth data")

    db.close()

def deletedata():
    db = MySQLdb.connect("localhost", "USERNAME", "PASWORD", "DATABASENAME")

    cursor = db.cursor()

    # Prepare SQL query to DELETE required records
    sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (50)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()

def updaterecord():
    db = MySQLdb.connect("localhost", "USERNAME", "PASWORD", "DATABASENAME")
    cursor = db.cursor()

    # Prepare SQL query to UPDATE required records
    sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')


    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()


createtable()
insertrecord()
readrecord()
updaterecord()
deletedata()

#I actually dont have MySql Database on my mac so just wrote the program as per my knowledge.
#You might need to provide Username User Password and Database Name
