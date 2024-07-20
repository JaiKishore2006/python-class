#Access Modifiers



##class student():
##    def __init__(self):
##        self.name="Google"  #public
##
##studentobj=student()
##print(studentobj.name)
##
##studentobj.name="Googleeeeeeeeee"
##print(studentobj.name)

#protected       
class student():
   def __init__(self):
        self._name="Google"

class emp(student):
    pass

obj=emp()
print(obj._name)



##studentobj=student()
##print(studentobj._name)
##studentobj._name="bjhdgejmd"
##
##print(studentobj._name)



#private
##class Geek:
##
##    # private members
##    __name = None
##    __roll = None
##    __branch = None
##
##    # constructor
##    def __init__(self, name, roll, branch):
##        self.__name = name
##        self.__roll = roll
##        self.__branch = branch
##
##    # private member function
##    def __displayDetails(self):
##
##        # accessing private data members
##        print("Name: ", self.__name)
##        print("Roll: ", self.__roll)
##        print("Branch: ", self.__branch)
##
##
##    def Accessfunction(self):
##        self.__displayDetails()
##        
##
##obj=Geek("jai",1,"ECE")
##obj.Accessfunction()





