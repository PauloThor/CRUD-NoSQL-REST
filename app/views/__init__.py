from flask import Flask


def init_app(app: Flask):
    from app.views.home_view import home_view
    home_view(app)

    return app