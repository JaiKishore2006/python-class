from pymongo import MongoClient

link=MongoClient("mongodb://localhost:27017")
mydb=link.python
col=mydb.demo

col1=mydb.sample




database=link.get_database("python")
coleection=database.get_collection("demo")
# document={
#     "name":"jai",
#     "age":18
# }

# result=col.insert_one(document)
# print(result)


# document=[]

# document1={
#     "name":"kishore",
#     "age":18
# }

# document2={
#     "name":"priya",
#     "age":16
# }
# document3={
#     "name":"Tharshini",
#     "age":20,
# }

# document.append(document1)
# document.append(document2)
# document.append(document3)
# print(document)

# result=col.insert_many(document)
# print(result)


#find


# result=col.find()

# for i in result:
#     print(i)

# result=col.find_one()

# print(result)

#query

# result=col.find({"age":16})


# for i in result:
#     print(i)

# result=col.find().sort("name",-1)

# for i in result:
#     print(i)

#update

# result=col.update_one({"age":16},{"$set":{"age":21}})
# print(result)

#delete
# result=col.delete_one({"name":"jai"})
# print(result)

# document={
#     "name":"jai",
#     "age":18
# }

# result=col1.insert_one(document)
# print(result)



# col1.drop()




