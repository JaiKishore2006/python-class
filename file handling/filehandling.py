
#file create

# f=open("first.txt","x")
# print(f)

#WRITE

# f=open("first.txt","w")
# f.write("hello ..... Welcome to Ocean Academy")
# f.close()

# f=open("first.txt","a")
# f.write("  hiii.... jai")
# f.close()


# f=open("first.txt","r")
# print(f.read())
# f.close()

# file2=open("second.txt","r")
# print(file2.read(6))

# print(file2.readline())
# print(file2.readline())

#loop
# for i in file2:
#     print(i)
# file2.close()

#delete

import os

# os.remove("third.txt")

if os.path.exists("third.txt"):
    os.remove("third.txt")
else:
    print("The File does not exists")

#delete folder

os.rmdir("demo")