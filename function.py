#function

##def SayHi():
##    print("hii ....")
##
##    
##SayHi()

##def even():
##    n=int(input("enter a number"))
##    if n%2==0:
##        print("even")
##    else:
##        print("odd")
##even()


#function with arguments and parameters

##def even(n):
##    if n%2==0:
##        print("even")
##    else:
##        print("odd")
##even(3)


#arguments types

##def add(x,y):
##    print(x+y)
##
##add(1,2)

##def add(x,y):
##    print(x+y)
##
##add(x=2,y=5)

#using return

##def add(x,y):
##    print("hi")
##    return x+y
##    
##print(add(2,3))



#args - non keyword arguments

##def sum(*num):
##    sum=0
##    for i in num:
##        sum=sum+i
##
##    print(f"sum: {sum}")
####    return sum
##sum(2,3,4,5,6,89)


#kwargs - keyword arguments

##def intro(**data):
##    for i ,j in data.items():
##        print(i,j)
##
##
##intro(name="jai",age=21)
##


##def sayHi(name):
##    print("hi...."+name)
##    
##sayHi("jai")


#lambda or anonymous function

##x=lambda x,y: print(x+y)
##x(2,3)

x=lambda y: f"{y} even" if y%2==0 else f"{y} odd"
print(x(6))

















    
