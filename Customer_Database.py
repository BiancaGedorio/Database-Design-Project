# Database Design Project 2020
# Author: Bianca Gedorio
# Student No: R00164040
# ITM2-A
# 12/11/2020

import pyodbc

# Connecting client and database server using ODBC
db = pyodbc.connect('DRIVER={MySQL ODBC 8.0 Unicode Driver};'
                    'User=root;'
                    'Password=Bi@nc@joie123..;'
                    'Server=localhost;'
                    'Database=project_database;'
                    )
cursor = db.cursor()


# Shows each row in the customer table
def display():
    try:
        # Execute Select MySQL Command
        cursor.execute("select * from customers;")
        print('\n\t\tCustomer Records\n')
        # Table Names
        print('Column: C_no, Fname, Lname, Tel_No')
        for x in cursor:
            print(x)
    except (ValueError, pyodbc.ProgrammingError, NameError) as e:
        print(e)
        return None


# Values are saved in the database
def insert_customer():
    try:
        # Insert MySQL Command
        insert = "INSERT INTO customers (fname, lname, tel_no) VALUES (?, ?, ?)"
        # Inserted value and Customer Number row are executed
        values = insert_values()
        cursor.execute(insert, values)
        # Store values in Database
        db.commit()
        print(cursor.rowcount, " customer record is stored successfully.")
    except (ValueError, pyodbc.ProgrammingError, pyodbc.IntegrityError, pyodbc.Error) as e:
        print(e)
        return None


# Input values in INSERT
def insert_values():
    print("\t\tFill in the Details\n")
    f_name = read_firstname()
    l_name = read_lastname()
    tel_no = read_tel()
    return f_name, l_name, tel_no


# User Input (First Name)
def read_firstname():
    f = read_nonempty_alphabetical_string("\tFirst Name: ")
    return f


# User Input (Last Name)
def read_lastname():
    ln = read_nonempty_alphabetical_string("\tLast Name: ")
    return ln


# User Input (Tel Number)
def read_tel():
    tel = numeric("\tTelephone Number: ")
    return tel


# User Input for updating the first name by specifying the customer number
def update_fname():
    try:
        print("\t\t\tUpdate Customer Details\n")
        num_row = numeric("\tChoose Row Number: ")
        change_fname = read_nonempty_alphabetical_string("\tUpdate First Name: ")
        # Update MySQL Command
        update = "UPDATE customers SET fname = ? WHERE c_no = ?"
        # Updated value and Customer Number row are executed
        val = (change_fname, num_row)
        cursor.execute(update, val)
        # Store values in Database
        db.commit()
        print(cursor.rowcount, "record(s) affected")
    except (ValueError, pyodbc.ProgrammingError, pyodbc.IntegrityError, pyodbc.Error) as e:
        print(e)
        return None


# User Input for updating the last name by specifying the customer number
def update_lname():
    try:
        print("\t\t\tUpdate Customer Details\n")
        num_row1 = numeric("\tChoose Row Number: ")
        change_lname = read_nonempty_alphabetical_string("\tUpdate Last Name: ")
        # Update MySQL Command
        update = "UPDATE customers SET lname = ? WHERE c_no = ?"
        # Updated value and Customer Number row are executed
        val = (change_lname, num_row1)
        cursor.execute(update, val)
        # Store values in Database
        db.commit()
        print(cursor.rowcount, "record(s) affected")
    except (ValueError, pyodbc.ProgrammingError, pyodbc.IntegrityError, pyodbc.Error) as e:
        print(e)
        return None


# User Input for updating the telephone number by specifying the customer number
def update_tel_no():
    try:
        print("\t\t\tUpdate Customer Details\n")
        num_row2 = numeric("\tChoose Row Number: ")
        change_tel_no = numeric("\tUpdate Telephone Number: ")
        # Update MySQL Command
        update = "UPDATE customers SET tel_no = ? WHERE c_no = ?"
        # Updated value and Customer Number row are executed
        val = (change_tel_no, num_row2)
        cursor.execute(update, val)
        # Store values in Database
        db.commit()
        print(cursor.rowcount, "record(s) affected")
    except (ValueError, pyodbc.ProgrammingError, pyodbc.IntegrityError, pyodbc.Error) as e:
        print(e)
        return None


# Update menu for selecting which column to append
def update_menu():
    print("\n\t ____Update SubMenu____")
    m_update = "\n\tWhich column do you want to update?" \
               "\n\t1: First name " \
               "\n\t2: Last Name " \
               "\n\t3: Telephone Number " \
               "\n\t4: Back to Main Menu" \
               "\n--> "
    # The menu loop and user input of option
    while True:
        try:
            u_number = int(input(m_update))
            if u_number == 1:
                update_fname()
                break
            elif u_number == 2:
                update_lname()
                break
            elif u_number == 3:
                update_tel_no()
                break
            elif u_number == 4:
                break
            else:
                print("Invalid. Enter 1-4. Try Again.")
        except ValueError:
            print("Error")
    return u_number


# Displaying the Menu
def main_menu():
    print("\n\n\t----Customer Record Database----\n\n")
    print("\n\t  Welcome to the Main Menu")
    menu = "\n**************************************************\n"\
           "\n\t1: Select" \
           "\n\t2: Insert" \
           "\n\t3: Update" \
           "\n\t4: Quit" \
           "\n--> "
    # The menu loop and user input of option
    while True:
        try:
            number = int(input(menu))
            if number == 1:
                display()
            elif number == 2:
                insert_customer()
            elif number == 3:
                update_menu()
            elif number == 4:
                print("\nThank you for using the Customer Database!")
                db.close()
                print("\nThe SQL connection is closed.")
                break
            else:
                print("Invalid. Enter 1-4 only. Try Again.")
        except ValueError:
            print("Error")
    return number


# Error Handling - Letters Only
def read_nonempty_alphabetical_string(prompt):
    while True:
        s = input(prompt)
        s_with_no_spaces = s.replace(' ', '')
        if len(s_with_no_spaces) > 0 and s_with_no_spaces.isalpha():
            break
        else:
            print("\t\t\t\tLETTER Values Only")
    return s


# Error Handling - Numeric Values Only
def numeric(prompt):
    while True:
        t = input(prompt)
        t_with_no_spaces = t.replace(' ', '')
        if len(t_with_no_spaces) > 0 and t.isnumeric():
            break
        else:
            print("\t\t\t\tNUMERIC Values Only")
    return t


main_menu()
