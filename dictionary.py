#dictionary

#ordered, changable, do not allow duplicate value

##car={"name":"A-6",
##    "brand":"BMW",
##    "color":"black",
##    "CarNo":121,
##     "color":"white"
##    }
##print(car)
##
###using dict constructor
##
##car=dict(name="A-6",brand="BMW",Color="red")
##print(car)

#access by key
##car={"name":"A-6",
##    "brand":"BMW",
##    "color":"black",
##    "CarNo":121
##    }
##print(car["brand"])

#using get()
##print(car.get("color"))

##print(car.items())

#change

##car["color"]="red"
##print(car)

#update

##car.update({"color":"white"})
##
##print(car)

##car["year"]=2024
##print(car)

#loop
##car={"name":"A-6",
##    "brand":"BMW",
##    "color":"black",
##    "CarNo":121
##    }
##
##for i in car.items():
##    print(i)


#nested dictionary

student={
    "student1":{
        "name":"jai",
        "age":18
        },
    "student2":{
        "name":"priya",
        "age":18
        },
    "student3":{
        "name":"kishore",
        "age":18
        }


    }

print(student["student1"]["name"])

#seperate
##student1={
##        "name":"jai",
##        "age":18
##        }
##
##student2={
##        "name":"priya",
##        "age":18
##        }
##
##student3={
##        "name":"kishore",
##        "age":18
##        }
##
##student={
##    "student1":student1,
##    "student2":student2,
##    "student3":student3
##    }
##
##print(student)
##
##








