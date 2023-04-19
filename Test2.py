phoneDirectory = {}
#using while loop
while True:
    print("WELCOME TO THE GRANN'S PHONE DIRECTORY MENU")
    print("1. Add a record")
    print("2. Search a record")
    print("3. Change a record")
    print("4. Delete a record")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone_number = input("Enter your 10-digit phone number: ")
        phoneDirectory[name] = phone_number
        print("Record added")

    elif choice == '2':
        name = input("Enter name to search: ")
        if name in phoneDirectory:
            print(name + ": " + phoneDirectory[name] + "\n")
        else:
            print("Record deleted")

    elif choice == '3':
        name = input("Enter name: ")
        if name in phoneDirectory:
            phone_number = input("Enter new 10-digit phone number: ")
            phoneDirectory[name] = phone_number
            print("Record updated")
        else:
            print("Record not found")

    elif choice == '4':
        name = input("Enter name: ")
        if name in phoneDirectory:
            del phoneDirectory[name]
            print("Record deleted")
        else:
            print("Record not found")

    elif choice == '5':
        print("")
        break

    else:
        print("Invalid choice")
