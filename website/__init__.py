from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECREAT_KEY']= 'wfe&wocjpijj7674@#wvpep13pvpv'
    

    from .views import views
    from .auth import auth

    app.register_blueprint(views , url_prefic ='/')
    app.register_blueprint(auth , url_prefix = '/' )
    return app