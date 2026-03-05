"""
Names: Ian Gui and Priya Prabhu
Assignment: Project 2 - Computer Inventory
Due Date: 03/05/2026
Description: This file contains the ComputerSystem and its subclasses Windows and Linux. 
The ComputerSystem class intializes with an ip address, a purchase_year (this is a hidden
property) and an operating system. It also has an abstract getSpace() and a str() formatting 
method. Its subclasses inherit these properties and also have either a File system capacity 
attribute or c drive capacity attribute depending on whether they are a Windows ComputerSystem 
or Linux ComputerSystem. In these subclasses, the abstract methodgetSpace() will be implemented 
based on the type.
"""


class ComputerSystem:
    """Class for computer system objects."""
    
    def __init__(self, ip, year, os):
        """Initializes the computer system with IP address, purchase year, operating system, and next pointer for linked list."""
        self.ip = ip
        self.__purchase_year = year  # hidden property
        self.os = os
        self.next = None  # for linked list

    #hidden property for purchase year with getter and setter
    @property
    def purchase_year(self):
        """Getter for the purchase year."""
        return self.__purchase_year

    @purchase_year.setter
    def purchase_year(self, value):
        """Setter for the purchase year."""
        self.__purchase_year = value

    #Abstract Method
    def getSpace(self):
        """to be implemented by subclasses"""
        pass

    def __str__(self):
        """String representation of the computer system, formatted for display in the inventory."""
        return f"{str(self.purchase_year).ljust(16)}" + \
               f"{self.ip.ljust(16)}" + \
               f"{str(self.getSpace()).ljust(28)}" + \
               f"{self.os}"


class Windows(ComputerSystem):
    """Subclass of ComputerSystem for Windows computers."""

    def __init__(self, ip, year, os, c_drive):
        """Initializes the Windows computer with specific attributes and calls the parent constructor."""
        super().__init__(ip, year, os)
        self.c_drive = c_drive

    def getSpace(self):
        """Returns the C drive capacity for Windows computers."""
        return f"C Drive: {self.c_drive}"


class Linux(ComputerSystem):
    """Subclass of ComputerSystem for Linux computers."""

    def __init__(self, ip, year, os, fs):
        """Initializes the Linux computer with specific attributes and calls the parent constructor."""
        super().__init__(ip, year, os)
        self.fs = fs

    def getSpace(self):
        """Returns the file system capacity for Linux computers."""
        return f"Filesystem: {self.fs}"
