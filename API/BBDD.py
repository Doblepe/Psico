import pymongo

class BBDD:
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = myclient['psico']
    peques = mydb["peques"]
    padres = mydb["padres"]
    agenda = mydb["Agenda"]
# We will add the right connection with the variable Mongo_URI =
mydb = BBDD.myclient['psico']
peques = mydb["peques"]
padres = mydb["padres"]
agenda = mydb["Agenda"]

# data = {"nombre": "Juan Pérez", "Privado": True}

# peques.insert_one(data)