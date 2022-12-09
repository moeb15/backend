from flask import Flask
from flask_restful import Api
from flask_cors import CORS

import os

from resources.homepage import Homepage
from resources.interests import InterestsResource
from resources.cv import CV

def create_app():
    application = app = Flask(__name__)

    register_extensions(app)
    register_resources(app)
    return application

def register_extensions(app):
    CORS(app)


def register_resources(app):
    api = Api(app)

    api.add_resource(Homepage, '/')
    api.add_resource(InterestsResource, '/interests')
    api.add_resource(CV, '/cv')

if __name__ == '__main__':
    application = create_app()
    application.run()