from .error_model import PostError
import pymongo
from datetime import datetime
from flask import jsonify

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['kenzie']

all_parameters = ['title', 'author', 'tags', 'content']


class Post:

    def __init__(self, title = '', author = '', tags = [], content = '', id = 1,
    created_at = '', updated_at = ''):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content

    
    def create_post(self):    
        self.get_id()        
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        new_post = {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "title": self.title,
            "author": self.author,
            "tags": self.tags,
            "content": self.content
        }        

        db.posts.insert_one(new_post)


    @staticmethod
    def get_all_data():
        data_list = db.posts.find()
        output = []
        
        for post in data_list:
            del post['_id']
            output.append(post)

        return output


    @staticmethod
    def get_single_data(id: int):
           
        output = db.posts.find_one({"id": int(id)})
        if output == None:
            raise PostError('Esse post não existe.', 404)
        del output['_id']

        return output


    def get_id(self):
        id = 0
        try:
            data = self.get_all_data()
            id = data[-1]['id']
        except Exception:
            ...

        self.id = id + 1


    @staticmethod
    def update_data(old_post, new_post: dict):
        new_post['updated_at'] = datetime.now()
        update = {"$set": new_post}

        res = db.posts.update_one(old_post, update)

        return res


    def delete_data(self):
        output = self.get_single_data(self.id)
        
        db.posts.delete_one(output)


    @staticmethod
    def verify_has_all_params(data_request):
        parameters_missing = [param for param in all_parameters if param not in data_request]

        if len(parameters_missing) > 0:
            raise PostError(f'Algumas keys estão faltando.', 400)


    @staticmethod
    def verify_params_are_corret(data_request):
        incorrect_keys = [param for param in data_request if param not in all_parameters]

        if len(incorrect_keys) > 0:
            raise PostError(f'Verifique se as suas keys estão corretas.', 400)
           
        
    def return_info(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "title": self.title,
            "author": self.author,
            "tags": self.tags,
            "content": self.content
        }


