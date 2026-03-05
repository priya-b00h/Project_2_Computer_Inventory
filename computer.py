
class ComputerSystem():

    def __init__(self, ip, purchase_year, os, c_drive):
        self.ip = ip
        self.__purchase_year = purchase_year
        self.os = os
        self.c_drive = c_drive

    def getSpace(self):
        pass

    @property
    def purchase_year(self):
        return self.__purchase_year

    @purchase_year.setter
    def purchase_year(self, value):
        self.__purchase_year = value

    def __str__(self):
        return f"{self.purchase_year} {self.ip} {self.c_drive} {self.os}"

class Linux(ComputerSystem):

    def _init_(self, fs): 
        super()._init_()
        self.fs = fs
    
    def getSpace(self):
        return self.fs
    
class Windows(ComputerSystem):
    
    def _init_(self): 
        super()._init_()
    
    def getSpace(self):
        return self.c_drive
    



#test
