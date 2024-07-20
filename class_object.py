#class object


class chennai():
        
        ticketNo=0

        #constructor
        def __init__(self,name,age,role):
                self.name=name
                self.age=age
                self.role=role

        def display(self):
                print("Name:",self.name)
                print("Age:",self.age)
                print("Role:",self.role)
##                print(self.ticketNo)



##        def study(self):
##                print("For study related .....")
##        def work(self):
##                print("For work related")




#object creation

##jai.study()

jai=chennai("jai",18,"student")
jai.display()

priya=chennai("priya",20,"student")
priya.ticketNo=1

priya.display()
print(priya.ticketNo)

