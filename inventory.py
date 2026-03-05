from linked import LinkedComputer

def mainMenu():
    """
    Prints the main menu and manages user input.
    """

    computers = LinkedComputer()

    def addComputer():
        """Adds computer with user inputted info to linked structure"""
        ip = input("Enter the computer's IP address: ")
        year = input("Enter the year of purchase: ")
        os = input("Enter the operating system: ")
        drive_capacity = input("Enter the C drive capacity: ")

    def removeComputers():
        amount = input("How many computers do you want to remove: ")

        if amount <= computers.size:
            if amount > 0:
                print("Year purchased  IP address   Storage Space   Operating System")
                print("-------------------------------------------------------------")

            for _ in range(amount):
                """removes """
                removed_object = computers.remove()
                print("2016".ljust(15), "1.1.1.1".ljust(15), "Filesystem, 999 GB".ljust(21), "Windows 11")

    while True:
        """prints main menu"""
        print("")
        print("------------------------------------")
        print("Menu")
        print("L. List all computers in your inventory")
        print("")
        print("A. Add a computer")
        print("R. Remove some computers")
        print("")
        print("Q. Quit")
        print("------------------------------------")
        print("")

        choice = input("Enter your choice: ").lower()
        print("")

        """checks user input"""
        if choice == "l":
            print(computers)
        elif choice == "a":
            addComputer()
        elif choice == "r":
            removeComputers
        elif choice == "q":
            break
        else:
            print("Invalid choice.")