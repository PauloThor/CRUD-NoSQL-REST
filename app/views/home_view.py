from flask import Flask, request

def home_view(app: Flask):

    @app.post('/posts')
    def create_post():
        data = request.get_json()

        return data
    
    return app

    
