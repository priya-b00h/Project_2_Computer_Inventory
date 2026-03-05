class LinkedComputer:
    """Represents a linked structure that stores ComputerSystems."""
    def __init__(self):
        self.head = None

    def add(self, computerObject):
        if self.head == None:
            self.head = computerObject
            computerObject.next = None
        elif computerObject.year < self.head.year:
            computerObject.next = self.head
            self.head = computerObject
        else:
            current = self.head
            while current.next and computerObject.year >= current.next.year:
                current = current.next

            computerObject.next = current.next
            current.next = computerObject

    def remove(self):
        if self.head != None:
            removedValue = self.head
            self.head = removedValue.next
            removedValue.next = None
            return removedValue
