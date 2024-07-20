def outer(fun):
    def inner():
        print("Thanks for Entering into Ocean Academy! ")
        fun()
        print("byeeeeee")
    return inner



@outer       #decorator function assign - method -2
def welcome():
    print("Welcome to Ocean Academy")

# welcome=outer(welcome)  #decorator function #method -1  
welcome()