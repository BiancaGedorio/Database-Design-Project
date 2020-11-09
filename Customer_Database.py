# Database Design Project 2020
# Author: Bianca Gedorio
# Student No: R00164040
# 01/12/2020

import pyodbc

# Connecting client and database server using ODBC
db = pyodbc.connect('DRIVER={MySQL ODBC 8.0 Unicode Driver};'
                    'User=root;'
                    'Password=Bi@nc@joie123..;'
                    'Server=localhost;'
                    'Database=project_database;'
                    )

cursor = db.cursor()
# Creating the table in the database
"""
sql = ("Create Table customers ("fname char(15),"
       "lname char(15),"
       "tel_no int(11) NOT NULL,"
       "email varchar(30)
       "c_no int PRIMARY KEY NOT NULL AUTO_INCREMENT;"
       )
cursor.execute(sql)
"""


# Shows each row in the customer table
def display():
    try:
        cursor.execute("select * from customers;")
        for x in cursor:
            print(x)
    except (ValueError, pyodbc.ProgrammingError) as e:
        print(e)
        return None


# Values are saved in the database
def insert_customer():
    try:
        insert = "INSERT INTO customers (c_no, fname, lname, tel_no, email) VALUES (?, ?, ?, ?, ?)"
        values = insert_values()
        # Executing command and values
        cursor.execute(insert, values)
        # Store values  in Database
        db.commit()
        print('Information stored successfully.')
        cursor.close()
    except (ValueError, pyodbc.ProgrammingError, pyodbc.IntegrityError, pyodbc.Error) as e:
        print(e)
        return None


# Input values in INSERT
def insert_values():
    print("\t\tPlease fill in the Details\n")
    c_no = read_id()
    f_name = read_firstname()
    l_name = read_lastname()
    tel_no = read_tel()
    email = str(input("\tEmail: "))
    return c_no, f_name, l_name, tel_no, email


# Error Handling - Letters Only
def read_nonempty_alphabetical_string(prompt):
    while True:
        s = input(prompt)
        s_with_no_spaces = s.replace(' ', '')
        if len(s_with_no_spaces) > 0 and s_with_no_spaces.isalpha():
            break
        else:
            print("LETTER VALUES Only")
    return s


# User Input (First Name)
def read_firstname():
    f = read_nonempty_alphabetical_string("\tFirst Name: ")
    return f


# User Input (Last Name)
def read_lastname():
    ln = read_nonempty_alphabetical_string("\tLast Name: ")
    return ln


# Error Handling - Numeric Values Only
def numeric(prompt):
    while True:
        t = input(prompt)
        t_with_no_spaces = t.replace(' ', '')
        if len(t_with_no_spaces) > 0 and t.isnumeric():
            break
        else:
            print("NUMERIC Values Only")
    return t


# User Input (Customer ID)
def read_id():
    id_no = numeric("\tCustomer Number: ")
    return id_no


# User Input (Tel Number)
def read_tel():
    tel = numeric("\tTelephone Number: ")
    return tel


# Updating the customer's number
def update_customers_c_no():
    try:
        update = "UPDATE customers SET c_no = ? WHERE c_no = ?"
        value = update_values()
        # Executing command and values
        cursor.execute(update, value)
        # Store values  in Database
        db.commit()
        print('Data updated successfully.')
        cursor.close()
    except (ValueError, pyodbc.ProgrammingError, pyodbc.IntegrityError, pyodbc.Error) as e:
        print(e)
        return None


# User Input
def update_values():
    print("\t\tUpdate\n")
    c_no = input("")
    return c_no


# Displaying the Menu
def main_menu():
    print("\t---Customer Record Database---")
    print("\t\tWelcome to the Main Menu")
    menu = "\n\t1: Select" \
           "\n\t2: Insert" \
           "\n\t3: Update" \
           "\n\t4: Quit" \
           "\nEnter a number: "
    # The menu loop and user input of option
    while True:
        try:
            number = int(input(menu))
            if number == 1:
                display()
            elif number == 2:
                insert_customer()
            elif number == 3:
                print("3")
            elif number == 4:
                print("\nThank for using the Customer Database")
                db.close()
                print("\nThe SQL connection is closed.")
                break
            else:
                print("Error. Please Try Again.")
        except ValueError:
            print("Invalid Choice. Enter 1-4")
    return number


main_menu()
