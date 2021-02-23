from app.training_service.views.template_view import ExampleApi
#from . import training_service


class viewsTemplate():

    def initialize_routes(self,api):
        api.add_resource(ExampleApi,'/api/example')