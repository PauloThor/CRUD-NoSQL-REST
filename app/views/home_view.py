from flask import Flask, request, jsonify
from app.models.error_model import PostError
from app.models.post_model import Post

def home_view(app: Flask):

    @app.post('/posts')
    def create_post():
        data = request.get_json()

        try:
            Post.verify_has_all_params(data)
            Post.verify_params_are_corret(data)
            
            new_post = Post(data['title'], data['author'], data['tags'], data['content'])
            new_post.create_post()

            return new_post.return_info(), 201

        except PostError as err:
            return err.message, err.status


    @app.get('/posts')
    def read_posts():
        output = Post.get_all_data()
        return jsonify(output), 200


    @app.get('/posts/<post_id>')
    def read_post(post_id: int):
        try:
            output = Post.get_single_data(int(post_id))

            return jsonify(output), 200
        except PostError as err:
            return err.message, err.status


    @app.delete('/posts/<post_id>')
    def delete_post(post_id: int):
        try:
            post_to_be_deleted = Post(id = int(post_id))
            post_to_be_deleted.delete_data()

            return {"msg": "Post excluído."}, 200
        except PostError as err:
            return err.message, err.status


    @app.patch('/posts/<post_id>')
    def update_post(post_id: int):
        data = request.get_json()
        try:
            Post.verify_params_are_corret(data)

            post_to_be_updated = Post.get_single_data(int(post_id))
            Post.update_data(post_to_be_updated, data)            

            updated_post = Post.get_single_data(post_id)

            return updated_post, 200
        except PostError as err:
            return err.message, err.status

   
    return app


