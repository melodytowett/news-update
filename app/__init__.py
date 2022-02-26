
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
bootstrap = Bootstrap()
#initializing the application
def create_app(config_name):
    app = Flask(__name__)
    #creat app configurations
    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)

    #register the blueprint
    from .main import main as main_blueprint
    app .register_blueprint(main_blueprint)

    #setting config
    from .requests import configure_request
    configure_request(app)


    return app