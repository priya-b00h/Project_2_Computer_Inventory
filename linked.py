"""
Names: Ian Gui and Priya Prabhu
Assignment: Project 2 - Computer Inventory
Due Date: 03/05/2026
Description: This file contains the LinkedComputer class that initializes a linked list of
ComputerSystem objects. It has the add(), remove() and string formatting methods. 
"""

class LinkedComputer:
    """Represents a linked structure that stores ComputerSystems."""
    def __init__(self):
        """Initiates head to none, as there are no items yet"""
        self.head = None
        self.size = 0

    def add(self, computerObject):
        """This function adds a computerObject into the correct position"""

        self.size += 1

       # If the linked structure is empty, add the computerObject as the head 
        if self.head == None:
            self.head = computerObject
            computerObject.next = None
        # If the new computerObject's purchase year is less than the head's purchase year, add it in front
        elif computerObject.purchase_year < self.head.purchase_year:
            computerObject.next = self.head
            self.head = computerObject
        # find the correct spot to add if not the head
        else:
            current = self.head
            #Moves through the linked structure until the new object is in the correct spot
            while current.next and computerObject.purchase_year >= current.next.purchase_year:
                current = current.next
            computerObject.next = current.next
            current.next = computerObject

    def remove(self):
        """Removes the first computer"""
        if self.head != None: #Ensures there is a computer to remove
            removedValue = self.head 
            self.head = removedValue.next #Moves the head to the next computer in the linked structure
            removedValue.next = None 
            self.size -= 1
            return removedValue 
        else:
            return None

    def __str__(self):
        """This function prints the linked structure in a menu format."""

        output = "Year purchased  IP address      Storage Space             Operating System\n"
        output += "------------------------------------------------------------------------------\n"
        current = self.head 
        #Loops through the linked structure and adds each computer's details to the output string
        while current: 
            output += str(current) + "\n"
            current = current.next
        return output
