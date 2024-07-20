#exception handling

#syntax error

##x=5
##if x==5:
## print("success")


#exception

##x=12
##
##y="jai"
##
##try:
##    z=x+y
##    print(z,"add")
##
##except Exception as error:
##    print("Error",error)


#raise

try:
    raise NameError("hi there")

except NameError:
    print("exception")
    

    
