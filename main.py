# ===================== Module: Book =====================

import mysql.connector
from mysql.connector import errorcode, connection
from datetime import date, datetime, timedelta
import os
import platform


def clrscreen():
    if platform.system() == "Windows":
        os.system('cls')


def insertB():
    try:
        cnx = connection.MySQLConnection(
            user='root',
            password='feedlight',
            host='localhost',
            database='Library'
        )
        Cursor = cnx.cursor()

        Bno = input("Enter Book Code : ")
        bna = input("Enter Book Name : ")
        Author = input("Enter Book Author's Name : ")
        price = int(input("Enter Book Price : "))
        publ = input("Enter Publisher of Book : ")
        qty = int(input("Enter Quantity purchased : "))

        print("Enter Date of Purchase ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))

        Qry = "INSERT INTO BookRecord VALUES (%s,%s,%s,%s,%s,%s,%s)"
        data = (Bno, bna, Author, price, publ, qty, date(YY, MM, DD))

        Cursor.execute(Qry, data)
        cnx.commit()

        Cursor.close()
        cnx.close()

        print("Record Inserted")
        input("Press Enter to continue")
        clrscreen()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


def display():
    try:
        cnx = connection.MySQLConnection(
            user='root',
            password='feedlight',
            host='localhost',
            database='Library'
        )
        Cursor = cnx.cursor()

        Cursor.execute("SELECT * FROM BookRecord")
        rec = Cursor.fetchall()
        Rt = 0

        for (Bno, Bname, Author, price, publ, qty, dop) in rec:
            Rt += 1
            print("=" * 60)
            print("Book Code :", Bno)
            print("Book Name :", Bname)
            print("Author :", Author)
            print("Price :", price)
            print("Publisher :", publ)
            print("Quantity :", qty)
            print("Purchased On :", dop)
            print("=" * 60)

        input("Press Enter to continue")
        clrscreen()
        print(Rt, "Record(s) found")

        Cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        print(err)


def delB():
    try:
        cnx = connection.MySQLConnection(
            user='root',
            password='feedlight',
            host='localhost',
            database='Library'
        )
        Cursor = cnx.cursor()

        bno = int(input("Enter Book Code to delete : "))
        Qry = "DELETE FROM BookRecord WHERE Bno=%s"
        Cursor.execute(Qry, (bno,))
        cnx.commit()

        print(Cursor.rowcount, "Record(s) Deleted Successfully")

        Cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        print(err)


def SearchB():
    try:
        cnx = connection.MySQLConnection(
            user='root',
            password='feedlight',
            host='localhost',
            database='Library'
        )
        Cursor = cnx.cursor()

        bno = input("Enter Book Code to search : ")
        Cursor.execute(
            "SELECT * FROM BookRecord WHERE Bno=%s",
            (bno,)
        )
        hall = Cursor.fetchall()

        Re = 0
        for (Bno, Bname, Author, price, publ, qty, dop) in hall:
            Re += 1
            print("=" * 60)
            print(Bno, Bname, Author, price, publ, qty, dop)
            print("=" * 60)

        input("Press Enter to continue")
        clrscreen()
        print(Re, "Record(s) found")

        Cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        print(err)


def UpdateB():
    try:
        cnx = connection.MySQLConnection(
            user='root',
            password='feedlight',
            host='localhost',
            database='Library'
        )
        Cursor = cnx.cursor()

        bno = input("Enter Book Code to update : ")
        bname = input("Enter Book Name : ")
        Auth = input("Enter Author Name : ")
        price = int(input("Enter Book Price : "))
        publ = input("Enter Publisher : ")
        qty = int(input("Enter Quantity : "))

        print("Enter Date of Purchase")
        DD = int(input("Date : "))
        MM = int(input("Month : "))
        YY = int(input("Year : "))

        Qry = """
        UPDATE BookRecord
        SET bname=%s, Author=%s, price=%s, publ=%s, qty=%s, dop=%s
        WHERE Bno=%s
        """

        data = (bname, Auth, price, publ, qty, date(YY, MM, DD), bno)
        Cursor.execute(Qry, data)
        cnx.commit()

        print(Cursor.rowcount, "Record(s) Updated Successfully")

        Cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        print(err)
# ===================== Module: Member =====================

import mysql.connector
from mysql.connector import errorcode, connection
from datetime import date, datetime, timedelta
import os


def clrscreen():
    print('\n' * 5)


def insertM():
    try:
        cnx = connection.MySQLConnection(
            user='root',
            password='feedlight',
            host='localhost',
            database='Library'
        )
        Cursor = cnx.cursor()

        mno = input("Enter Member Code : ")
        mname = input("Enter Member Name : ")
        mob = input("Enter Member Mobile No. : ")

        print("Enter Date of Membership")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))

        address = input("Enter Member Address : ")

        Qry = "INSERT INTO Mem VALUES (%s,%s,%s,%s,%s)"
        data = (mno, mname, mob, date(YY, MM, DD), address)

        Cursor.execute(Qry, data)
        cnx.commit()

        Cursor.close()
        cnx.close()

        print("Record Inserted")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


def display():
    try:
        os.system('cls')

        cnx = connection.MySQLConnection(
            user='root',
            password='feedlight',
            host='localhost',
            database='Library'
        )
        Cursor = cnx.cursor()

        Cursor.execute("SELECT * FROM Mem")

        for (Mno, Mname, MOB, dom, address) in Cursor:
            print("=" * 60)
            print("Member Code :", Mno)
            print("Member Name :", Mname)
            print("Mobile No :", MOB)
            print("Date of Membership :", dom)
            print("Address :", address)
            print("=" * 60)

        Cursor.close()
        cnx.close()
        input("Press Enter to continue")

    except mysql.connector.Error as err:
        print(err)


def delM():
    try:
        cnx = connection.MySQLConnection(
            user='root',
            password='feedlight',
            host='localhost',
            database='Library'
        )
        Cursor = cnx.cursor()

        mno = input("Enter Member Code to delete : ")

        Qry = "DELETE FROM Mem WHERE mno=%s"
        Cursor.execute(Qry, (mno,))
        cnx.commit()

        print(Cursor.rowcount, "Record(s) Deleted Successfully")

        Cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        print(err)


def SearchM():
    try:
        cnx = connection.MySQLConnection(
            user='root',
            password='feedlight',
            host='localhost',
            database='Library'
        )
        Cursor = cnx.cursor()

        mnm = input("Enter Member Name to search : ")
        Qry = "SELECT * FROM Mem WHERE mname=%s"
        Cursor.execute(Qry, (mnm,))

        Re = 0
        for (Mno, Mname, MOB, dom, address) in Cursor:
            Re += 1
            print("=" * 60)
            print("Member Code :", Mno)
            print("Member Name :", Mname)
            print("Mobile No :", MOB)
            print("Date of Membership :", dom)
            print("Address :", address)
            print("=" * 60)

        clrscreen()
        print(Re, "Record(s) found")

        Cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        print(err)
# ===================== MODULE: Issue =====================

import mysql.connector
from mysql.connector import errorcode, connection
from datetime import date
import os


def clrscreen():
    print('\n' * 5)


def issueIB():
    try:
        cnx = connection.MySQLConnection(
            user='root',
            password='root',
            host='localhost',
            database='Library'
        )
        Cursor = cnx.cursor()

        bno = input("Enter Book Code to issue : ")
        mno = input("Enter Member Code : ")

        print("Enter Date of Issue")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))

        Qry = "INSERT INTO Issue(bno,mno,doi) VALUES (%s,%s,%s)"
        data = (bno, mno, date(YY, MM, DD))

        Cursor.execute(Qry, data)
        cnx.commit()

        Cursor.close()
        cnx.close()

        print("Record Inserted")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


def returnIB():
    try:
        cnx = connection.MySQLConnection(
            user='root',
            password='root',
            host='localhost',
            database='Library'
        )
        Cursor = cnx.cursor()

        bno = input("Enter Book Code to return : ")
        mno = input("Enter Member Code : ")
        retDate = date.today()

        Qry = "UPDATE Issue SET dor=%s WHERE bno=%s AND mno=%s"
        Cursor.execute(Qry, (retDate, bno, mno))
        cnx.commit()

        print(Cursor.rowcount, "Record(s) Updated Successfully")

        Cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


def ShowIB():
    try:
        os.system('cls')

        cnx = connection.MySQLConnection(
            user='root',
            password='root',
            host='localhost',
            database='Library'
        )
        Cursor = cnx.cursor()

        query = """
        SELECT B.bno, B.bname, M.mno, M.mname, I.doi, I.dor
        FROM BookRecord B, Issue I, Mem M
        WHERE B.bno = I.bno AND I.mno = M.mno
        """

        Cursor.execute(query)
        hall = Cursor.fetchall()

        for (Bno, Bname, Mno, Mname, doi, dor) in hall:
            print("=" * 60)
            print("Book Code :", Bno)
            print("Book Name :", Bname)
            print("Member Code :", Mno)
            print("Member Name :", Mname)
            print("Date of Issue :", doi)
            print("Date of Return :", dor)
            print("=" * 60)

        Cursor.close()
        cnx.close()
        input("Press Enter to continue")

    except mysql.connector.Error as err:
        print(err)
# ===================== MODULE: MenuL =====================

import Book
import Member
import Issue


def MenuB():
    while True:
        Book.clrscreen()

        print("\t\t\t Book Record Management\n")
        print("==============================================================")
        print("1. Add Book Record")
        print("2. Display Book Records")
        print("3. Search Book Record")
        print("4. Delete Book Record")
        print("5. Update Book Record")
        print("6. Return to Main Menu")
        print("==============================================================")

        choice = int(input("Enter Choice between 1 to 6 > : "))

        if choice == 1:
            Book.insertB()
        elif choice == 2:
            Book.display()
        elif choice == 3:
            Book.SearchB()
        elif choice == 4:
            Book.delB()
        elif choice == 5:
            Book.UpdateB()
        elif choice == 6:
            return
        else:
            print("Wrong Choice. Enter again.")

        input("Enter any key to continue")


def MenuM():
    while True:
        Book.clrscreen()

        print("\t\t\t Member Record Management\n")
        print("==============================================================")
        print("1. Add Member Record")
        print("2. Display Member Records")
        print("3. Search Member Record")
        print("4. Delete Member Record")
        print("5. Update Book Record")
        print("6. Return to Main Menu")
        print("==============================================================")

        choice = int(input("Enter Choice between 1 to 6 > : "))

        if choice == 1:
            Member.insertM()
        elif choice == 2:
            Member.display()
        elif choice == 3:
            Member.SearchM()
        elif choice == 4:
            Member.delM()
        elif choice == 5:
            print("No such Function")
        elif choice == 6:
            return
        else:
            print("Wrong Choice. Enter again.")

        input("Enter any key to continue")


def MenuI():
    while True:
        Book.clrscreen()

        print("\t\t\t Issue / Return Management\n")
        print("==============================================================")
        print("1. Issue Book")
        print("2. Display Issued Book Records")
        print("3. Return Issued Book")
        print("4. Return to Main Menu")
        print("==============================================================")

        choice = int(input("Enter Choice between 1 to 4 > : "))

        if choice == 1:
            Issue.issueIB()
        elif choice == 2:
            Issue.ShowIB()
        elif choice == 3:
            Issue.returnIB()
        elif choice == 4:
            return
        else:
            print("Wrong Choice. Enter again.")

        input("Enter any key to continue")
# ===================== MODULE: Library =====================

import MenuL
import Book
import Member
import Issue

while True:
    Book.clrscreen()

    print("\t\t\t Library Management\n")
    print("==============================================================")
    print("1. Book Management")
    print("2. Members Management")
    print("3. Issue / Return Book")
    print("4. Exit")
    print("==============================================================")

    choice = int(input("Enter Choice between 1 to 4 : "))

    if choice == 1:
        MenuL.MenuB()

    elif choice == 2:
        MenuL.MenuM()

    elif choice == 3:
        MenuL.MenuI()

    elif choice == 4:
        break

    else:
        print("Wrong Choice... Enter again")

    input("Enter any key to continue")
# ===================== MODULE: runonce =====================

import mysql.connector
from mysql.connector import connection


def db():
    cnx = connection.MySQLConnection(
        user='root',
        password='root',
        host='localhost'
    )
    Cursor = cnx.cursor()
    Cursor.execute("CREATE DATABASE Library")
    cnx.close()


db()


def table():
    cnx = connection.MySQLConnection(
        user='root',
        password='root',
        host='localhost',
        database='Library'
    )
    Cursor = cnx.cursor()

    Cursor.execute("""
    CREATE TABLE BookRecord(
        Bno INT,
        bname VARCHAR(255),
        author VARCHAR(255),
        price INT,
        publ VARCHAR(255),
        qty INT,
        dop DATE
    )
    """)

    Cursor.execute("""
    CREATE TABLE Mem(
        mno INT,
        mname VARCHAR(255),
        mob VARCHAR(255),
        dom DATE,
        address VARCHAR(255)
    )
    """)

    Cursor.execute("""
    CREATE TABLE Issue(
        bno INT,
        mno INT,
        doi DATE,
        dor DATE
    )
    """)

    cnx.commit()
    cnx.close()


table()


def val():
    cnx = connection.MySQLConnection(
        user='root',
        password='root',
        host='localhost',
        database='Library'
    )
    Cursor = cnx.cursor()

    Cursor.execute(
        "INSERT INTO BookRecord VALUES "
        "(1,'Mein Kampf','Adolf Hitler',670,'AGK',78,'2013-12-12')"
    )

    Cursor.execute(
        "INSERT INTO BookRecord VALUES "
        "(2,'Adventures of Tom Sawyer','Mark Twain',400,'YK',13,'2003-05-24')"
    )

    Cursor.execute(
        "INSERT INTO BookRecord VALUES "
        "(3,'Agni Veena','Kazi Nasrul Islam',590,'mnm pblctions',53,'2002-03-19')"
    )

    Cursor.execute(
        "INSERT INTO Mem VALUES "
        "(991,'Arun','8822934287','2010-12-23',"
        "'No. 1, New Bangaru Naidu Colony, K.K. Nagar (West), Chennai - 600078')"
    )

    Cursor.execute(
        "INSERT INTO Mem VALUES "
        "(994,'Harish','9376652876','2009-11-25',"
        "'No. 17, Velmurugan Colony, Vadapalani, Chennai - 600026')"
    )

    Cursor.execute(
        "INSERT INTO Mem VALUES "
        "(993,'Alister','9976687567','2003-05-18',"
        "'21, Sabari Street, Nesapakkam, K.K. Nagar West, Chennai - 600078')"
    )

    Cursor.execute(
        "INSERT INTO Issue(bno,mno,doi) VALUES (3,993,'2009-11-25')"
    )

    cnx.commit()
    cnx.close()


val()