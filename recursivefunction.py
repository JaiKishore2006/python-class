#recursive function

# def m3():
#     print("m3...")


# def m2():
#     m3()
#     print("m2...")
   

# def m1():
#     m2()
#     print("m1....")
    

# m1()


def print10(n):
    print(n)
    if n!=0:
      print10(n-1)

print10(10)