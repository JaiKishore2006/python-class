#set
#unordered, unchangable,  does not allow duplicate
#create
##my_set={"jai",1,False,"priya","tharshini",2,3,0,True}

#using set constructor
##new_set=set(("priya",1,2,3))

##my_set={"jai",1,False,"priya","tharshini",2,3,0,True,"jai"}

##print(my_set)

#access
##my_set={"jai",1,False,"priya","tharshini",2,3,0,True,"jai"}
##
##for i in my_set:
##    print(i)

##my_set={"jai",1,False,"priya","tharshini",2,3,0,True,"jai"}
##print("jai" in my_set)

#add

##my_set={1,2,3,4}
##my_set.add(5)
##
##print(my_set)

#remove
##my_set={1,2,3,4}
##my_set.discard (3)
##print(my_set)

##my_set={1,2,3,4}
##my_set.pop()
##print(my_set)

#join
##my_set={1,2,3,4}
##new_set={5,6,4}
##res=my_set|new_set
##print(res)

my_set={1,2,3,4}
new_set={5,6,4}
my_set.update(new_set)
print(my_set)





