from flask import Flask
from config import Config_options
#initializing the application
def create_app(config_name):
    app = Flask(__name__)
    #creat app configurations
    app.config.from_object(Config_options[config_name])

    return app