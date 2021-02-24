import os
from dotenv import load_dotenv

load_dotenv(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '.env')))

class BaseConfig(object):
    DEBUG = True
    MONGO_CONFIG = os.environ.get("MONGODB_SETTINGS")
class DevelopmentConfig(object):
    DEBUG = True
    MONGO_CONFIG = os.getenv("MONGODB_SETTINGS")
    def URI_MONGO(app):
        app.config['MONGODB_SETTINGS'] = {
            'host': os.getenv("MONGODB_SETTINGS")
            }