#inheritance

#single inheritance
##class dad():
##    def money(self):
##        print("dads money.....")
##    def phone(self):
##        print("dad phone....")
##
##
##class son(dad): #single inheritance
##    def laptop(self):
##        print("son laptop.....")
##
##
##jai=son()
##
##jai.laptop()
##jai.money()
##jai.phone()


#mutiple inheritance


#multiple inheritance
##class dad():
##    def money(self):
##        print("money...dad")
##
##
##class mom():
##    def sweet(self):
##        print("mom ....sweet")
##
##
##class son(dad,mom):
##    def laptop(self):
##        print("son laptop...")
##
##
##jai=son()
##jai.laptop()
##jai.money()
##jai.sweet()



#multilevel inheritance

##class grandfather():
##    def land(self):
##        print("land ...")
##
##class dad(grandfather):
##   def money(self):
##       print("money...dad")
##
##
##class son(dad):
##    def laptop(self):
##        print("son laptop...")
##
##
##
###obj dad
####objdad=dad()
####objdad.money()
####objdad.land()
##
###obj son
##
##objson=son()
##objson.laptop()
##objson.money()
##objson.land()



#hierachial inheritance

class dad():
   def money(self):
       print("money...dad")

class land():
    def land(self):
        print("land...")

class son1(dad,land):
    pass

class son2(dad):
    pass

class son3(dad):
    pass



son1obj=son1()
son1obj.money()
son1obj.land()


#hybrid - single, multiple, hierarchial






        
