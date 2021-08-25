import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['kenzie']

new_data = {"nome": "Cassio", "idade": 32}

db.posts.insert_one(new_data)

new_datas = [
    {"nome": "Cassio", "idade": 32},
    {"nome": "Luís", "idade": 30},
    {"nome": "Renato", "idade": 52},
    {"nome": "Paulo", "idade": 92}
]

db.posts.insert_many(new_datas)

def add_data(data):
    output = {
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "id": get_id(data.name),
        **data
    }
    db.posts.insert_one(output)


def get_id(name: str):
    id = 0
    try:
        id = db.posts.find_one({"name": name}).id
    except Exception:
        ...

    return id + 1

data = db.post.find_one({"nome": "Cassio"})
print(data)

data_list = db.post.find()
print([user for user in data_list])

update = {"$set": {"idade": 26, "clt": True}}

data = db.posts.find_one({"nome": "Paulo"})

db.posts.update_one(data, update)

print(data)

db.posts.update_one({"nome": "Henrique"}, update, upsert=True)

data_to_remove = db.posts.find_one({"idade": 30})

db.posts.delete_one(data_to_remove)
