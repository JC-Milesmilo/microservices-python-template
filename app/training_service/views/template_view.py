from app.errors import SchemaValidationError,InternalServerError
from flask import Response, request
#from . import training_service
from flask_restful import Resource

from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, \
    ValidationError


class ExampleApi(Resource):
    def get(self):
        return {'try': 'try'}, 200
    def post(self):
        try:
            return {'id': 'try'},200
        except (FieldDoesNotExist, ValidationError):
            raise (SchemaValidationError)
        except Exception as e:
            raise InternalServerError

class TestApi(Resource):
    def get():
        return 'init'