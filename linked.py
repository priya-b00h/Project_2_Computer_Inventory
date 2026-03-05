class LinkedComputer:
    """Represents a linked structure that stores ComputerSystems."""
    def __init__(self):
        """Initiates head to none, as there are no items yet"""
        self.head = None
        self.size = 0

    def add(self, computerObject):
        """This function adds a computerObject into the correct position"""

        self.size += 1

        if self.head == None:
            self.head = computerObject
            computerObject.next = None
        elif computerObject.year < self.head.year:
            computerObject.next = self.head
            self.head = computerObject
        else:
            current = self.head
            """Moves through the linked structure until the new object is in the correct spot"""
            while current.next and computerObject.year >= current.next.year:
                current = current.next

            computerObject.next = current.next
            current.next = computerObject

    def remove(self):
        """Removes the first computer"""
        if self.head != None:
            removedValue = self.head
            self.head = removedValue.next
            removedValue.next = None
            self.size -= 1
            return removedValue
    
    def __str__(self):
        """This function prints the linked structure in a menu format."""

        print("Year purchased  IP address      Storage Space         Operating System")
        print("----------------------------------------------------------------------")
        print("2016".ljust(15), "1.1.1.1".ljust(15), "Filesystem, 999 GB".ljust(21), "Windows 11")