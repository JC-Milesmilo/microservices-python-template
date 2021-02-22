import os
class BaseConfig(object):
    DEBUG = True
    MONGO_CONFIG = os.environ.get("MONGODB_SETTINGS")
class DevelopmentConfig(object):
    DEBUG = True
    MONGO_CONFIG = os.environ.get("MONGODB_SETTINGS")
    def URI_MONGO(app):
        app.config['MONGODB_SETTINGS'] = {
            'host': os.environ.get("MONGODB_SETTINGS")
            }