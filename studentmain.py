
import student_detailspyxl
import getpass
admin_username = "admin"
admin_password = "1234"

# Admin Login
def admin_login():
    print(" -----ADMIN LOGIN----- ")
    adminuser = input("Enter admin username: ")
    adminpasswd = getpass.getpass("Enter admin password: ")
    if adminuser == admin_username and adminpasswd == admin_password:
        print("SUCCESSFULLY LOGGED IN")
        disp_menu()
          
    else:
        print("Invalid credentials.")
        return False    

username ="user"
password ="1111" 
# User Login
def user_login():
    print(" -----STUDENT LOGIN-----")
    stduser = input("Enter  username: ")
    stdpasswd = getpass.getpass("Enter  password: ")
    if stduser == username and stdpasswd == password:
        print("SUCCESSFULLY LOGGED IN")
        print("\n")
        disp_students()
    else:
        print("Invalid credentials.")
        return False
    
    # ...

def create_student():
    usn = input("Enter USN: ")
    name = (input("Enter name: "))
    branch = input("Enter branch: ")
    year = input("Enter year: ")
    mobile_no=int(input("Enter mobile number:"))

    student_detailspyxl.add_student(usn, name, branch, year,mobile_no)
    print("Student added successfully.")
    disp_menu()

def disp_students():
    student_detailspyxl.display_students()

def update_student():
    usn = input("Enter USN of student to update: ")
    updated_name = input("Enter updated name: ")
    updated_branch = input("Enter updated branch: ")
    updated_year = input("Enter updated year: ")
    updated_mobile_no=input("Enter updated mobile number")
    student_detailspyxl.update_student(usn, updated_name, updated_branch, updated_year,updated_mobile_no)

def delete_student():
    usn = input("Enter USN of student to delete: ")
    student_detailspyxl.delete_student(usn)

def disp_menu():
    print("\nMenu:")
    print("1. view Student Information")
    print("2. Enroll Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        disp_students()
    elif choice == "2":
        create_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        exit(0)
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


while True:
    ch = input("\nPLEASE SELECT WHO ARE ACCESSING THE STUDENT DATABASE\n(1) Admin\n(2) Student\n(3) Exit\n")
    if ch == "1":
        admin_login()
    elif ch == "2":
        user_login()
    else:
        exit()
        
