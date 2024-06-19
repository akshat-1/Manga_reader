from flask import Flask
from gunicorn.http import message


def create_app():
    app = Flask(__name__)
    app.config['SECREAT_KEY']= 'wfe&wocjpijj7674@#wvpep13pvpv'
    message.MAX_REQUEST_LINE = 2**16 - 2
    

    from .views import views
    from .auth import auth

    app.register_blueprint(views , url_prefic ='/')
    app.register_blueprint(auth , url_prefix = '/' )
    return app