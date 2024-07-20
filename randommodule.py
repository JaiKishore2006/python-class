
#random module

##import random
#0- 1 
##print(random.random())


#start - end - float value
##print(random.uniform(10,20))
##
##
###start - end number
##print(random.randint(1,100))
##
###include start
##
##print(random.randrange(10,20))
##
###already data - one 
##my_list=["apple","banana","cherry","gauva","pine apple"]
##print(random.choice(my_list))
##
##print(random.sample(my_list,4))
##random.shuffle(my_list)
##print(my_list)


#collection module

import collections

my_list=["A","A","A","B","B","C","B","A","B"]

print(collections.Counter(my_list))





