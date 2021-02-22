# Import libraries
from app.training_service.adapter.mongo_repository.db import mongoengine_proj
from flask import Flask
from flask_restful import Api, Resource
from dotenv import load_dotenv
from os.path import join, dirname
from config import DevelopmentConfig
from . import training_service


app = Flask(__name__)

mongo_init = mongoengine_proj
mongoengine_proj.initialize_db(app)

api = Api(app)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path, '.env')
app.config.from_object(DevelopmentConfig())

DevelopmentConfig.URI_MONGO(app)

if __name__ == '__main__':
    app.run(debug=True)