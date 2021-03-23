'''
This is the definition for the different methods of the different routes
'''

from flask import Response, request
#from . import training_service
from flask_restful import Resource
from app.errors import SchemaValidationError,InternalServerError
from app.training_service.model.template_model import template_model_db

from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, \
    ValidationError


class ExampleApi(Resource):
    '''
    Class that contains the definition for the api/example routes
    '''
    @staticmethod
    def get():
        '''
        Returns all documents from the collection
        '''
        name = template_model_db.objects().to_json()
        return Response(name, mimetype="application/json",status=200)

    @staticmethod
    def post():
        '''
        Creates a document in the collection
        '''
        try:
            body = request.get_json()
            name_post = template_model_db(**body).save()
            id = template_model_db.id
            return {'id': str(id)},200
        except (FieldDoesNotExist, ValidationError):
            raise (SchemaValidationError)
        except Exception as e:
            raise InternalServerError

class TestApi(Resource):
    def get():
        return 'init'
