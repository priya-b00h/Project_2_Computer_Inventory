"""
Names: Ian Gui and Priya Prabhu
Assignment: Project 2 - Computer Inventory
Due Date: 03/05/2026
Description: This file contains the implementation of the ComputerSystem and its subclasses Windows and Linux.
It uses the LinkComputer class to create an inventory of ComputerSystem objects. This inventory has a menu and 
responds to user input to list, add and remove computers in the inventory using the print(), addComputer() and 
removeComputer() functions.
"""



from linked import LinkedComputer
from computer import ComputerSystem, Windows, Linux


def mainMenu():
    """
    Prints the main menu and manages user input.
    """

    # Create a LinkedComputer instance to store the inventory
    computers = LinkedComputer()

    def addComputer():
            """Adds computer with user inputted info to linked structure"""
            
            # Get and validate IP address input
            ip = input("Enter the computer's IP address: ").strip()  # Remove leading/trailing whitespace
            ip_parts = ip.split(".")
            while len(ip_parts) != 4 or not all(part.isdigit() and 0 <= int(part) <= 255 for part in ip_parts):
                print("Invalid IP address. Please enter in format x.x.x.x (0-255).")
                ip = input("Enter the computer's IP address: ").strip()
                ip_parts = ip.split(".")

            while True:
                try:
                    year = int(input("Enter the year of purchase: "))
                    break
                except ValueError:
                    print("Please enter a valid year.")

            # Loop until valid OS is entered
            while True:
                os = input("Enter the operating system: ")

                # Check if the OS is Windows or Linux (case-insensitive)
                if "linux" in os.lower():
                    fs = input("Enter the file system capacity: ")
                    computer = Linux(ip, year, os, fs)
                    break
                elif "windows" in os.lower():
                    drive_capacity = input("Enter the C drive capacity: ")
                    computer = Windows(ip, year, os, drive_capacity)
                    break
                else:
                    print("*Invalid operating system. Please pick Windows or Linux.*")




            computers.add(computer)

    def removeComputers():
            """Removes oldest computers from the linked structure based on user input amount"""
            if(computers.size == 0):
                print("You have no computers in your inventory.")
                return

            amount = int(input("How many computers do you want to remove: "))

            # Check if the amount to remove is less than or equal to the number of computers in the inventory
            if amount <= computers.size and amount > 0:
                print("Year purchased  IP address      Storage Space             Operating System\n")
                print("------------------------------------------------------------------------------")
                
                # Remove the specified number of computers and print their details
                for _ in range(amount):
                    removed_computer = computers.head 
                    computers.remove()
                    print(removed_computer)
            else:
                print(f"You only have {computers.size} computers in your inventory.")

    # Add some initial computers to the inventory for testing
    c1 = Windows("192.168.1.1", 2016, "Windows 10", "500 GB")
    c2 = Linux("192.168.1.2", 2018, "Linux Ubuntu", "ext4")
    computers.add(c1)
    computers.add(c2)

    # Main menu loop
    while True:
        #main menu formatting
        """prints main menu"""
        print("")
        print("------------------------------------")
        print("               MENU")
        print("L. List all computers in your inventory")
        print("")
        print("A. Add a computer")
        print("R. Remove some computers")
        print("")
        print("Q. Quit")
        print("------------------------------------")
        print("")

        #case-insensitive user input
        choice = input("Enter your choice: ").lower()
        print("")

        #checks user input to call the correct function
        if choice == "l":
            print(computers)
        elif choice == "a":
            addComputer()
        elif choice == "r":
            removeComputers()
        elif choice == "q":
            break
        else:
            print("Invalid choice.")
#call main menu to start the program
mainMenu()
