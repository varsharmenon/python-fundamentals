lst = []
ch = str(input("are you entering numericals or strings? (type 1 for numericals, and 2 for strings.)"))
n = int(input("How many elements do you want in the list? "))
if ch=='1':

    for i in range(n):
        element = float(input(f"Enter element {i+1}: "))
        if element == 0:
             element == 0.0
        lst.append(element)


    while True:
        print("\n--- LIST OPERATIONS MENU ---")
        print("1. Display list")
        print("2. Add element")
        print("3. Remove element")
        print("4. Sort list")
        print("5. Reverse list")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            if n=='0':
                print("The list is empty.")
            else:
                print("Current list:", lst)

        elif choice == 2:
            element = input("Enter element to add: ")
            lst.append(element)
            print("Element added.")

        elif choice == 3:
                element = input("Enter element to remove: ")
                if element in lst:
                    lst.remove(element)
                    print("Element removed.")
                else:
                    print("Element not found in list.")

        elif choice == 4:
                lst.sort()
                print("List sorted.")

        elif choice == 5:
            lst.reverse()
            print("List reversed.")

        elif choice == 6:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")
elif ch=='2':

    for i in range(n):
        element = str(input(f"Enter element {i+1}: "))
        lst.append(element)


    while True:
        print("\n--- LIST OPERATIONS MENU ---")
        print("1. Display list")
        print("2. Add element")
        print("3. Remove element")
        print("4. Sort list")
        print("5. Reverse list")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            if n=='0':
                print("The list is empty.")
            else:
                print("Current list:", lst)

        elif choice == 2:
            element = input("Enter element to add: ")
            lst.append(element)
            print("Element added.")

        elif choice == 3:
                element = input("Enter element to remove: ")
                if element in lst:
                    lst.remove(element)
                    print("Element removed.")
                else:
                    print("Element not found in list.")

        elif choice == 4:
                lst.sort()
                print("List sorted.")

        elif choice == 5:
            lst.reverse()
            print("List reversed.")

        elif choice == 6:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")
else:
    print("invalid character")

