from app.training_service.adapter.mongo_repository import db

db_mongo = db.mongo_db

class template_model_db(db_mongo.Document):
    name = db_mongo.StringField(required=True, unique=True)