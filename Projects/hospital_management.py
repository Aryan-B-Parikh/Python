import mysql.connector as sql
conn = sql.connect(host='localhost', user='root', passwd='', database='project')
if conn.is_connected():
    print('Successfully connected to database!')
c1 = conn.cursor()
print('---------------------------------------------')
print("HOSPITAL MANAGEMENT SYSTEM")
print('---------------------------------------------')
print('"GOD WISHES YOU"')
print("1. LOGIN")
print("2. EXIT")
choice = int(input("ENTER YOUR CHOICE: "))
if choice == 1:
    u1 = input("Enter username: ")
    pwd1 = input("Enter password: ")
    if u1 == 'AryanParikh' and pwd1 == '08Aryan@06Parikh':
        print("WELCOME TO HOSPITAL")
        while True:
            print("\nMENU:")
            print("1. Register Patient details")
            print("2. Register Doctor details")
            print("3. Register Worker details")
            print("4. Show all Patients")
            print("5. Show all Doctors")
            print("6. Show all Workers")
            print("7. Search Patient by name")
            print("8. Search Doctor by name")
            print("9. Search Worker by name")
            print("10. Exit")
            choice = int(input("ENTER YOUR CHOICE: "))
            if choice == 1:
                p_name = input('Enter Patient Name: ')
                p_age = int(input('Enter Age: '))
                p_problem = input('Enter the Problem/Disease: ')
                p_phone = input('Enter Phone number: ')
                sql_insert = "INSERT INTO patient_details VALUES (%s, %s, %s, %s)"
                c1.execute(sql_insert, (p_name, p_age, p_problem, p_phone))
                conn.commit()
                print("Patient successfully registered.")
            elif choice == 2:
                d_name = input('Enter Doctor Name: ')
                d_age = int(input('Enter Age: '))
                d_department = input('Enter the Department: ')
                d_phone = input('Enter Phone number: ')
                sql_insert = "INSERT INTO doctor_details VALUES (%s, %s, %s, %s)"
                c1.execute(sql_insert, (d_name, d_age, d_department, d_phone))
                conn.commit()
                print("Doctor successfully registered.")
            elif choice == 3:
                w_name = input('Enter Worker Name: ')
                w_age = int(input('Enter Age: '))
                w_work = input('Enter type of work: ')
                w_phone = input('Enter Phone number: ')
                sql_insert = "INSERT INTO worker_details VALUES (%s, %s, %s, %s)"
                c1.execute(sql_insert, (w_name, w_age, w_work, w_phone))
                conn.commit()
                print("Worker successfully registered.")
            elif choice == 4:
                c1.execute("SELECT * FROM patient_details")
                for row in c1.fetchall():
                    print(row)
            elif choice == 5:
                c1.execute("SELECT * FROM doctor_details")
                for row in c1.fetchall():
                    print(row)
            elif choice == 6:
                c1.execute("SELECT * FROM worker_details")
                for row in c1.fetchall():
                    print(row)
            elif choice == 7:
                h = input("Enter patient name: ")
                c1.execute("SELECT * FROM patient_details WHERE p_name = %s", (h,))
                for row in c1.fetchall():
                    print(row)
            elif choice == 8:
                d = input("Enter doctor name: ")
                c1.execute("SELECT * FROM doctor_details WHERE d_name = %s", (d,))
                for row in c1.fetchall():
                    print(row)
            elif choice == 9:
                f = input("Enter worker name: ")
                c1.execute("SELECT * FROM worker_details WHERE w_name = %s", (f,))
                for row in c1.fetchall():
                    print(row)
            elif choice == 10:
                print("Exiting. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Wrong username or password.")
elif choice == 2:
    print("Exiting program.")
    exit()