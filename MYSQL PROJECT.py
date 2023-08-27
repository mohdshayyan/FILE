#                                                                                       ---| PYTHON CODING |---
#                                                                                 ---|School Management System|---
#                                                                             ---|  Designed and Maintained By  |---
#                                                                       ---| SHAYYAN - Class XII SCI {2023-2024}|---

import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
#from PIL import Image
from datetime import datetime


mydb = mysql.connector.connect(
host="localhost",
user='root',
password='root')
print(mydb, "connected to server")
print("\n")
print("-" * 165)
print(" " * 68 + "Welcome to School Management System by Shayyan")
print("-" * 165)



'''
# Load the background image
background_image = Image.open(r'C:\Users\hello\Desktop\asc.jpg')

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Set the background image as the plot's background
ax.imshow(background_image, aspect='auto', extent=(0, 10, 0, 6))
plt.title("--------- Welcome To All Saint's Church School ---------")
# Display the plot
plt.show()
'''

def create_database():
        cursor = mydb.cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS school')
        cursor.execute('USE school')

def create_students():
        cursor = mydb.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS students (Id VARCHAR(255),name VARCHAR(255), age VARCHAR(255), gender VARCHAR(255), Class VARCHAR(255),date_added VARCHAR(255))')

# Define the function to add a new student
def add_student():
    id = input("Enter ID of student: ")
    name = input("Enter student Name: ")
    age = input("Enter student's age: ")
    gender = input("Enter student gender: ")
    Class = input("Enter student Class: ")
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    cursor = mydb.cursor()
    # Inserting Values
    sql = "INSERT INTO students (id, name, age, gender, Class, date_added) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (id, name, age, gender, Class, date_time)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Define the function to view student details
def view_students():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall() 
    print("Press (f) to see in the form of DataFrame")
    print("Press (i) to see the Saprate Index values")
    print("Press (l) to see in the form of list")
    print("Press (g) to see in the form of Graph b/w Name & Ages ")    
    ch = input("Enter your choice: ")
    if ch=='i':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            print("Id is:", lst1)
            lst2 = [row[1] for row in result_list]
            print('Name is:', lst2)
            lst3 = [row[2] for row in result_list]
            print('Age is', lst3)
            lst4 = [row[3] for row in result_list]
            print('Gender is: ', lst4)
            lst5 = [row[4] for row in result_list]
            print('Class is', lst5)            
            lst6 = [row[5] for row in result_list]
            print('Date_&_Time', lst6)            
    elif ch=='l':
            result_list = [list(row) for row in result]
            print(result_list)           
    elif ch=='f':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            lst2 = [row[1] for row in result_list]
            lst3 = [row[2] for row in result_list]
            lst4 = [row[3] for row in result_list]
            lst5 = [row[4] for row in result_list]
            lst6 = [row[5] for row in result_list]            
            df = pd.DataFrame({'ID': lst1, 'Name': lst2, 'Age': lst3, 'Gender': lst4, 'Class': lst5,'Date_&_Time': lst6})
            print(df.to_markdown())

    elif ch == 'g':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            lst2 = [row[1] for row in result_list]
            lst3 = [row[2] for row in result_list]
            lst4 = [row[3] for row in result_list]
            lst5 = [row[4] for row in result_list]
            df = pd.DataFrame({'ID': lst1, 'Name': lst2, 'Age': lst3, 'Gender': lst4, 'Class': lst5})

    # Sort the dataframe by Age in ascending order
            df_sorted = df.sort_values(by='Age')

    # Get the sorted values for 'Name' and 'Age'
            Name = df_sorted['Name'].tolist()
            Age = df_sorted['Age'].tolist()

    # Create the bar chart
            plt.bar(Name, Age, color=['blue', 'green', 'red', 'orange', 'purple'])
            plt.xlabel('Name')
            plt.ylabel('Age')
            plt.title('Student Ages')
    
    # Set the y-axis limits and ticks
            plt.ylim(0, 18)  # Set the y-axis limits from 0 to 18
            plt.yticks(range(19))  # Set the y-axis ticks from 0 to 18    
            plt.show()



# Define the function to update student details
def update_student():
    id = input("Enter student's ID: ")
    name = input("Enter student's Name: ")
    age = input("Enter studenlt's age: ")
    gender = input("Enter student's gender: ")
    Class = input("Enter student's Class: ")
    cursor = mydb.cursor()
    sql_up = "update students set name = %s, age = %s, gender = %s, Class = %s where id = %s"
    val_up = (name, age, gender, Class,id)
    cursor.execute(sql_up, val_up)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")

# Define the function to delete student details
def delete_student():
    id = input("Enter student ID: ")
    cursor = mydb.cursor()
    sql = "delete from students where id = %s"
    val = (id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

    # CREATING A TABLE
def create_Staff():
        cursor = mydb.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Staff(Id varchar(50) primary key,post varchar(50),name varchar(50),salary varchar(50),phone varchar(50),date_added VARCHAR(255))')

# Define the function to add a new staff
def add_staff():
    Id = input("Enter staff ID: ")
    post = input("Enter staff Post: ")
    name = input("Enter staff Name: ")
    salary = input("Enter staff Salary: ")
    phone = input("Enter staff Phone no: ")
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")  
    cursor = mydb.cursor()
    # Inserting Values
    sql = "INSERT INTO staff (Id, post, name, salary, phone, date_added) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (Id, post, name, salary, phone, date_time)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Define the function to view student details
def view_staff():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM staff")
    result = cursor.fetchall()
    print("Press (f) to see in the form of DataFrame")
    print("Press (i) to see the Saprate Index values")
    print("Press (l) to see in the form of list")
    print("Press (g) to see in the form of Graph b/w Name & SALARY ")   
    ch = input("Enter your choice: ")
    if ch=='i':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            print("Id is:", lst1)
            lst2 = [row[1] for row in result_list]
            print('Post is:', lst2)
            lst3 = [row[2] for row in result_list]
            print('Name is:', lst3)
            lst4 = [row[3] for row in result_list]
            print('Salary is: ', lst4)
            lst5 = [row[4] for row in result_list]
            print('Phone_no is: ', lst5)
            lst6 = [row[5] for row in result_list]
            print('Date_&_Time is: ', lst6)                  
    elif ch=='l':
            result_list = [list(row) for row in result]
            print(result_list)            
    elif ch=='f':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            lst2 = [row[1] for row in result_list]
            lst3 = [row[2] for row in result_list]
            lst4 = [row[3] for row in result_list]
            lst5 = [row[4] for row in result_list]
            lst6 = [row[5] for row in result_list]                  
            df=pd.DataFrame({'ID':lst1,'POST':lst2,'NAME':lst3,'SALARY':lst4,'PHONE':lst5,'Date_&_Time': lst6})
            print(df.to_markdown())    

        # Plotting pie chart
    elif ch=='g':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            lst2 = [row[1] for row in result_list]
            lst3 = [row[2] for row in result_list]
            lst4 = [row[3] for row in result_list]
            lst5 = [row[4] for row in result_list]
            df=pd.DataFrame({'ID':lst1,'POST':lst2,'NAME':lst3,'SALARY':lst4,'PHONE':lst5})            
            plt.pie(df['SALARY'], labels=df['NAME'], autopct='%1.1f%%')
            plt.title('Staff Salary Distribution')
            plt.show()
            
# Define the function to update staff details
def update_staff():
    Id=input("Enter staff ID: ")
    post=input("Enter staff Post: ")
    name = input("Enter staff Name: ")
    salary = input("Enter staff Salary: ")
    phone = input("Enter staff Phone no: ")
    cursor = mydb.cursor()
    sql = "UPDATE staff set Id = %s , post= %s, name = %s, salary = %s, phone = %s WHERE Id = %s"
    val = (Id,post,name,salary, phone)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")

# Define the function to delete staff details
def delete_staff():
    Id = input("Enter staff ID: ")
    cursor = mydb.cursor()
    sql = "DELETE FROM staff WHERE Id = %s"
    val = (Id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

# CREATING A TABLE
def create_fee():
        cursor = mydb.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS fee(SrNo varchar(50) primary key,Name varchar(50),Class varchar(50),Status varchar(50),Quarter varchar(50),PaidAmt varchar(50),date_added VARCHAR(255))')

# Define the function to add Fee details
def fee():
    SrNo = input("Enter Payer's ID: ")
    Name = input("Enter Payer's Name: ")
    Class = input("Enter Payer's Class: ")
    Status = input("Enter Status (Paid/Due): ")
    Quarter = input("Enter Quarter: ")
    PaidAmt = input("Enter Paid Amount: ")
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    cursor = mydb.cursor()
    # Inserting Values
    sql = "INSERT INTO fee (SrNo, Name, Class, Status, Quarter, PaidAmt, date_added) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (SrNo, Name, Class, Status, Quarter, PaidAmt, date_time)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Define the function to view Fee details
def view_fee():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fee")
    result = cursor.fetchall()
    print("Press (f) to see in the form of DataFrame")
    print("Press (i) to see the Saprate Index values")
    print("Press (l) to see in the form of list")
    print("Press (g) to see in the form of Graph b/w Name & Paid Amount ")      
    ch = input("Enter your choice: ")
    if ch=='i':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            print("SrNo is:", lst1)
            lst2 = [row[1] for row in result_list]
            print('Name is:', lst2)
            lst3 = [row[2] for row in result_list]
            print('Class is:', lst3)
            lst4 = [row[3] for row in result_list]
            print('Status is: ', lst4)
            lst5 = [row[4] for row in result_list]
            print('Quarter is:', lst5)
            lst6 = [row[5] for row in result_list]
            print('PaidAmt is:', lst6)    
            lst7 = [row[6] for row in result_list]
            print('Date_&_Time is:', lst7)
            
    elif ch=='l':
            result_list = [list(row) for row in result]
            print(result_list)
            
    elif ch=='f':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            lst2 = [row[1] for row in result_list]
            lst3 = [row[2] for row in result_list]
            lst4 = [row[3] for row in result_list]
            lst5 = [row[4] for row in result_list]
            lst6 = [row[5] for row in result_list]
            lst7 = [row[6] for row in result_list]            
            df=pd.DataFrame({'SrNo':lst1,'Name':lst2,'Class':lst3,'Status':lst4,'Quarter':lst5,'PaidAmt':lst6,'Date_&_Time': lst7 })
            print(df.to_markdown())
 #################################################################           
        # Plotting line chart
# Plotting line chart
    elif ch == 'g':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            lst2 = [row[1] for row in result_list]
            lst3 = [row[2] for row in result_list]
            lst4 = [row[3] for row in result_list]
            lst5 = [row[4] for row in result_list]
            lst6 = [row[5] for row in result_list]
            df=pd.DataFrame({'SrNo':lst1,'Name':lst2,'Class':lst3,'Status':lst4,'Quarter':lst5,'PaidAmt':lst6 })
    
    # Sort the DataFrame by Quarter in ascending order
            df.sort_values(by='PaidAmt')    
            Name = df['Name']
            PaidAmt = df['PaidAmt']    
            plt.plot(Name, PaidAmt)
            plt.xlabel('Name')
            plt.ylabel('Paid Amount')
            plt.title('Fee Payment Over Quarters')
            plt.show()

# Define the function to update Fee details
def update_fee():
    SrNo = input("Enter student SrNo: ")
    Name = input("Enter student Name: ")
    Class = input("Enter student Class: ")
    Status = input("Enter student Status(Paid/Due): ")
    Quarter = input("Enter student Quarter: ")
    PaidAmt = input("Enter student PaidAmount: ")  
    cursor = mydb.cursor()
    sqlx = "UPDATE fee SET Name = %s, Class = %s, Status = %s, Quarter = %s,PaidAmt = %s WHERE SrNo = %s"
    valx = (Name,Class,Status,Quarter,PaidAmt,SrNo)
    cursor.execute(sqlx, valx)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")
    
# Define the function to delete Fee details
def delete_fee():
    SrNo = input("Enter student SrNo: ")
    cursor = mydb.cursor()
    sqle = "DELETE FROM fee WHERE SrNo = %s"
    vale = (SrNo,)
    cursor.execute(sqle, vale)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

    # Execute the selected option
    # Get the user's choice
def menu():
    print("_" * 100)
    print("----------------Modules in School Management System ---------")
    print("Module_1: Student record Module ")
    print("Module_2: Staff record Module")
    print("Module_3: Fee record Module")
    print("Module_4: Exit from the system")
    print("_" * 100)
    
# Get the user's choice:
# if option first:
def getchoice():
    while True:
        create_database()    
        menu()
        print("")
        ch = input("Enter your choice: ")
        if ch=='1':
            print("PRESS (a): To Add New Student record                                       PRESS (b): View Student details ")
            print("PRESS (c): To Update Student details                                           PRESS (d): Delete Student details")
            ch = input("Enter your choice: ")
            create_students()
            if ch=='a':
                add_student()
                input("Press ENTER KEY to continue.....")
                print()
            elif ch=='b':
                view_students()
                input("Press ENTER KEY to continue.....")
                print()
            elif ch=='c':
                update_student()
                input("Press ENTER KEY to continue.....")
                print()
            elif ch=='d':
                delete_student()
                input("Press ENTER KEY to continue.....")
                print()
## if option Second:
        elif ch=='2':
            print("PRESS (e) : Add New Staff record                                       PRESS (f) : View Staff details | ")
            print("PRESS (g) : UPDATE Staff details                                       PRESS (h) :Delete Staff details   ")
            opp =input("Enter your choice: ")
            create_Staff()
            if opp=='e':
                add_staff()
                input("Press ENTER KEY to continue.....")
                print()
            elif opp=='f':
                view_staff()
                input("Press ENTER KEY to continue.....")
                print()                
            elif opp=='g':
                update_staff()
                input("Press ENTER KEY to continue.....")
                print()                
            elif opp=='h':
                delete_staff()
                input("Press ENTER KEY to continue.....")
                print()                
### if option Third:
        elif ch=='3':
            print("PRESS (i): Add Fee deposit details                                        PRESS (j): View Fee details ")
            print("PRESS (k): Update Fee details                                                PRESS (l): Delete Fee details")
            opp = input("Enter your choice: ")
            create_fee()
            if opp=='i':
                fee()
                input("Press ENTER KEY to continue.....")
                print()                
            elif opp=='j':
                view_fee()
                input("Press ENTER KEY to continue.....")
                print()                
            elif opp=='k':
                update_fee()
                input("Press ENTER KEY to continue.....")
                print()                
            elif opp=='l':
                delete_fee()
                input("Press ENTER KEY to continue.....")
                print()                
        
#### if option Fourth:
        elif ch=='4':
                print()
                print("Exited !")
                print("Succesfully,")
                print("Thanks")
                print("For")
                print("Coming :-)")
                print()
                print()
                print()
                print()
                break
        
# Recall Choice function =>
getchoice()
# Disconnecting from the server =>
mydb.close()





'''
#                                                                                       ---| PYTHON CODING |---
#                                                                                 ---|School Management System|---
#                                                                             ---|  Designed and Maintained By  |---
#                                                                       ---| SHAYYAN - Class XII SCI {2023-2024}|---

import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
from datetime import datetime
# Define the function to add a new student

mydb = mysql.connector.connect(
host="localhost",
user='root',
password='root')
print(mydb, "connected to server")
print("\n")
print("-" * 165)
print(" " * 68 + "Welcome to School Management System")
print("-" * 165)

def create_database():
        cursor = mydb.cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS school')
        cursor.execute('USE school')

def create_students():
        cursor = mydb.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS students (Id VARCHAR(255),name VARCHAR(255), age VARCHAR(255), gender VARCHAR(255), Class VARCHAR(255),date_added VARCHAR(255))')

# Define the function to add a new student
def add_student():
    id = input("Enter ID of student: ")
    name = input("Enter student Name: ")
    age = input("Enter student's age: ")
    gender = input("Enter student gender: ")
    Class = input("Enter student Class: ")
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    cursor = mydb.cursor()
    # Inserting Values
    sql = "INSERT INTO students (id, name, age, gender, Class, date_added) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (id, name, age, gender, Class, date_time)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Define the function to view student details
def view_students():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall() 
    print("Press (f) to see in the form of DataFrame")
    print("Press (i) to see the Saprate Index values")
    print("Press (l) to see in the form of list")
    print("Press (g) to see in the form of Graph b/w Name & Ages ")    
    ch = input("Enter your choice: ")
    if ch=='i':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            print("Id is:", lst1)
            lst2 = [row[1] for row in result_list]
            print('Name is:', lst2)
            lst3 = [row[2] for row in result_list]
            print('Age is', lst3)
            lst4 = [row[3] for row in result_list]
            print('Gender is: ', lst4)
            lst5 = [row[4] for row in result_list]
            print('Class is', lst5)            
            lst6 = [row[5] for row in result_list]
            print('Date_&_Time', lst6)            
    elif ch=='l':
            result_list = [list(row) for row in result]
            print(result_list)           
    elif ch=='f':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            lst2 = [row[1] for row in result_list]
            lst3 = [row[2] for row in result_list]
            lst4 = [row[3] for row in result_list]
            lst5 = [row[4] for row in result_list]
            lst6 = [row[5] for row in result_list]            
            df = pd.DataFrame({'ID': lst1, 'Name': lst2, 'Age': lst3, 'Gender': lst4, 'Class': lst5,'Date_&_Time': lst6})
            print(df.to_markdown())

    elif ch == 'g':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            lst2 = [row[1] for row in result_list]
            lst3 = [row[2] for row in result_list]
            lst4 = [row[3] for row in result_list]
            lst5 = [row[4] for row in result_list]
            df = pd.DataFrame({'ID': lst1, 'Name': lst2, 'Age': lst3, 'Gender': lst4, 'Class': lst5})

    # Sort the dataframe by Age in ascending order
            df_sorted = df.sort_values(by='Age')

    # Get the sorted values for 'Name' and 'Age'
            Name = df_sorted['Name'].tolist()
            Age = df_sorted['Age'].tolist()

    # Create the bar chart
            plt.bar(Name, Age, color=['blue', 'green', 'red', 'orange', 'purple'])
            plt.xlabel('Name')
            plt.ylabel('Age')
            plt.title('Student Ages')
    
    # Set the y-axis limits and ticks
            plt.ylim(0, 18)  # Set the y-axis limits from 0 to 18
            plt.yticks(range(19))  # Set the y-axis ticks from 0 to 18    
            plt.show()



# Define the function to update student details
def update_student():
    id = input("Enter student's ID: ")
    name = input("Enter student's Name: ")
    age = input("Enter studenlt's age: ")
    gender = input("Enter student's gender: ")
    Class = input("Enter student's Class: ")
    cursor = mydb.cursor()
    sql_up = "update students set name = %s, age = %s, gender = %s, Class = %s where id = %s"
    val_up = (name, age, gender, Class,id)
    cursor.execute(sql_up, val_up)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")

# Define the function to delete student details
def delete_student():
    id = input("Enter student ID: ")
    cursor = mydb.cursor()
    sql = "delete from students where id = %s"
    val = (id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

    # CREATING A TABLE
def create_Staff():
        cursor = mydb.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Staff(Id varchar(50) primary key,post varchar(50),name varchar(50),salary varchar(50),phone varchar(50),date_added VARCHAR(255))')

# Define the function to add a new staff
def add_staff():
    Id = input("Enter staff ID: ")
    post = input("Enter staff Post: ")
    name = input("Enter staff Name: ")
    salary = input("Enter staff Salary: ")
    phone = input("Enter staff Phone no: ")
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")  
    cursor = mydb.cursor()
    # Inserting Values
    sql = "INSERT INTO staff (Id, post, name, salary, phone, date_added) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (Id, post, name, salary, phone, date_time)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Define the function to view student details
def view_staff():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM staff")
    result = cursor.fetchall()
    print("Press (f) to see in the form of DataFrame")
    print("Press (i) to see the Saprate Index values")
    print("Press (l) to see in the form of list")
    print("Press (g) to see in the form of Graph b/w Name & SALARY ")   
    ch = input("Enter your choice: ")
    if ch=='i':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            print("Id is:", lst1)
            lst2 = [row[1] for row in result_list]
            print('Post is:', lst2)
            lst3 = [row[2] for row in result_list]
            print('Name is:', lst3)
            lst4 = [row[3] for row in result_list]
            print('Salary is: ', lst4)
            lst5 = [row[4] for row in result_list]
            print('Phone_no is: ', lst5)
            lst6 = [row[5] for row in result_list]
            print('Date_&_Time is: ', lst6)                  
    elif ch=='l':
            result_list = [list(row) for row in result]
            print(result_list)            
    elif ch=='f':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            lst2 = [row[1] for row in result_list]
            lst3 = [row[2] for row in result_list]
            lst4 = [row[3] for row in result_list]
            lst5 = [row[4] for row in result_list]
            lst6 = [row[5] for row in result_list]                  
            df=pd.DataFrame({'ID':lst1,'POST':lst2,'NAME':lst3,'SALARY':lst4,'PHONE':lst5,'Date_&_Time': lst6})
            print(df.to_markdown())    

        # Plotting pie chart
    elif ch=='g':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            lst2 = [row[1] for row in result_list]
            lst3 = [row[2] for row in result_list]
            lst4 = [row[3] for row in result_list]
            lst5 = [row[4] for row in result_list]
            df=pd.DataFrame({'ID':lst1,'POST':lst2,'NAME':lst3,'SALARY':lst4,'PHONE':lst5})            
            plt.pie(df['SALARY'], labels=df['NAME'], autopct='%1.1f%%')
            plt.title('Staff Salary Distribution')
            plt.show()
            
# Define the function to update staff details
def update_staff():
    Id=input("Enter staff ID: ")
    post=input("Enter staff Post: ")
    name = input("Enter staff Name: ")
    salary = input("Enter staff Salary: ")
    phone = input("Enter staff Phone no: ")
    cursor = mydb.cursor()
    sql = "UPDATE staff set Id = %s , post= %s, name = %s, salary = %s, phone = %s WHERE Id = %s"
    val = (Id,post,name,salary, phone)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")

# Define the function to delete staff details
def delete_staff():
    Id = input("Enter staff ID: ")
    cursor = mydb.cursor()
    sql = "DELETE FROM staff WHERE Id = %s"
    val = (Id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

# CREATING A TABLE
def create_fee():
        cursor = mydb.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS fee(SrNo varchar(50) primary key,Name varchar(50),Class varchar(50),Status varchar(50),Quarter varchar(50),PaidAmt varchar(50),date_added VARCHAR(255))')

# Define the function to add Fee details
def fee():
    SrNo = input("Enter Payer's ID: ")
    Name = input("Enter Payer's Name: ")
    Class = input("Enter Payer's Class: ")
    Status = input("Enter Status (Paid/Due): ")
    Quarter = input("Enter Quarter: ")
    PaidAmt = input("Enter Paid Amount: ")
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    cursor = mydb.cursor()
    # Inserting Values
    sql = "INSERT INTO fee (SrNo, Name, Class, Status, Quarter, PaidAmt, date_added) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (SrNo, Name, Class, Status, Quarter, PaidAmt, date_time)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Define the function to view Fee details
def view_fee():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fee")
    result = cursor.fetchall()
    print("Press (f) to see in the form of DataFrame")
    print("Press (i) to see the Saprate Index values")
    print("Press (l) to see in the form of list")
    print("Press (g) to see in the form of Graph b/w Name & Paid Amount ")      
    ch = input("Enter your choice: ")
    if ch=='i':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            print("SrNo is:", lst1)
            lst2 = [row[1] for row in result_list]
            print('Name is:', lst2)
            lst3 = [row[2] for row in result_list]
            print('Class is:', lst3)
            lst4 = [row[3] for row in result_list]
            print('Status is: ', lst4)
            lst5 = [row[4] for row in result_list]
            print('Quarter is:', lst5)
            lst6 = [row[5] for row in result_list]
            print('PaidAmt is:', lst6)    
            lst7 = [row[6] for row in result_list]
            print('Date_&_Time is:', lst7)
            
    elif ch=='l':
            result_list = [list(row) for row in result]
            print(result_list)
            
    elif ch=='f':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            lst2 = [row[1] for row in result_list]
            lst3 = [row[2] for row in result_list]
            lst4 = [row[3] for row in result_list]
            lst5 = [row[4] for row in result_list]
            lst6 = [row[5] for row in result_list]
            lst7 = [row[6] for row in result_list]            
            df=pd.DataFrame({'SrNo':lst1,'Name':lst2,'Class':lst3,'Status':lst4,'Quarter':lst5,'PaidAmt':lst6,'Date_&_Time': lst7 })
            print(df.to_markdown())
 #################################################################           
        # Plotting line chart
# Plotting line chart
    elif ch == 'g':
            result_list = [list(row) for row in result]
            lst1 = [row[0] for row in result_list]
            lst2 = [row[1] for row in result_list]
            lst3 = [row[2] for row in result_list]
            lst4 = [row[3] for row in result_list]
            lst5 = [row[4] for row in result_list]
            lst6 = [row[5] for row in result_list]
            df=pd.DataFrame({'SrNo':lst1,'Name':lst2,'Class':lst3,'Status':lst4,'Quarter':lst5,'PaidAmt':lst6 })
    
    # Sort the DataFrame by Quarter in ascending order
            df.sort_values(by='PaidAmt')    
            Name = df['Name']
            PaidAmt = df['PaidAmt']    
            plt.plot(Name, PaidAmt)
            plt.xlabel('Name')
            plt.ylabel('Paid Amount')
            plt.title('Fee Payment Over Quarters')
            plt.show()

# Define the function to update Fee details
def update_fee():
    SrNo = input("Enter student SrNo: ")
    Name = input("Enter student Name: ")
    Class = input("Enter student Class: ")
    Status = input("Enter student Status(Paid/Due): ")
    Quarter = input("Enter student Quarter: ")
    PaidAmt = input("Enter student PaidAmount: ")  
    cursor = mydb.cursor()
    sqlx = "UPDATE fee SET Name = %s, Class = %s, Status = %s, Quarter = %s,PaidAmt = %s WHERE SrNo = %s"
    valx = (Name,Class,Status,Quarter,PaidAmt,SrNo)
    cursor.execute(sqlx, valx)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")
    
# Define the function to delete Fee details
def delete_fee():
    SrNo = input("Enter student SrNo: ")
    cursor = mydb.cursor()
    sqle = "DELETE FROM fee WHERE SrNo = %s"
    vale = (SrNo,)
    cursor.execute(sqle, vale)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

    # Execute the selected option
    # Get the user's choice
def menu():
    print("_" * 100)
    print("----------------Modules in School Management System ---------")
    print("Module_1: Student record Module ")
    print("Module_2: Staff record Module")
    print("Module_3: Fee record Module")
    print("Module_4: Exit from the system")
    print("_" * 100)
    
# Get the user's choice:
# if option first:
def getchoice():
    while True:
        create_database()    
        menu()
        print("")
        ch = input("Enter your choice: ")
        if ch=='1':
            print("PRESS (a): To Add New Student record                                       PRESS (b): View Student details ")
            print("PRESS (c): To Update Student details                                           PRESS (d): Delete Student details")
            ch = input("Enter your choice: ")
            create_students()
            if ch=='a':
                add_student()
                input("Press ENTER KEY to continue.....")
                print()
            elif ch=='b':
                view_students()
                input("Press ENTER KEY to continue.....")
                print()
            elif ch=='c':
                update_student()
                input("Press ENTER KEY to continue.....")
                print()
            elif ch=='d':
                delete_student()
                input("Press ENTER KEY to continue.....")
                print()
## if option Second:
        elif ch=='2':
            print("PRESS (e) : Add New Staff record                                       PRESS (f) : View Staff details | ")
            print("PRESS (g) : UPDATE Staff details                                       PRESS (h) :Delete Staff details   ")
            opp =input("Enter your choice: ")
            create_Staff()
            if opp=='e':
                add_staff()
                input("Press ENTER KEY to continue.....")
                print()
            elif opp=='f':
                view_staff()
                input("Press ENTER KEY to continue.....")
                print()                
            elif opp=='g':
                update_staff()
                input("Press ENTER KEY to continue.....")
                print()                
            elif opp=='h':
                delete_staff()
                input("Press ENTER KEY to continue.....")
                print()                
### if option Third:
        elif ch=='3':
            print("PRESS (i): Add Fee deposit details                                        PRESS (j): View Fee details ")
            print("PRESS (k): Update Fee details                                                PRESS (l): Delete Fee details")
            opp = input("Enter your choice: ")
            create_fee()
            if opp=='i':
                fee()
                input("Press ENTER KEY to continue.....")
                print()                
            elif opp=='j':
                view_fee()
                input("Press ENTER KEY to continue.....")
                print()                
            elif opp=='k':
                update_fee()
                input("Press ENTER KEY to continue.....")
                print()                
            elif opp=='l':
                delete_fee()
                input("Press ENTER KEY to continue.....")
                print()                
        
#### if option Fourth:
        elif ch=='4':
                print()
                print("Exited !")
                print("Succesfully,")
                print("Thanks")
                print("For")
                print("Coming :-)")
                print()
                print()
                print()
                print()
                break
        
# Recall Choice function =>
getchoice()
# Disconnecting from the server =>
mydb.close()
'''
