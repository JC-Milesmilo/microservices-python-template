from flask_mongoengine import MongoEngine

mongo_db = MongoEngine()
class mongoengine_proj():
    def __init__(self) -> None:
        pass
    def initialize_db(app):
        mongo_db.init_app(app)