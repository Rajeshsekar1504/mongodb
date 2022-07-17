import pymongo
client = pymongo.MongoClient("mongodb+srv://rajesh1504:Adhiraj@1504@atlascluster.zxudjtu.mongodb.net/?retryWrites=true&w=majority")
db = client.test

d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )