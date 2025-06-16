import csv

def save_password(website, username, password):
    with open('passwords.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([website, username, password])
    print("Password saved successfully!")

def view_passwords():
    try:
        with open('passwords.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Website: {row[0]}, Username: {row[1]}, Password: {row[2]}")
    except FileNotFoundError:
        print("No passwords stored yet.")

def main():
    while True:
        print("\n--- Password Manager ---")
        print("1. Add new password")
        print("2. View saved passwords")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            save_password(website, username, password)
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
